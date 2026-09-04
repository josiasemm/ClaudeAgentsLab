<div align="center">

<br/>

<img src="images/claudebanner.gif" width="120" />

# ClaudeAgentsLab

<p><b>Specialized read-only Claude Code subagents for automated Python & Pytest QA.</b></p>

</div>

<img src="images/orange-line.gif" width="100%"/>

<img align="right" src="images/clawdlaptop.gif" width="220"/>

When you give an AI model full access to your codebase, it tends to do too much — editing things it shouldn't, missing subtle bugs, or hallucinating fixes. **ClaudeAgentsLab** takes a different approach: instead of one model doing everything, it uses specialized subagents with read-only permissions that focus exclusively on finding what's broken, without touching a single file.

Two agents, two jobs:
- One audits your code logic — types, null references, broken contracts
- One audits your tests — missing edge cases, weak assertions, uncovered error paths

No writes. No side effects. Just honest, structured reports.

<br clear="right"/>

<img src="images/orange-line.gif" width="100%"/>

### ↳ Architecture & Ecosystem 🏗️

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

<img src="images/orange-line.gif" width="100%"/>

### ↳ Subagents Catalog 🤖

| Subagent | Model | Permissions | Focus |
| :--- | :---: | :---: | :--- |
| **`code-reviewer`** | Claude Sonnet | `Read`, `Grep`, `Glob` | Runtime bug detection (`TypeError`, `None` dereferencing), inverted boolean logic and broken function contracts. Ignores cosmetic issues. |
| **`test-reviewer`** | Claude Sonnet | `Read`, `Grep`, `Glob` | Detection of missing edge cases, untested functions, weak assertions and uncovered error paths in `pytest`. |

<img src="images/orange-line.gif" width="100%"/>

### ↳ Skills & Playbooks 📜

Modular, reusable guidelines that teach any agent in the ecosystem the rigorous review protocol:

* 📋 **`python-code-review`**: Discards cosmetic warnings (line length, quotes) and focuses exclusively on functional bugs, incorrect assumptions and serious maintainability issues.
* 🧪 **`python-test-review`**: Evaluates the ability of tests to detect production regressions, requiring verification of empty collections, null inputs and data invariants.

<img src="images/orange-line.gif" width="100%"/>

### ↳ Testbench & Detected Bugs 🔍

The `src/tasks.py` module deliberately contains architectural defects to evaluate the precision of the `code-reviewer` subagent:

```python
# ❌ Bug 1: Inverted logic in pending tasks
def get_pending_tasks(tasks):
    return [task for task in tasks if task["completed"] is True]  # Returns completed instead of pending!

# ❌ Bug 2: Possible TypeError from None dereferencing
def complete_task(tasks, task_id):
    task = find_task(tasks, task_id)
    task["completed"] = True  # Crashes if task_id doesn't exist and returns None!
    return task

# ❌ Bug 3: Hardcoded identifier
def create_task(title):
    return {"id": 1, "title": title, "completed": False}  # All IDs collide at 1
```

> **Agent result:** The `code-reviewer` subagent isolates all 3 defects without modifying the source file, emitting a structured report with diagnostics and proposed fixes.

<img src="images/orange-line.gif" width="100%"/>

### ↳ Quickstart 💻

```bash
# 1. Clone the repository
git clone https://github.com/josiasemm/ClaudeAgentsLab.git
cd ClaudeAgentsLab

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the unit test suite
pytest -v
```

<img src="images/orange-line.gif" width="100%"/>

### ↳ License 📄

Distributed under the MIT License. See [LICENSE](LICENSE) for more details.

<div align="center">
<img src="images/claudefutbol.gif" width="80"/>
</div>