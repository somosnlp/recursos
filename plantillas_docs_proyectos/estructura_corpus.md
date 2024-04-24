# Estructura Corpus

## Columnas que incluir

Por ser corpus de instrucciones debe tener las siguientes columnas:

- `pregunta`
- `respuesta`

Además, dado el enfoque en las variedades de la lengua del hackathon, también incluimos las siguientes columnas:

- `idioma` (variedad geográfica): código ISO del idioma ("catalán" = `ca`, "quechua" = `qu`), en caso de ser español hay que especificar la variedad geográfica ("español de México" = `es_MX`, "español de Ecuador" = `es_EC`).
- `registro` (variedad funcional): `coloquial`, `medio` o `culto`
- `periodo` (variedad histórica): si es un corpus en español elegid entre `actual`, `moderno` (ss. XVIII-XIX), `clásico` (ss. XVI-XVII) o `medieval`, si es en otro idioma rellenar si tenéis conocimiento.

Para completar la información de los ejemplos incluiremos también:

- `dominio`: `legal`, `salud` (clínico, biomédico, farmacia), `literatura` (poesía, música, teatro), `sociales` (historia, geografía, etc), `exactas` (física, mates, etc), `prensa`, `gastronomia`, `filosofia` (ética, lógica, etc), `seguros`, ..., `general` (última opción). Si puedes, especifica el subdominio, e.g. `literatura_poesia`, `sociales_historia`.
- `tarea`: `pregunta`, `clasificacion`, `traduccion`, `resumen`, `similitud_semantica`. Si puedes, especifica también la subtarea, e.g. `pregunta_abierta`, `pregunta_opcion_multiple`.
- `país_origen`: código ISO del país de origen de los datos. En general, coincide con la variedad geográfica. Si por ejemplo sabes la zona concreta del país, indícalo también (e.g. `ES (Galicia)`).
- `país_referencia`: código ISO del país al que hace referencia el texto, si aplica.

Otras consideraciones:

- Si anotáis manual o sintéticamente una base de datos ya existente, incluid en la nueva versión toda la información disponible en la primera (no eliminéis columnas).
- Si tomáis información de internet o documentos de texto, incluid una columna `origen` con el enlace a la web o al documento como referencia.
- Si el ejemplo ha sido generado sintéticamente, incluid columnas `prompt` y `modelo` con el prompt y modelo utilizados.

## Aclaraciones sobre la información de los países

- La variedad geográfica y el país de origen de los datos suele coincidir, si habéis tomado los datos de una web ".es" seguramente la variedad sea `es_ES`, si es una ley peruana será `es_PE`, si son datos de una red social paraguaya será `es_PY`. Si el corpus ha sido anotado a mano, la variedad geográfica coincide con el país de origen de la persona anotadora.
- El país de referencia no tiene nada que ver con la variedad de la lengua. Ejemplos:
  - "Decime tres platos típicos de Cuba", `pais_origen: AR/UY, pais_referencia: CU`
  - "¿Cómo le dicen a la micro en Bolivia?", `pais_origen: CL, pais_referencia: BO`
  - "Decime cuáles son los vinos más típicos de Mendoza", `pais_origen: AR, pais_referencia: AR`
  - "Según la ley colombiana, ¿qué pasa si...?", `pais_referencia: CO`
  - "¿Cómo diría un boricua que ...?", `pais_referencia: PR`

## Colaboración y preguntas

Esta guía está en desarrollo, las sugerencias y comentarios son más que bienvenidas. A vuestra disposición en Discord :)
