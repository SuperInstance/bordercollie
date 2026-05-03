**Topics:** `fleet-coordination` `agent-herding` `synchronization` `task-routing` `distributed-agents` `cocapn`

---

# BorderCollie — Fleet Herding Agent

> Fleet herding at scale — keeping 10,000+ agents aligned and heading in the same direction.

**BorderCollie** is a **fleet coordination agent** that keeps distributed AI agents synchronized and heading toward shared goals. Like a border collie managing sheep, it manages, groups, and directs tasks across distributed systems — ensuring no agent drifts off course while the herd moves together.

Part of the [Cocapn fleet](https://github.com/SuperInstance) — lighthouse keeper architecture.

---

## What It Does

BorderCollie manages the **alignment problem** in distributed agent fleets:

- **Alignment** — Ensures all agents see consistent goals and constraints
- **Synchronization** — Keeps agent state and configuration in sync across the fleet
- **Herding** — Detects drift and nudges agents back on course
- **Grouping** — Organizes agents into working groups (teams, roles, specializations)

### Key Features

- **Goal propagation** — Push goals to all agents in the herd
- **Drift detection** — Monitor agent behavior against expected baseline
- **Priority routing** — High/medium/low priority task distribution
- **Status tracking** — Real-time view of aligned vs. drifting agents

---

## Quick Start

### Install

```bash
pip install cocapn-bordercollie
```

### Basic Usage

```python
from bordercollie import Herd

# Create a herd
herd = Herd()

# Register agents with roles
herd.add("oracle1", {"role": "coordinator", "capacity": 100})
herd.add("jetson1", {"role": "worker", "capacity": 60})
herd.add("ccc1", {"role": "worker", "capacity": 40})

# Herd toward a goal
herd.herd_toward(goal="sync-config", priority="high")

# Check status
status = herd.status()
print(f"Aligned: {status['aligned']}")
print(f"Drifting: {status['drifting']}")
```

### Advanced Usage

```python
from bordercollie import Herd, Priority

# Create herd with configuration
herd = Herd(
    drift_threshold=0.15,      # Flag agents >15% off baseline
    sync_interval=30,          # Re-sync every 30 seconds
    priority=Priority.HIGH
)

# Add agents with metadata
herd.add("agent-1", {"role": "orchestrator", "specialization": "code"})
herd.add("agent-2", {"role": "worker", "specialization": "research"})
herd.add("agent-3", {"role": "worker", "specialization": "docs"})

# Broadcast a goal to a subset
herd.herd_subset(
    goal="audit-fleet",
    filter={"role": "worker"},
    priority=Priority.MEDIUM
)

# Get drift report
drift_report = herd.drift_report()
for agent, drift_score in drift_report.items():
    if drift_score > 0.5:
        print(f"ALERT: {agent} is drifting ({drift_score:.0%})")
```

---

## Architecture

```
bordercollie/
├── README.md
├── CHARTER.md
├── DOCKSIDE-EXAM.md
├── LICENSE
└── tests/
    └── test_bordercollie_docs.py   # Documentation contract tests
```

### Component Overview

| Component | Role |
|-----------|------|
| `Herd` | Main class. Manages agent registry, tracks status |
| Drift Detector | Compares agent behavior against expected baseline |
| Goal Propagator | Broadcasts goals to agents, tracks acknowledgment |
| Priority Router | Routes tasks based on priority and agent capacity |
| Status Monitor | Real-time aligned/drifting counts |

### Herding Flow

```
Goal Input
    │
    ▼
Priority Router
    │
    ├── High priority ──► Immediate broadcast to all agents
    │
    ├── Medium priority ──► Batch broadcast, wait for ack
    │
    └── Low priority ──► Deferred, batch with other goals
    │
    ▼
Drift Detector ◄── Agent Responses
    │
    ├── Agent on target ──► Mark "aligned"
    │
    └── Agent drifted ──► Mark "drifting", send correction
    │
    ▼
Status Report ──► Dashboard / fleet monitor
```

---

## Demo: Herding a Fleet

```python
from bordercollie import Herd, Priority

# Simulate a fleet herding session
herd = Herd()

# Register 5 agents
agents = [
    ("oracle1", {"role": "coordinator"}),
    ("jetson1", {"role": "worker"}),
    ("ccc1", {"role": "worker"}),
    ("forgemaster", {"role": "trainer"}),
    ("scout1", {"role": "explorer"}),
]

for name, meta in agents:
    herd.add(name, meta)

# Herd the fleet toward a configuration sync
result = herd.herd_toward(
    goal="sync-fleet-config-v2",
    priority=Priority.HIGH
)

print("=== Herding Result ===")
print(f"Goal: {result['goal']}")
print(f"Agents targeted: {result['targeted']}")
print(f"Acknowledged: {result['acknowledged']}")
print(f"Drift detected: {result['drift_count']}")
print()
print(herd.status())
```

**Expected output:**

```
=== Herding Result ===
Goal: sync-fleet-config-v2
Agents targeted: 5
Acknowledged: 4
Drift detected: 1

=== Fleet Status ===
Aligned: 4 (oracle1, jetson1, ccc1, forgemaster)
Drifting: 1 (scout1 — last seen 3 sync cycles ago)
```

---

## Fleet Context

Part of the Cocapn fleet. Related repos:

| Repo | Role |
|------|-------|
| [cudaclaw](https://github.com/SuperInstance/cudaclaw) | GPU-accelerated agent orchestration |
| [ai-character-sdk](https://github.com/SuperInstance/ai-character-sdk) | Unified AI character SDK with memory |
| [crab-traps](https://github.com/SuperInstance/crab-traps) | Lure collection for fleet learning |
| [capitaine](https://github.com/Lucineer/capitaine) | The Lucineer flagship repo-agent |
| [fleet-orchestrator](https://github.com/SuperInstance/fleet-orchestrator) | Stateless edge coordination hub |

---
🦐 Cocapn fleet — lighthouse keeper architecture
