---
name: python-test-review
description: >-
  Reviews pytest test suites to detect missing scenarios, edge cases,
  weak assertions, untested error paths, and uncovered critical behaviors.
  Operates strictly in read-only mode without modifying files.
---

# Python Test Review Skill

Esta Skill guía la revisión especializada de suites de pruebas escritas con `pytest`, evaluando la exhaustividad, rigurosidad y calidad de las aserciones sin modificar el código.

## Restricciones estrictas
1. **Solo lectura y búsqueda**:
   - Usar únicamente herramientas de lectura e inspección (`Read`, `Grep`, `Glob`, `view_file`, `grep_search`, `find_by_name`).
   - No modificar, agregar ni eliminar ningún archivo de código o de prueba durante la revisión.
2. **Enfoque en calidad de pruebas**:
   - Evaluar si las pruebas realmente garantizan el comportamiento esperado y protegen contra regresiones.

## Áreas de inspección requeridas

### 1. Escenarios faltantes
- Funciones públicas o módulos en `src/` que carecen por completo de pruebas en `tests/` (por ejemplo, funciones declaradas en código fuente pero nunca importadas en los tests).
- Flujos donde el estado del sistema cambia y no se verifica dicho cambio posterior.

### 2. Casos límite (Edge Cases)
- Comportamiento ante colecciones vacías (listas vacías `[]`, diccionarios vacíos `{}`).
- Entradas nulas (`None`), tipos incorrectos o cadenas en blanco (`""`, `"   "`).
- Identificadores o índices inexistentes (búsquedas que no encuentran coincidencia).

### 3. Aserciones débiles
- Pruebas que solo verifican que no se lance excepción o que el retorno sea un booleano sin validar los datos completos.
- Pruebas que no verifican el valor exacto de las claves del diccionario o atributos de los objetos resultantes.
- Aserciones que permiten falsos positivos.

### 4. Rutas de error sin pruebas
- Caminos alternativos (`if/else`, bloques `except`) donde la función debe retornar `None` o lanzar una excepción específica.
- Verificación de excepciones esperadas mediante `pytest.raises`.

### 5. Comportamientos importantes sin cobertura
- Invariantes de la aplicación (por ejemplo, asegurar que completar una tarea no muta otras tareas de la lista).
- Casos de idempotencia o ejecuciones repetidas.

## Estructura de reporte
Para cada hallazgo:
- **Prueba o Módulo evaluado**: Archivo de prueba y/o archivo fuente correspondiente.
- **Deficiencia identificada**: Escenario faltante | Caso límite | Aserción débil | Ruta de error | Falta de cobertura.
- **Riesgo**: Qué bug podría pasar desapercibido si no se prueba este escenario.
- **Propuesta de prueba**: Esquema o ejemplo de cómo debería ser el caso de prueba con `pytest`.
