<!--
Esta plantilla de Dataset Card es una adaptación de la de Hugging Face: https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/templates/datasetcard_template.md

¿Cómo utilizar esta plantilla? Copia el contenido en el README.md del repo de tu dataset en el Hub de Hugging Face y rellena cada sección.

Para más información sobre cómo rellenar cada sección ver las docs: https://huggingface.co/docs/hub/datasets-cards y https://huggingface.co/docs/datasets/dataset_card

Para más información sobre la dataset card metadata ver: https://github.com/huggingface/hub-docs/blob/main/datasetcard.md?plain=1
-->

# Dataset Card for < Nombre del corpus >

<!-- Suele haber un nombre corto ("pretty name") para las URLs, tablas y demás y uno largo más descriptivo. Para crear el pretty name podéis utilizar acrónimos. -->

<!-- Resumen del corpus y motivación del proyecto (inc. los ODS relacionados). Esta sección es como el abstract. También se puede incluir aquí el logo del proyecto. -->

<!-- Si queréis incluir una versión de la Dataset Card en español, enlazarla aquí al principio (e.g. `README_es.md`).-->

## Dataset Details

### Dataset Description

<!-- Resumen del dataset. -->

- **Curated by:** [More Information Needed] <!-- Nombre de los miembros del equipo -->
- **Funded by:** SomosNLP, HuggingFace, Argilla <!-- Si contasteis con apoyo de otra entidad (e.g. vuestra universidad), añadidla aquí -->
- **Language(s) (NLP):** [More Information Needed] <!-- Enumerar las lenguas en las que se ha entrenado el modelo, especificando el país de origen. Utilizar códigos ISO. Por ejemplo: Spanish (`es-CL`, `es-ES`, `es-MX`), Catalan (`ca`), Quechua (`qu`).  -->
- **License:** apache-2.0 <!-- Elegid una licencia lo más permisiva posible teniendo en cuenta la licencia del model pre-entrenado y los datasets utilizados -->

### Dataset Sources

- **Repository:** [More Information Needed] <!-- Enlace al `main` del repo donde tengáis los scripts, i.e.: o del mismo repo del dataset en HuggingFace o a GitHub. -->
- **Paper [optional]:** [More Information Needed] <!-- Si vais a presentarlo a NAACL poned "WIP", "Comming soon!" o similar. Si no tenéis intención de presentarlo a ninguna conferencia ni escribir un preprint, eliminar. -->
- **Demo:** [optional] [More Information Needed] <!-- Enlace a la demo del dataset -->
- **Video presentation:** [optional] [More Information Needed] <!-- Enlace a vuestro vídeo de presentación en YouTube (están todos subidos aquí: https://www.youtube.com/playlist?list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J) -->

### Dataset Versions & Formats [optional]

<!-- Si tenéis varias versiones de vuestro dataset podéis combinarlas todas en un mismo repo y simplemente enlazar aquí los commits correspondientes. Ver ejemplo de https://huggingface.co/bertin-project/bertin-roberta-base-spanish -->

<!-- Si hay varias formatos del dataset (e.g. sin anotar, pregunta/respuesta, gemma) las podéis enumerar aquí. -->

## Uses

<!-- Address questions around how the dataset is intended to be used. -->

### Direct Use

<!-- This section describes suitable use cases for the dataset. -->

[More Information Needed]

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the dataset will not work well for. -->

[More Information Needed]

## Dataset Structure

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->

<!-- En esta sección podéis enumerar y explicar cada columna del corpus. Para cada columna que sea de tipo "categoría" podéis indicar el porcentaje de ejemplos. -->

[More Information Needed]

## Dataset Creation

### Curation Rationale

<!-- Motivation for the creation of this dataset. -->

[More Information Needed]

### Source Data

<!-- This section describes the source data (e.g. news text and headlines, social media posts, translated sentences, ...). -->

#### Data Collection and Processing

<!-- This section describes the data collection and processing process such as data selection criteria, filtering and normalization methods, tools and libraries used, etc. -->

<!-- Enlazar aquí los scripts y notebooks utilizados para generar el corpus. -->

[More Information Needed]

#### Who are the source data producers?

<!-- This section describes the people or systems who originally created the data. It should also include self-reported demographic or identity information for the source data creators if this information is available. -->

[More Information Needed]

### Annotations [optional]

<!-- If the dataset contains annotations which are not part of the initial data collection, use this section to describe them. -->

#### Annotation process

<!-- This section describes the annotation process such as annotation tools used in the process, the amount of data annotated, annotation guidelines provided to the annotators, interannotator statistics, annotation validation, etc. -->

<!-- Enlazar aquí el notebook utilizado para crear el espacio de anotación de Argilla y la guía de anotación. -->

[More Information Needed]

#### Who are the annotators?

<!-- This section describes the people or systems who created the annotations. -->

[More Information Needed]

#### Personal and Sensitive Information

<!-- State whether the dataset contains data that might be considered personal, sensitive, or private (e.g., data that reveals addresses, uniquely identifiable names or aliases, racial or ethnic origins, sexual orientations, religious beliefs, political opinions, financial or health data, etc.). If efforts were made to anonymize the data, describe the anonymization process. -->

[More Information Needed]

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

<!-- Aquí podéis mencionar los posibles sesgos heredados según el origen de los datos y de las personas que lo han anotado, hablar del balance de las categorías representadas, los esfuerzos que habéis hecho para intentar mitigar sesgos y riesgos. -->

[More Information Needed]

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations.

Example:

Users should be made aware of the risks, biases and limitations of the dataset. More information needed for further recommendations. -->

[More Information Needed]

## License

<!-- Indicar bajo qué licencia se libera el dataset explicando, si no es apache 2.0, a qué se debe la licencia más restrictiva (i.e. herencia de los datos utilizados). -->

## Citation

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

[More Information Needed]

<!--

Aquí tenéis un ejemplo de cita de un dataset que podéis adaptar:

```
@software{benallal2024cosmopedia,
  author = {Ben Allal, Loubna and Lozhkov, Anton and Penedo, Guilherme and Wolf, Thomas and von Werra, Leandro},
  title = {Cosmopedia},
  month = February,
  year = 2024,
  url = {https://huggingface.co/datasets/HuggingFaceTB/cosmopedia}
}
```

- benallal2024cosmopedia -> nombre + año + nombre del dataset
- author: lista de miembros del equipo
- title: nombre del dataset
- year: año
- url: enlace al dataset

-->

## Glossary [optional]

<!-- If relevant, include terms and calculations in this section that can help readers understand the dataset or dataset card. -->

## More Information

<!-- Indicar aquí que el marco en el que se desarrolló el proyecto, en esta sección podéis incluir agradecimientos y más información sobre los miembros del equipo. Podéis adaptar el ejemplo a vuestro gusto. -->

This project was developed during the [Hackathon #Somos600M](https://somosnlp.org/hackathon) organized by SomosNLP. The dataset was created using `distilabel` by Argilla and endpoints sponsored by HuggingFace.

**Team:** [More Information Needed]

<!--
- [Name 1](Link to Hugging Face profile)
- [Name 2](Link to Hugging Face profile)
-->

## Contact [optional]

<!-- Email de contacto para´posibles preguntas sobre el dataset. -->
