# bordercollie

**Herding agent for fleet coordination.** Keeps fleet instances aligned, synchronized, and heading in the same direction — like a border collie manages sheep, this agent manages, groups, and directs tasks across distributed systems.

## Brand Line

> Fleet herding at scale — keeping 10,000+ agents aligned and heading in the same direction.

## Installation

```bash
pip install cocapn-bordercollie
```

## Usage

```python
from bordercollie import Herd

# Create a herd of fleet agents
herd = Herd()

# Add agents to the herd
herd.add("agent-1", {"role": "orchestrator"})
herd.add("agent-2", {"role": "worker"})

# Herd all agents toward a goal
herd.herd_toward(goal="sync-config", priority="high")

# Check herd status
status = herd.status()
print(f"Aligned: {status['aligned']}, Drifting: {status['drifting']}")
```

## Fleet Context

Part of the Cocapn fleet. Related repos:
- [cudaclaw](https://github.com/SuperInstance/cudaclaw) — GPU-accelerated agent orchestration
- [ai-character-sdk](https://github.com/SuperInstance/ai-character-sdk) — Unified AI character SDK with memory
- [crab-traps](https://github.com/SuperInstance/crab-traps) — Lure collection for fleet learning
- [capitaine](https://github.com/Lucineer/capitaine) — The Lucineer flagship repo-agent

---
🦐 Cocapn fleet — lighthouse keeper architecture