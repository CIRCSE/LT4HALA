***
<p style="text-align: center;">--<a href="index">Home</a>--&nbsp;&nbsp;--<a href="CFP">CFP</a>--&nbsp;&nbsp;--EvaLatin--&nbsp;&nbsp;--<a href="Keynote">Keynote Speaker</a>--&nbsp;&nbsp;--<a href="Program">Program</a>--&nbsp;&nbsp;--<a href="organization">Organization</a>--</p>
***

## EvaLatin

![](LOGO.png)

- [Introduction](#introduction)
- [Important Dates](#important-dates)
- [Data](#data)
  * [Training Data](#training-data)
  * [Test Data](#test-data)
- [How to participate](#how-to-participate)

___
**10/12/2019** - Training data, scorer and detailed guidelines available [here](https://github.com/CIRCSE/LT4HALA/tree/master/data_and_doc).

***

Three or more...

---

Hyphens

***

Asterisks

___

### INTRODUCTION

The workshop will also be the venue of *EvaLatin*, the first evaluation campaign totally devoted to the evaluation of NLP tools for Latin. The campaign is designed with the aim of answering two questions:
- How can we promote the development of resources and language technologies for the Latin language?
- How can we foster collaboration among scholars working on Latin and attract researchers from different disciplines?

EvaLatin first edition will have 2 tasks (i.e. Lemmatization and PoS tagging) each with 3 sub-tasks (i.e. Classical, Cross-Genre, Cross-Time). Shared data in CoNLL-U format and an evaluation script will be provided to the participants who will choose to participate in either one or all tasks and subtasks. 

We plan to have one oral session and one poster session to disseminate the results of EvaLatin.

### IMPORTANT DATES
- 10 December 2019: training data available
- Evaluation Window I - Task: Lemmatization
  - 17 February 2010: test data available
  - 21 February 2020 system results due to organizers
- Evaluation Window II - Task: PoS tagging
  - 24 February 2020: test data available
  - 28 February 2020: system results due to organizers
- 6 March 2020: assessment returned to participants
- 27 March 2020: reports due to organizers
- 10 April 2020: camera ready version of reports due to organizers
- 12 May 2020: workshop

### DATA
Training data will be distributed in the [CoNLL-U format](https://universaldependencies.org/format.html). In our dataset ID, FORM, LEMMA and UPOS fields are annotated: all the other fields are filled in with underscores.

#### Training Data
Texts provided as training data are by 5 Classical authors: Caesar, Cicero, Seneca, Pliny the Younger and Tacitus. For every one of these authors we release around 50,000 annotated tokens, for a total of almost 260,000 tokens. All the texts are in prose but of different genres: treatises in the case of Caesar, Seneca and Tacitus, public speeches for Cicero, and letters for Pliny the Younger. 

| AUTHORS           | TEXTS                     | # TOKEN |
|-------------------|---------------------------|---------|
| Caesar            | De Bello Gallico          | 44,818  |
| Caesar            | De Bello Civili (book II) | 6,389   |
| Cicero            | Philippicae (books I-XIV) | 52,563  |
| Pliny the Younger | Epistulae (books I-VIII)  | 50,827  |
| Seneca            | De Beneficiis             | 45,457  |
| Seneca            | De Clementia              | 8,172   |
| Tacito            | Historiae                 | 51,420  |

#### Test Data
Tokenisation is a central issue in evaluation and comparison because each system could apply different tokenisation rules leading to different outputs. In order to avoid this problem, test data will be provided in tokenised format, one token per line, and with a white line separating each sentence. Test data will contain only the tokenized words but not the correct tags, that have to be added by the participant systems to be submitted for the evaluation.
The gold standard test data, that is the annotation used for the evaluation, will be provided to the participants after the evaluation.

### HOW TO PARTICIPATE
Participants will be required to submit their runs and to provide a technical report that should include a brief description of their approach, focusing on the adopted algorithms, models and resources, a summary of their experiments, and an analysis of the obtained results.
  
The first run will be produced according to the *closed modality*: the only annotated data to be used for training and tuning the systems are those distributed by the organizers. Other non-annotated resources, e.g. word embeddings, are instead allowed. The second run will be produced according to the *open modality*: annotated external data, such as the Latin datasets of the Universal Dependecies initiative, can be also employed. All external resources are expected to be described in the systems' reports. The closed run is compulsory, while the open run is optional.

