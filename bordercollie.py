#!/usr/bin/env python3
"""
bordercollie — Herd class for managing many local agents
Herd.spawn(n) → create n agents
Herd.distribute(tasks) → assign work
Herd.gather() → collect results
"""

import json, time, uuid, threading, queue
from typing import List, Dict, Callable, Any, Optional
from dataclasses import dataclass, field
from concurrent.futures import ThreadPoolExecutor, as_completed

@dataclass
class Agent:
    id: str
    name: str
    status: str = "idle"  # idle, working, done, error
    task: Optional[str] = None
    result: Any = None
    error: Optional[str] = None
    started_at: Optional[float] = None
    finished_at: Optional[float] = None

@dataclass
class Task:
    id: str
    payload: Any
    assigned_to: Optional[str] = None
    status: str = "pending"  # pending, running, done, failed
    result: Any = None

class Herd:
    def __init__(self, name: str = "default"):
        self.name = name
        self.agents: Dict[str, Agent] = {}
        self.tasks: List[Task] = []
        self.results: queue.Queue = queue.Queue()
        self._lock = threading.Lock()
    
    def spawn(self, n: int, prefix: str = "agent") -> List[str]:
        """Create n agents. Returns list of agent IDs."""
        ids = []
        for i in range(n):
            aid = f"{prefix}-{uuid.uuid4().hex[:8]}"
            self.agents[aid] = Agent(id=aid, name=f"{prefix}-{i+1}")
            ids.append(aid)
        return ids
    
    def distribute(self, tasks: List[Any], worker_fn: Callable[[Any], Any], max_workers: Optional[int] = None):
        """Distribute tasks across agents using thread pool."""
        max_workers = max_workers or len(self.agents)
        self.tasks = [Task(id=str(uuid.uuid4())[:8], payload=t) for t in tasks]
        
        agent_ids = list(self.agents.keys())
        
        def run_task(task: Task, agent_id: str) -> None:
            agent = self.agents[agent_id]
            agent.status = "working"
            agent.task = task.id
            agent.started_at = time.time()
            task.assigned_to = agent_id
            task.status = "running"
            
            try:
                result = worker_fn(task.payload)
                task.status = "done"
                task.result = result
                agent.result = result
                agent.status = "done"
            except Exception as e:
                task.status = "failed"
                agent.error = str(e)
                agent.status = "error"
            finally:
                agent.finished_at = time.time()
                self.results.put((agent_id, task.id, task.result, agent.error))
        
        with ThreadPoolExecutor(max_workers=max_workers) as ex:
            futures = []
            for i, task in enumerate(self.tasks):
                agent_id = agent_ids[i % len(agent_ids)]
                future = ex.submit(run_task, task, agent_id)
                futures.append(future)
            
            for future in futures:
                future.result()
    
    def gather(self) -> Dict[str, Any]:
        """Collect all results. Returns {agent_id: result}."""
        return {aid: agent.result for aid, agent in self.agents.items() if agent.status == "done"}
    
    def status(self) -> Dict:
        """Current herd status."""
        idle = sum(1 for a in self.agents.values() if a.status == "idle")
        working = sum(1 for a in self.agents.values() if a.status == "working")
        done = sum(1 for a in self.agents.values() if a.status == "done")
        error = sum(1 for a in self.agents.values() if a.status == "error")
        return {
            "total_agents": len(self.agents),
            "idle": idle,
            "working": working,
            "done": done,
            "error": error,
            "tasks_total": len(self.tasks),
            "tasks_done": sum(1 for t in self.tasks if t.status == "done"),
            "tasks_failed": sum(1 for t in self.tasks if t.status == "failed"),
        }
    
    def eject(self, agent_id: str) -> Optional[Agent]:
        """Remove an agent from the herd. Returns the agent if found."""
        with self._lock:
            return self.agents.pop(agent_id, None)
    
    def inject(self, agent: Agent):
        """Add an existing agent to the herd."""
        with self._lock:
            self.agents[agent.id] = agent

def demo():
    """Demo: 5 agents processing 10 tasks."""
    herd = Herd(name="tile-processors")
    
    # Spawn 5 agents
    ids = herd.spawn(5, prefix="processor")
    print(f"Spawned {len(ids)} agents")
    
    # Create 10 tasks
    tasks = [f"process-tile-{i}" for i in range(10)]
    
    # Worker function: simulate processing
    def worker(payload: str) -> Dict:
        time.sleep(0.1)  # Simulate work
        return {"processed": payload, "timestamp": time.time()}
    
    # Distribute
    print(f"Distributing {len(tasks)} tasks...")
    herd.distribute(tasks, worker, max_workers=5)
    
    # Gather
    results = herd.gather()
    print(f"\nGathered {len(results)} results:")
    for aid, result in results.items():
        print(f"  {aid}: {result['processed']}")
    
    # Status
    stats = herd.status()
    print(f"\nHerd status: {stats['done']}/{stats['total_agents']} done, {stats['error']} errors")

if __name__ == "__main__":
    demo()
