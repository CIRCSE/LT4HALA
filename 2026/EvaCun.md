***
<p style="text-align: center;"><b>LT4HALA 2026</b></p>
<p style="text-align: center;">--<a href="index">Home</a>--&nbsp;&nbsp;--<a href="CFP">CFP</a>--&nbsp;&nbsp;--<a href="EvaLatin">EvaLatin</a>--&nbsp;&nbsp;--<a href="EvaHan">EvaHan</a>--&nbsp;&nbsp;--EvaCun--&nbsp;&nbsp;--<a href="Program">Program</a>--&nbsp;&nbsp;--<a href="organization">Organization</a>--</p>
***

![](logo-EvaCun.png)

## EvaCun 2026

- **EvaCun 2026** is an evaluation campaign on **cuneiform language technologies**, focusing on automatic processing of cuneiform texts (in transliteration) for ancient Mesopotamian languages (e.g. Sumerian and Akkadian).  
- It is part of **LT4HALA 2026**, co-organized with **LREC 2026**, which will be held from **May 11 to 16, 2026**, in **Mallorca, Spain**.  
- EvaCun 2026 will provide shared tasks on **transliteration normalization**, **morphological analysis and lemmatization**, and **named entity recognition** on scholarly cuneiform corpora.

- [Introduction](#introduction)
- [Important Dates](#important-dates)
- [Data](#data)
- [Evaluation](#evaluation)
- [How to participate](#how-to-participate)

___

### INTRODUCTION

The **EvaCun 2026** shared task aims to bring together researchers from **computational linguistics**, **Assyriology**, **digital humanities**, and **NLP for low-resource and historical languages** to evaluate and compare systems for automatic processing of cuneiform texts.

Cuneiform sources pose a number of unique challenges:

- multiple languages, dialects, and orthographic conventions;  
- line-based, tablet-oriented textual organization;  
- rich morphological systems and complex onomastics (names of people, places, deities, institutions);  
- heterogeneous scholarly conventions for transliteration and normalization.

EvaCun 2026 focuses on **machine-readable transliterations**, with the goal of supporting downstream tasks such as search, corpus linguistics, and knowledge graph construction. The shared task is planned to include the following subtasks (final task definitions will be announced in the CFP and evaluation guidelines):

- **Task 1 – Transliteration Normalization**  
  Mapping variant scholarly transliterations to a consistent normalized form (e.g. standard sign/word segmentation and orthographic conventions).

- **Task 2 – Morphological Analysis and Lemmatization**  
  Given segmented transliteration, automatically assigning **lemmas** and **morpho-syntactic features** to tokens.

- **Task 3 – Named Entity Recognition (NER)**  
  Identifying and classifying **named entities** (e.g. persons, places, gods, institutions) in transliterations, with optional linking to reference identifiers when available.

The shared task is open to a wide range of methods, from traditional sequence labeling models to modern **transformer-based** and **multimodal** architectures.

---

### IMPORTANT DATES

The schedule for **EvaCun 2026** follows the same timeline as the other LT4HALA 2026 evaluation campaigns:

- **Registration deadline:** January 30, 2026  
- **Training data release:** January 1, 2026  
- **Test data release:** February 1, 2026  
- **Running results submission:** February 6, 2026  
- **Technical report submission deadline:** February 28, 2026  
- **Notification of acceptance:** March 1, 2026  
- **Camera-ready posters due:** March 10, 2026  

(Registration is planned to open **December 1, 2025**.)

---

### DATA

The **EvaCun 2026** dataset will consist of expert-curated **cuneiform transliterations** drawn from established scholarly corpora and digital editions. All texts are provided in a unified encoding and split into **training**, **development**, and **test** partitions.

**Training data (released January 1, 2026):**
- [Zenodo record 10794626](https://zenodo.org/records/10794626)
- [Zenodo record 17220688](https://zenodo.org/records/17220688)

Planned characteristics of the dataset include:

- **Languages and Periods**  
  - Focus on major cuneiform languages (e.g. Akkadian and/or Sumerian).  
  - Texts from different periods and genres (e.g. letters, administrative records, legal documents, royal inscriptions).

- **Format and Annotation**  
  - Line-based transliterations in UTF-8, with consistent conventions for sign and word boundaries.  
  - For Task 1, parallel **raw** versus **normalized** transliterations.  
  - For Task 2, tokens annotated with **lemmas** and **morphological tags** (e.g. POS, case, number, gender, verbal features) for the training and development sets.  
  - For Task 3, entities annotated with **entity types** (e.g. PER, LOC, ORG, DEITY, etc.); some entities may additionally include links to stable identifiers in external prosopographical or gazetteer resources where available.

- **Splits**  
  - **Training set:** released with full annotations for all relevant tasks.  
  - **Development set:** released with gold annotations for system tuning and error analysis.  
  - **Test set:** released **without** gold labels; only the organizers will have access to the gold annotations used for the official evaluation.

- **Licensing and Use**  
  - All data will be released under a license suitable for research use.  
  - Participants must agree not to redistribute the test data or gold labels and to respect any usage restrictions specified in the data release agreement.

More detailed documentation on the sources, annotation guidelines, and file formats will be provided with the **training data release**.

---

### EVALUATION

Systems submitted to **EvaCun 2026** will be evaluated using standard metrics for sequence labeling and classification tasks. The exact metrics and scoring scripts will be distributed together with the test data.

Planned evaluation protocol (subject to refinement in the official guidelines):

- **Task 1 – Transliteration Normalization**  
  - Primary metrics: **token-level accuracy** and **character-level F1** between system output and normalized gold standard.  
  - Secondary analyses may include error breakdown by sign type, word class, or text genre.

- **Task 2 – Morphological Analysis and Lemmatization**  
  - Lemmatization: **lemma accuracy** at token level.  
  - Morphological tagging: **macro-averaged F1** and **overall accuracy** for morpho-syntactic feature bundles.  
  - Joint scoring (lemma + morphology correct) may be reported as an additional measure.

- **Task 3 – Named Entity Recognition (NER)**  
  - Span-based evaluation with **precision**, **recall**, and **F1** at the entity level.  
  - Evaluation will follow standard NER conventions (e.g. exact match of entity boundaries and type).  
  - If linking is included, link correctness may be evaluated separately or as an optional sub-metric.

**Submission format**

- Participants will submit their predictions in standardized text or JSON formats specified in the evaluation guidelines (e.g. one file per subtask, mirroring the structure of the provided test files).  
- Each team may submit multiple **runs** (e.g. primary and contrastive systems); the number and type of runs will be described in the call for participation.  
- An official **evaluation script** will be released to allow participants to compute scores locally on the development set.

Results will be summarized in the **LT4HALA 2026 overview paper** and in the **EvaCun 2026 shared task report**, and participants will be invited to contribute **technical reports** describing their systems and findings.

---

### HOW TO PARTICIPATE

To participate in **EvaCun 2026**, please follow these steps:

1. **Registration**  
   - Complete the EvaCun registration form (link to be announced on the LT4HALA main page).  
   - Registration is open from **December 1, 2025** until **January 30, 2026**.  
   - Only **registered teams** will receive access credentials for the training and test data.

2. **Sign the Data and Participation Agreement**  
   - After registering, participants will receive the data usage and participation terms.  
   - Teams must confirm that they accept the conditions before downloading the training data and before accessing the test set.

3. **Access the Training Data and Baselines**  
   - Once registration is confirmed, instructions will be sent for downloading:  
     - the **training and development data**,  
     - documentation on file formats and annotation schemes,  
     - and any available **baseline systems or scripts** to facilitate participation.

4. **Develop and Run Your System**  
   - Use the training and development sets to design, train, and tune your systems for one or more EvaCun tasks.  
   - Participants are free to use external resources (pretrained models, additional corpora, lexica, etc.) as long as they comply with the evaluation rules (e.g. no manual use of the test set).

5. **Submit System Outputs and Technical Report**  
   - Generate predictions for the **official test data** and submit your system outputs by **February 6, 2026**.  
   - Prepare a short **technical report** describing your methods, resources, and results, and submit it by **February 28, 2026**.  
   - Notifications of acceptance will be sent on **March 1, 2026**, and **camera-ready** versions will be due on **March 10, 2026**.

6. **Present at LT4HALA / LREC 2026**  
   - Accepted system description papers will be presented at the LT4HALA workshop co-located with **LREC 2026 in Mallorca, Spain**.  
   - At least one author of each accepted paper is expected to register for the workshop and present the work.

For inquiries about EvaCun 2026, including questions about registration, data access, and task definitions, please contact:  
**[admin@tokenworks.ai](mailto:admin@tokenworks.ai)**

***

<p style="text-align: center;">Back to the <a href="https://circse.github.io/LT4HALA/"><b>Main Page</b></a></p>

***
