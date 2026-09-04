<div align="center">

  <br />

  <img src="images/clawdlaptop.gif" width="115" alt="Claude Code Mascot" />

  # ClaudeAgentsLab

  **Specialized read-only Claude Code subagents for automated Python & Pytest QA.**

  <sub>Dual-pipeline inspection · Zero writes · Strict sandbox</sub>

  <br />
  <br />

  <p align="center">
    <a href="#-overview">Overview</a> &nbsp;•&nbsp;
    <a href="#-architecture--ecosystem">Architecture</a> &nbsp;•&nbsp;
    <a href="#-subagents-catalog">Subagents</a> &nbsp;•&nbsp;
    <a href="#-testbench--detected-defects">Testbench</a> &nbsp;•&nbsp;
    <a href="#-quickstart">Quickstart</a>
  </p>

</div>

---

> [!IMPORTANT]
> **Unrestricted AI agents in production introduce silent regressions.**  
> When a model is given blanket write access, it tends to over-edit, mask broken contracts, or hallucinate fixes. **ClaudeAgentsLab** demonstrates an enterprise-grade safety pattern: **Dual Read-Only Subagents** (`Read`, `Grep`, `Glob`) that rigorously isolate logical flaws and audit `pytest` suites without modifying a single file.

---

## ↳ Overview

**ClaudeAgentsLab** is a dual-pipeline auditing playground designed for the **Claude Code (Anthropic)** ecosystem. Instead of relying on a single generalist agent, it splits quality assurance into two specialized, sandboxed inspectors with strictly partitioned responsibilities:

| Subagent | Persona & Role | Execution Tools | Target Scope |
| :--- | :--- | :---: | :--- |
| **`code-reviewer`** | Senior Python Logic Inspector | `Read`, `Grep`, `Glob` | `src/*.py` · Runtime bugs, `TypeError` on `None`, inverted boolean operators, mutation side-effects. |
| **`test-reviewer`** | Pytest Rigor & Coverage Auditor | `Read`, `Grep`, `Glob` | `tests/*.py` · Uncovered edge-cases, weak assertions, missing error paths, testing idempotency. |

---

## ↳ Architecture & Ecosystem

```text
ClaudeAgentsLab/
├── .claude/
│   ├── agents/
│   │   ├── code-reviewer.md        🤖 Subagent specification (Sonnet · Read-only)
│   │   └── test-reviewer.md        🧪 Subagent specification (Sonnet · Read-only)
│   └── skills/
│       ├── python-code-review/
│       │   └── SKILL.md            📜 Procedural manual for static logic auditing
│       └── python-test-review/
│           └── SKILL.md            📜 Procedural manual for pytest rigor verification
├── .agents/                        🔄 Google Antigravity compatibility mirror
├── src/                            📦 Application source code (vulnerable testbench)
│   ├── tasks.py
│   └── validation.py
├── tests/                          🧪 Unit test suite (baseline coverage)
│   ├── test_tasks.py
│   └── test_validation.py
├── requirements.txt                ⚡ Dependencies (pytest)
├── README.md                       📑 Documentation
└── LICENSE                         ⚖️ MIT open source license
```

---

## ↳ Testbench & Detected Defects

The `src/tasks.py` module intentionally contains 3 critical architectural defects designed to benchmark the diagnostic precision of `code-reviewer`:

### 🔍 Defect 01: Inverted Boolean Logic
```diff
# File: src/tasks.py (Line 25)
- def get_pending_tasks(tasks):
-     return [task for task in tasks if task["completed"] is True]  # ❌ Returns completed tasks!
+ def get_pending_tasks(tasks):
+     return [task for task in tasks if not task.get("completed", False)]  # ✔ Clean logic
```

### 🔍 Defect 02: Potential `TypeError` on Missing Item
```diff
# File: src/tasks.py (Line 18)
- def complete_task(tasks, task_id):
-     task = find_task(tasks, task_id)
-     task["completed"] = True  # ❌ Crashes with TypeError if task_id does not exist (None)!
+ def complete_task(tasks, task_id):
+     task = find_task(tasks, task_id)
+     if task is None:
+         raise ValueError(f"Task {task_id} not found")
+     task["completed"] = True
+     return task
```

### 🔍 Defect 03: Static Identifier Collision
```diff
# File: src/tasks.py (Line 1)
- def create_task(title):
-     return {"id": 1, "title": title, "completed": False}  # ❌ Every task collides with ID 1
+ def create_task(tasks, title):
+     next_id = max([t["id"] for t in tasks], default=0) + 1  # ✔ Deterministic sequence
+     return {"id": next_id, "title": title, "completed": False}
```

<details>
<summary><b>🔎 Click to view how <code>test-reviewer</code> audits the test suite</b></summary>

<br />

The `test-reviewer` subagent inspects `tests/test_tasks.py` and flags:
* **Missing Error Paths:** `find_task()` has zero tests verifying what happens when querying a non-existent ID.
* **Empty Collection Invariants:** No tests validating functions against empty lists `[]`.
* **Weak Assertions:** `test_complete_task()` does not assert that other unrelated tasks remain untouched (mutation leak).

</details>

---

## ↳ Quickstart

### Prerequisites
* Python 3.10+
* Git

### Local Execution
```bash
# 1. Clone the repository
git clone https://github.com/josiasemm/ClaudeAgentsLab.git
cd ClaudeAgentsLab

# 2. Install dependencies
pip install -r requirements.txt

# 3. Execute unit test baseline
pytest -v
```

---

## ↳ License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

<br />

<div align="center">
  <img src="images/claudefutbol.gif" width="75" alt="Claude" />
</div>