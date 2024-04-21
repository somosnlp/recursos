<!--
Esta plantilla de Model Card es una adaptación de la de Hugging Face: https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/templates/modelcard_template.md

¿Cómo utilizar esta plantilla? Copia el contenido en el README.md del repo de tu modelo en el Hub de Hugging Face y rellena cada sección.

Para más información sobre cómo rellenar cada sección ver las docs: https://huggingface.co/docs/hub/model-cards
-->

# Model Card for < Nombre del modelo >

<!-- Suele haber un nombre corto ("pretty name") para las URLs, tablas y demás y uno largo más descriptivo. Para crear el pretty name podéis utilizar acrónimos. -->

<!-- Resumen del modelo y motivación del proyecto (inc. los ODS relacionados). Esta sección es como el abstract. -->

<!-- Si queréis incluir una versión de la Dataset Card en español, enlazarla aquí al principio (e.g. `README_es.md`).-->

## Model Details

### Model Description

<!-- Resumen del modelo. -->

- **Developed by:** [More Information Needed] <!-- Nombre de los miembros del equipo -->
- **Funded by:** SomosNLP, HuggingFace <!-- Si contasteis con apoyo de otra entidad (e.g. vuestra universidad), añadidla aquí -->
- **Model type:** Language model, instruction tuned
- **Language(s):** [More Information Needed] <!-- Enumerar las lenguas en las que se ha entrenado el modelo, especificando el país de origen. Utilizar códigos ISO. Por ejemplo: Spanish (`es-CL`, `es-ES`, `es-MX`), Catalan (`ca`), Quechua (`qu`).  -->
- **License:** apache-2.0 <!-- Elegid una licencia lo más permisiva posible teniendo en cuenta la licencia del model pre-entrenado y los datasets utilizados -->
- **Fine-tuned from model:** [More Information Needed] <!-- Enlace al modelo pre-entrenado que habéis utilizado como base -->
- **Dataset used:** [More Information Needed] <!-- Enlace al dataset utilizado para el ajuste -->

### Model Sources

- **Repository:** [More Information Needed] <!-- Enlace al `main` del repo donde tengáis los scripts, i.e.: o del mismo repo del modelo en HuggingFace o a GitHub. -->
- **Paper:** [optional] [More Information Needed] <!-- Si vais a presentarlo a NAACL poned "WIP", "Comming soon!" o similar. Si no tenéis intención de presentarlo a ninguna conferencia ni escribir un preprint, eliminar. -->
- **Demo:** [More Information Needed] <!-- Enlace a la demo -->
- **Video presentation:** [optional] [More Information Needed] <!-- Enlace a vuestro vídeo de presentación en YouTube (están todos subidos aquí: https://www.youtube.com/playlist?list=PLTA-KAy8nxaASMwEUWkkTfMaDxWBxn-8J) -->

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

[More Information Needed]

### Downstream Use [optional]

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->

[More Information Needed]

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

[More Information Needed]

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

[More Information Needed]

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

<!-- Example: Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. More information needed for further recommendations. -->

## How to Get Started with the Model

Use the code below to get started with the model.

```

[More Information Needed]

```

## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

[More Information Needed]

### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

<!-- Detallar la técnica de entrenamiento utilizada y enlazar los scripts/notebooks. -->

#### Preprocessing [optional]

[More Information Needed]

#### Training Hyperparameters

<!-- Enumerar los valores de los hiperparámetros de entrenamiento. -->

- **Training regime:** <!--fp32, fp16 mixed precision, bf16 mixed precision, bf16 non-mixed precision, fp16 non-mixed precision, fp8 mixed precision -->

#### Speeds, Sizes, Times [optional]

<!-- This section provides information about throughput, start/end time, checkpoint size if relevant, etc. -->

[More Information Needed]

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

### Testing Data, Factors & Metrics

#### Testing Data

<!-- This should link to a Dataset Card. -->

[More Information Needed]

#### Factors

<!-- These are the things the evaluation is disaggregating by, e.g., subpopulations or domains. -->

[More Information Needed]

#### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->

[More Information Needed]

### Results

<!-- Enlazar aquí los scripts/notebooks de evaluación y especificar los resultados. -->

[More Information Needed]

## Model Examination [optional]

<!-- Relevant interpretability work for the model goes here. -->

[More Information Needed]

## Environmental Impact

<!-- Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly. -->

<!-- Rellenar la información de la lista y calcular las emisiones con la página mencionada. -->

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** [More Information Needed]
- **Hours used:** [More Information Needed]
- **Cloud Provider:** [More Information Needed]
- **Compute Region:** [More Information Needed]
- **Carbon Emitted:** [More Information Needed]

## Technical Specifications [optional]

<!-- Esta sección es opcional porque seguramente ya habéis mencionado estos detalles más arriba, igualmente está bien incluirlos aquí de nuevo como bullet points a modo de resumen. -->

### Model Architecture and Objective

[More Information Needed]

### Compute Infrastructure

[More Information Needed]

#### Hardware

<!-- Indicar el hardware utilizado, podéis agradecer aquí a quien lo patrocinó. -->

[More Information Needed]

#### Software

<!-- Enumerar las librerías utilizadas (e.g. transformers, distilabel). -->

[More Information Needed]

## License

<!-- Indicar bajo qué licencia se libera el modelo explicando, si no es apache 2.0, a qué se debe la licencia más restrictiva (i.e. herencia de las licencias del modelo pre-entrenado o de los datos utilizados). -->

## Citation

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

- benallal2024cosmopedia -> nombre + año + nombre del modelo
- author: lista de miembros del equipo
- title: nombre del modelo
- year: año
- url: enlace al modelo

-->

## Glossary [optional]

<!-- If relevant, include terms and calculations in this section that can help readers understand the model or model card. -->

## More Information

<!-- Indicar aquí que el marco en el que se desarrolló el proyecto, en esta sección podéis incluir agradecimientos y más información sobre los miembros del equipo. Podéis adaptar el ejemplo a vuestro gusto. -->

This project was developed during the [Hackathon #Somos600M](https://somosnlp.org/hackathon) organized by SomosNLP. The model was trained using GPUs sponsored by HuggingFace.

**Team:** [More Information Needed]

<!--
- [Name 1](Link to Hugging Face profile)
- [Name 2](Link to Hugging Face profile)
-->

## Contact [optional]

<!-- Email de contacto para´posibles preguntas sobre el modelo. -->
