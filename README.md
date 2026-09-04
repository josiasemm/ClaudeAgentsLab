<div align="center">

  <br />

  <img src="images/clawdlaptop.gif" width="130" alt="ClaudeAgentsLab Mascot" />

  # ClaudeAgentsLab

  **Specialized read-only Claude Code subagents for automated Python & Pytest QA.**

  <sub>Zero writes · Zero mutations · Strict logical inspection</sub>

</div>

<br />

---

## ↳ Overview

When you give an AI agent unrestricted write access to your codebase, things break. Models tend to over-edit, introduce subtle regressions, or hallucinate fixes for non-existent issues.

**ClaudeAgentsLab** demonstrates a safer architectural pattern: **Subagents with "hands tied"**. Instead of one model doing everything, it deploys two specialized inspectors restricted to read-only tools (`Read`, `Grep`, `Glob`) that audit your code and test suite without modifying a single file.

| Subagent | Role | Allowed Tools | Focus |
| :--- | :---: | :---: | :--- |
| **`code-reviewer`** | Code Logic Inspector | `Read`, `Grep`, `Glob` | Catches runtime bugs (`TypeError`, `None` dereferences), inverted logic, and broken function contracts. |
| **`test-reviewer`** | Test Suite Auditor | `Read`, `Grep`, `Glob` | Identifies missing edge cases, untested functions, weak assertions, and uncovered error paths in `pytest`. |

---

## ↳ Architecture & Ecosystem

```text
ClaudeAgentsLab/
├── .claude/
│   ├── agents/
│   │   ├── code-reviewer.md        🤖 Logic, types and error handling inspector
│   │   └── test-reviewer.md        🧪 Pytest suite auditor
│   └── skills/
│       ├── python-code-review/
│       │   └── SKILL.md            📜 Static analysis procedure manual
│       └── python-test-review/
│           └── SKILL.md            📜 Test coverage procedure manual
├── .agents/                        🔄 Google Antigravity compatibility mirror
├── src/                            📦 Application source code (testbench)
│   ├── tasks.py
│   └── validation.py
├── tests/                          🧪 Unit test suite
│   ├── test_tasks.py
│   └── test_validation.py
├── requirements.txt                ⚡ Project dependencies
├── README.md                       📑 Technical documentation
└── LICENSE                         ⚖️ MIT open source license
```

---

## ↳ Testbench & Detected Defects

The `src/tasks.py` module deliberately contains architectural defects to verify the subagents' diagnostic accuracy:

```python
# ❌ Defect 1: Inverted boolean logic (returns completed instead of pending)
def get_pending_tasks(tasks):
    return [task for task in tasks if task["completed"] is True]

# ❌ Defect 2: TypeError on None dereference when task_id does not exist
def complete_task(tasks, task_id):
    task = find_task(tasks, task_id)
    task["completed"] = True
    return task

# ❌ Defect 3: Hardcoded static identifier collision
def create_task(title):
    return {"id": 1, "title": title, "completed": False}
```

> **Agent Audit Result:** The `code-reviewer` isolates all 3 defects without touching the source file, outputting structured diagnosis and remediation code.

---

## ↳ Quickstart

```bash
# 1. Clone the repository
git clone https://github.com/josiasemm/ClaudeAgentsLab.git
cd ClaudeAgentsLab

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the unit test suite
pytest -v
```

---

## ↳ License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

<br />

<div align="center">
  <img src="images/claudefutbol.gif" width="75" alt="Claude" />
</div>