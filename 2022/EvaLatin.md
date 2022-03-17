***
<p style="text-align: center;"><b>LT4HALA 2022</b></p>
<p style="text-align: center;">--<a href="index">Home</a>--&nbsp;&nbsp;--<a href="CFP">CFP</a>--&nbsp;&nbsp;--EvaLatin--&nbsp;&nbsp;--<a href="EvaHan">EvaHan</a>--&nbsp;&nbsp;--<a href="Program">Program</a>--&nbsp;&nbsp;--<a href="organization">Organization</a>--</p>
***

## EvaLatin

![](LOGO.png)

- [Introduction](#introduction)
- [Important Dates](#important-dates)
- [Data](#data)
  * [Training Data](#training-data)
  * [Test Data](#test-data)
- [Evaluation](#evaluation)
- [How to participate](#how-to-participate)

___

### INTRODUCTION

The LT4HALA 2022 workshop will also be the venue of the second edition of *EvaLatin*, the evaluation campaign totally devoted to the evaluation of NLP tools for Latin. The campaign is designed with the aim of answering two questions:
- How can we promote the development of resources and language technologies for the Latin language?
- How can we foster collaboration among scholars working on Latin and attract researchers from different disciplines?

EvaLatin 2022 edition will have 3 tasks (i.e. Lemmatization, PoS tagging, and Morphological Feature Identification) each with 3 sub-tasks (i.e. Classical, Cross-Genre, Cross-Time). These sub-tasks are designed to measure the impact of genre and diachrony on the NLP tools performances, a relevant aspect to keep in mind when dealing with the diachronic and diatopic diversity of Latin. Shared data in CoNLL-U format and an evaluation script will be provided to the participants who will choose to participate in either one or all tasks and subtasks. 

We plan to have one oral session and one poster session during the workshop at LREC 2022 to disseminate the results of EvaLatin.

EvaLatin 2022 is organized by Rachele Sprugnoli, Margherita Fantoli, Flavio M. Cecchini and Marco Passarotti.

### IMPORTANT DATES
- 20 December 2021: training data available
- Evaluation Window I - Task: Lemmatization
  - 17 March 2022: test data available
  - 23 March 2022 system results due to organizers
- Evaluation Window II - Task: PoS tagging
  - 24 March 2022: test data available
  - 30 March 2022: system results due to organizers
- Evaluation Window III - Task: Features tagging
  - 31 March 2022: test data available
  - 6 April 2022: system results due to organizers
- 26 April 2022: reports due to organizers
- 10 May 2022: short report review deadline
- 24 May 2022: camera ready version of reports due to organizers

### DATA
Data are distributed in the [CoNLL-U format](https://universaldependencies.org/format.html). In our dataset ID, FORM, LEMMA, UPOS, and FEATS fields are annotated: all the other fields are filled in with underscores.

#### Training Data
**17 March 2022 --> Download NEW training data: [EvaLatin2022-training-new.zip](https://github.com/CIRCSE/LT4HALA/blob/master/2022/data_and_doc/EvaLatin2022-training-new.zip). In the previous version of the training data some tokens were misspelled due to a bug in the script used for the conversion of the LASLA annotation into the CoNLL-U format (72 types - 1,109 tokens). Misspelled types are reported in Appendix B of the [guidelines](https://github.com/CIRCSE/LT4HALA/blob/master/2022/data_and_doc/EvaLatin_2022_guidelines-TEST.pdf) and the corresponding tokens will not be taken into consideration in the evaluation (download the new version of the [scorer](https://github.com/CIRCSE/LT4HALA/blob/master/2022/data_and_doc/conll18_ud_eval_EvaLatin_2022_rev2.py)).**

Texts provided as training data are the same adopted as training and test data in EvaLatin 2020 but the annotation can be different from the one of the previous edition of the campaign: indeed, in 2020 we did not use the LASLA corpus directly but a manually revised version of the annotations automatically made by the Perseus model of UDPiPe.

Texts are by 5 Classical authors for a total of more than 300,000 tokens: Caesar, Cicero, Seneca, Pliny the Younger and Tacitus. Each author is represented by one specific text genre: treatises in the case of Caesar, Seneca and Tacitus, public speeches for Cicero, and letters for Pliny the Younger. 

| AUTHORS           | TEXTS                           | # TOKEN |
|-------------------|---------------------------------|---------|
| Caesar            | De Bello Gallico                | 44,818  |
| Caesar            | De Bello Civili (book I and II) | 17,287  |
| Cicero            | Philippicae (books I-XIV)       | 52,563  |
| Cicero            | In Catilinam                    | 12,564  |
| Pliny the Younger | Epistulae (books I-VIII and X)  | 60,695  |
| Seneca            | De Beneficiis                   | 45,457  |
| Seneca            | De Clementia                    | 8,172   |
| Seneca            | De Vita Beata                   | 7,270   |
| Seneca            | De Providentia                  | 4,077   |
| Tacitus            | Historiae                       | 51,420  |
| Tacitus           | Agricola                        | 6,737   |
| Tacitus            | Germania                        | 5,513   |
| TOTAL             | TEXTS                           | 316,573 |

#### Test Data
**17 March 2022 --> Download test data: [EvaLatin2022-test.zip](https://github.com/CIRCSE/LT4HALA/tree/master/2022/data_and_doc/EvaLatin2022-test.zip)**

Tokenisation is a central issue in evaluation and comparison because each system could apply different tokenisation rules leading to different outputs. In order to avoid this problem, test data will be provided in tokenised format, one token per line, and with a white line separating each sentence. Test data will contain only the tokenized words but not the correct tags, that have to be added by the participant systems to be submitted for the evaluation.
The gold standard test data, that is the annotation used for the evaluation, will be provided to the participants after the evaluation.

### EVALUATION
**17 March 2022 --> A new version of the scorer is available: [conll18_ud_eval_EvaLatin_2022_rev2.py](https://github.com/CIRCSE/LT4HALA/tree/master/2022/data_and_doc/conll18_ud_eval_EvaLatin_2022_rev2.py). In this version of the scorer, tokens affected by a bug in the training set are skipped and not taken into consideration when calculating the accuracy.**

The previous version (with no skipped tokens) is also still available: [conll18_ud_eval_EvaLatin_2022.py](https://github.com/CIRCSE/LT4HALA/tree/master/2022/data_and_doc/conll18_ud_eval_EvaLatin_2022.py).

### HOW TO PARTICIPATE
Participants will be required to submit their runs and to provide a technical report that should include a brief description of their approach, focusing on the adopted algorithms, models and resources, a summary of their experiments, and an analysis of the obtained results.
  
The first run will be produced according to the *closed modality*: the only annotated data to be used for training and tuning the systems are those distributed by the organizers. Other non-annotated resources, e.g. word embeddings, are instead allowed. The second run will be produced according to the *open modality*: annotated external data, such as the Latin datasets of the Universal Dependecies initiative, can be also employed. All external resources are expected to be described in the systems' reports. The closed run is compulsory, while the open run is optional.


For detailed information, please read the guidelines:
- version 1 (training): [EvaLatin_2022_guidelines_v1.pdf](https://github.com/CIRCSE/LT4HALA/blob/master/2022/data_and_doc/EvaLatin_2022_guidelines_v1.pdf).
- **version 2 (updated on March 16): [EvaLatin_2022_guidelines-TEST.pdf](https://github.com/CIRCSE/LT4HALA/blob/master/2022/data_and_doc/EvaLatin_2022_guidelines-TEST.pdf)**

***
<p style="text-align: center;">Back to the <a href="https://circse.github.io/LT4HALA/"><b>Main Page</b></a></p>
***

