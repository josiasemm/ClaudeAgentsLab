# 📋 Task Manager — Claude Code en Acción

> Proyecto de gestión de tareas con configuración de **Skills** y **Subagentes de Inteligencia Artificial** para revisión y auditoría automatizada de código Python y pruebas unitarias con `pytest`.

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Testing: Pytest](https://img.shields.io/badge/Testing-Pytest-yellow.svg)](https://docs.pytest.org/)
[![Claude Code Agent Ready](https://img.shields.io/badge/Agentic-Claude%20Code-purple.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📖 Descripción del Proyecto

Este repositorio fue desarrollado como práctica del módulo **Clase 3 - Claude Code en acción**, enfocado en la creación de agentes autónomos y manuales de procedimientos (*Skills*) aplicados al aseguramiento de calidad de software (*QA & Code Review*).

El sistema incluye una aplicación básica de lista de tareas diseñada con casos límite y desafíos lógicos deliberados, junto con dos inspectores de IA configurados bajo un estricto protocolo de **sólo lectura** (`Read`, `Grep`, `Glob`).

---

## 🗂️ Estructura del Proyecto

```text
task-manager/
├── .claude/
│   ├── agents/
│   │   ├── code-reviewer.md        # Subagente auditor de código Python
│   │   └── test-reviewer.md        # Subagente auditor de cobertura con pytest
│   └── skills/
│       ├── python-code-review/
│       │   └── SKILL.md            # Reglas y protocolo para revisión de código
│       └── python-test-review/
│           └── SKILL.md            # Reglas y protocolo para revisión de pruebas
├── .agents/                        # Espejo compatible con Antigravity
├── src/
│   ├── tasks.py                    # Lógica de manipulación de tareas
│   └── validation.py               # Validaciones de reglas de negocio
├── tests/
│   ├── test_tasks.py               # Pruebas unitarias de tareas
│   └── test_validation.py          # Pruebas unitarias de validación
├── requirements.txt                # Dependencias del entorno
├── README.md                       # Documentación
└── LICENSE                         # Licencia MIT
```

---

## 🤖 Agentes y Skills Configuradas

### 1. Subagente `code-reviewer` (`.claude/agents/code-reviewer.md`)
* **Modelo:** Sonnet.
* **Permisos:** Modo exclusivo de sólo lectura (`Read`, `Grep`, `Glob`).
* **Responsabilidad:** Detectar bugs reales de funcionamiento, suposiciones incorrectas (ej. desreferenciación de `None`, IDs hardcodeados) y problemas de mantenibilidad, ignorando aspectos puramente cosméticos.

### 2. Subagente `test-reviewer` (`.claude/agents/test-reviewer.md`)
* **Modelo:** Sonnet.
* **Permisos:** Modo exclusivo de sólo lectura (`Read`, `Grep`, `Glob`).
* **Responsabilidad:** Auditar la batería de tests en `tests/`, detectando funciones sin cobertura, casos límite no contemplados y aserciones débiles.

### 3. Skills del Repositorio (`.claude/skills/`)
* **`python-code-review`:** Guía metodológica para la inspección funcional y robustez en Python.
* **`python-test-review`:** Guía metodológica para la auditoría de rigor en suites de `pytest`.

---

## 💻 Instalación y Pruebas

### Prerrequisitos
* Python 3.10 o superior
* Git

### Ejecución local
```bash
# 1. Clonar el repositorio
git clone https://github.com/josiasemm/task-manager.git
cd task-manager

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar la suite de pruebas
pytest -v
```

---

## 📄 Licencia
Distribuido bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más información.

---

## 👤 Autor

**Josias Emmanuel González Moreno**
* 🎓 Estudiante de **Ingeniería en Software** e **Ingeniería Física**.
* 💡 Apasionado por el desarrollo de software, la simulación científica y los flujos de trabajo con agentes de IA.
* 🐙 **GitHub:** [@josiasemm](https://github.com/josiasemm)
