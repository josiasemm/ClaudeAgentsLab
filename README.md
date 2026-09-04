<div align="center">

<img src="images/banner.jpg" alt="ClaudeAgentsLab Banner" width="100%" />

<br/>
<br/>

# ClaudeAgentsLab
### Laboratorio de Subagentes Autónomos & Skills de Auditoría para Python

[![Claude Code](https://img.shields.io/badge/Claude%20Code-Anthropic-D97706?style=for-the-badge&logo=anthropic&logoColor=white)](https://docs.anthropic.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-Testing%20Suite-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![License MIT](https://img.shields.io/badge/License-MIT-10B981?style=for-the-badge)](LICENSE)

<p align="center">
  <b>Un entorno experimental para la orquestación de subagentes especializados con permisos de sólo lectura, detección de vulnerabilidades lógicas y aseguramiento de calidad (QA).</b>
</p>

---

</div>

### ↳ Overview 🧪

En el desarrollo de software moderno con Inteligencia Artificial, delegar todo el trabajo a un solo modelo sin restricciones suele generar código roto o alucinaciones. 

**ClaudeAgentsLab** implementa el paradigma de **Agentes Especializados con Permisos Restringidos**:
* 🔒 **Permisos estrictos de sólo lectura:** En lugar de dar acceso total de edición a ciegas, los subagentes operan con "las manos atadas" únicamente usando herramientas de inspección (`Read`, `Grep`, `Glob`).
* 🎯 **Auditoría profunda sin efectos secundarios:** Auditan minuciosamente la lógica, señalan fallos de ejecución y evalúan el rigor de las pruebas sin alterar ni un solo archivo del repositorio.

---

### ↳ Architecture & Ecosystem 🏗️

```text
ClaudeAgentsLab/
├── .claude/
│   ├── agents/
│   │   ├── code-reviewer.md        🤖 Inspector de lógica, tipos y manejo de errores
│   │   └── test-reviewer.md        🧪 Auditor de suites de pruebas con pytest
│   └── skills/
│       ├── python-code-review/
│       │   └── SKILL.md            📜 Manual de procedimiento para análisis estático
│       └── python-test-review/
│           └── SKILL.md            📜 Manual de procedimiento para cobertura de tests
├── .agents/                        🔄 Espejo de compatibilidad con Google Antigravity
├── src/                            📦 Código fuente de la aplicación (Banco de pruebas)
│   ├── tasks.py
│   └── validation.py
├── tests/                          🧪 Batería de pruebas unitarias
│   ├── test_tasks.py
│   └── test_validation.py
├── requirements.txt                ⚡ Dependencias del proyecto
├── README.md                       📑 Documentación técnica
└── LICENSE                         ⚖️ Licencia de código abierto MIT
```

---

### ↳ Subagents Catalog 🤖

| Subagente | Modelo | Permisos | Enfoque Principal |
| :--- | :---: | :---: | :--- |
| **`code-reviewer`** | Claude Sonnet | `Read`, `Grep`, `Glob` | Detección de bugs de ejecución (`TypeError`, desreferenciación de `None`), lógica booleana invertida y contratos de función rotos. Ignora aspectos cosméticos. |
| **`test-reviewer`** | Claude Sonnet | `Read`, `Grep`, `Glob` | Detección de casos límite omitidos (edge cases), funciones sin pruebas, aserciones débiles y rutas de error no cubiertas en `pytest`. |

---

### ↳ Skills & Playbooks 📜

Directrices modulares y reutilizables que enseñan a cualquier agente del ecosistema el protocolo riguroso de revisión:

* 📋 **`python-code-review`**: Descarta advertencias cosméticas (longitud de línea, comillas) y focaliza la atención exclusivamente en bugs funcionales, suposiciones incorrectas y problemas graves de mantenibilidad.
* 🧪 **`python-test-review`**: Evalúa la capacidad de las pruebas para detectar regresiones en producción, exigiendo verificación de colecciones vacías, entradas nulas e invariantes de datos.

---

### ↳ Testbench & Detected Bugs 🔍

El módulo `src/tasks.py` contiene deliberadamente defectos arquitectónicos para evaluar la precisión del subagente `code-reviewer`:

```python
# ❌ Defecto 1: Lógica invertida en tareas pendientes
def get_pending_tasks(tasks):
    return [task for task in tasks if task["completed"] is True]  # Retorna completadas en vez de pendientes!

# ❌ Defecto 2: Posible TypeError por desreferenciación de None
def complete_task(tasks, task_id):
    task = find_task(tasks, task_id)
    task["completed"] = True  # Explota si task_id no existe y retorna None!
    return task

# ❌ Defecto 3: Identificador hardcodeado
def create_task(title):
    return {"id": 1, "title": title, "completed": False}  # Todos los IDs colisionan en 1
```

> **Resultado del agente:** El subagente `code-reviewer` aísla los 3 defectos sin modificar el archivo fuente, emitiendo un reporte estructurado con diagnósticos y propuestas de solución.

---

### ↳ Quickstart & Testing 💻

* **Prerrequisitos:** Python 3.10+ y Git instalados.

```bash
# 1. Clonar el repositorio
git clone https://github.com/josiasemm/ClaudeAgentsLab.git
cd ClaudeAgentsLab

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar la suite de pruebas unitarias
pytest -v
```

---

### ↳ License 📄

Distribuido bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

### ↳ Author 👤

<div align="center">

**Josias Emmanuel González Moreno**  
*Estudiante de Ingeniería en Software e Ingeniería Física*

[![GitHub](https://img.shields.io/badge/GitHub-josiasemm-181717?style=flat&logo=github)](https://github.com/josiasemm)
[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

*Apasionado por la inteligencia artificial aplicada, la ingeniería de software y el modelado computacional.*

</div>
