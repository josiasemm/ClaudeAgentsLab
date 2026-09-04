---
name: python-code-review
description: >-
  Reviews Python source code to detect runtime bugs, incorrect assumptions,
  missing error handling, and critical maintainability issues. Ignores cosmetic
  formatting issues and operates strictly in read-only mode without modifying files.
---

# Python Code Review Skill

Esta Skill guía la revisión exhaustiva de código Python, enfocándose en la detección de fallas funcionales, riesgos de ejecución y problemas de arquitectura, sin detenerse en aspectos cosméticos.

## Restricciones estrictas
1. **Solo lectura y búsqueda**:
   - Usar únicamente comandos y herramientas de lectura y búsqueda (`Read`, `Grep`, `Glob`, `view_file`, `grep_search`, `find_by_name`).
   - Está estrictamente prohibido modificar, sobrescribir o crear archivos de código durante la revisión.
2. **Ignorar formato cosmético**:
   - Descartar problemas estéticos como espaciado, longitud de líneas, comillas simples vs dobles o estilo PEP 8 que no alteren el comportamiento.

## Criterios de revisión

### 1. Errores reales de funcionamiento
- Lógica condicional invertida o defectuosa (por ejemplo, filtrar tareas completadas en lugar de pendientes).
- Fallos en tiempo de ejecución (`TypeError`, `KeyError`, `IndexError`, `AttributeError`).
- Desreferenciación de `None` (acceder a índices o atributos de objetos que pueden ser nulos).
- Valores estáticos/hardcodeados donde se requiere lógica dinámica.

### 2. Suposiciones incorrectas
- Asumir que las entradas son siempre del tipo de dato esperado sin previa validación.
- Asumir que una búsqueda o consulta siempre encontrará un elemento existente.
- Asumir que strings recibidos contienen texto significativo sin verificar espacios en blanco o valores nulos.
- Asumir inmutabilidad en estructuras mutables compartidas.

### 3. Manejo de errores faltante
- Ausencia de validaciones de límites o control ante colecciones vacías.
- Falta de retorno controlado (`None`, códigos de error o excepciones semánticas) cuando una operación falla.
- Falta de control de tipos antes de aplicar operaciones críticas.

### 4. Problemas importantes de mantenibilidad
- Mutación inadvertida de parámetros recibidos por referencia.
- Argumentos por defecto mutables en firmas de funciones.
- Acoplamiento excesivo o lógica dispersa difícil de probar de forma aislada.

## Estructura de salida recomendada
Para cada hallazgo:
- **Ubicación**: Archivo y línea de código.
- **Categoría**: Error funcional | Suposición incorrecta | Manejo de errores | Mantenibilidad.
- **Descripción**: Impacto del problema y cómo reproducirlo.
- **Sugerencia**: Explicación conceptual de cómo corregirlo.
