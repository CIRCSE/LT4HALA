***
<p style="text-align: center;"><b>LT4HALA 2026</b></p>
<p style="text-align: center;">--<a href="index">Home</a>--&nbsp;&nbsp;--<a href="CFP">CFP</a>--&nbsp;&nbsp;--EvaLatin--&nbsp;&nbsp;--<a href="EvaHan">EvaHan</a>--&nbsp;&nbsp;--<a href="EvaCun">EvaCun</a>--&nbsp;&nbsp;--<a href="Program">Program</a>--&nbsp;&nbsp;--<a href="organization">Organization</a>--</p>
***

## EvaLatin

![](LOGO.png)

- [Introduction](#introduction)
- [Important Dates](#important-dates)
- [Data](#data)
- [Evaluation](#evaluation)
- [How to participate](#how-to-participate)

___

### INTRODUCTION

The LT4HALA 2026 workshop will also be the venue of the forth edition of *EvaLatin*, the campaign totally devoted to the evaluation of NLP tools for Latin. The campaign is designed with the aim of answering two questions:
- How can we promote the development of resources and language technologies for the Latin language?
- How can we foster collaboration among scholars working on Latin and attract researchers from different disciplines?

EvaLatin 2026 edition will have 2 tasks, i.e. Dependency Parsing and Named Entity Recognition. 

Shared test data and an evaluation script will be provided to the participants who will choose to participate in either one or all tasks. 

### IMPORTANT DATES
- 22 December 2025: guidelines available
- Evaluation Window I - Task: Dependency Parsing
  - 3 February 2026: test data available
  - 10 February 2026: system results due to organizers
- Evaluation Window II - Task: Named Entity Recognition
  - 12 February 2026: test data available
  - 19 February 2026: system results due to organizers
- 10 March 2026: reports due to organizers
- 20 March 2026: short report review deadline
- 27 March 2026: camera ready version of reports due to organizers

### DATA

**Dependency parsing** 

The dependency parsing task is based on the [Universal Dependencies](https://universaldependencies.org) (UD) framework. No specific training set is released but participants are free to make use of any (kind of) data/resource they consider useful for the task, including the Latin treebanks already available in the UD collection. In this regard, one of the challenges of this task is to understand which treebank (or combination of treebanks) is the most suitable to deal with new test data. 

Test data will be distributed in the CoNLL-U format with gold tokenization, lemmatization, part-of-speech tagging and morphological annotation.

**Named Entity Recognition**

TBA


### EVALUATION

**Dependency parsing** 

The output .conllu file provided by the participants shall have the indications of the syntactic head and of the dependency relation in the fields 7 (HEAD) and 8 (DEPREL) respectively. We will provide an official scorer and we will evaluate dependency relations with and without subtypes separately, e.g., "advcl:abs" (_ablativus absolutus_/_ablative absolute_) and "advcl" (_adverbial clause modifier_), providing two separate rankings. However, the use of subtypes is not mandatory: participants who do not use subtypes will not be penalized but they will still be evaluated for dependency relations without subtypes.

**Named Entity Recognition**

TBA

### HOW TO PARTICIPATE
Participants will be required to submit their runs and to provide a technical report that should include a brief description of their approach, focusing on the adopted algorithms, models and resources, a summary of their experiments, and an analysis of the obtained results. Technical reports will be included in the proceedings as short papers: the maximum length is 4 pages (excluding references) and they should follow the [LREC 2026 official format](https://lrec2026.info/authors-kit/)). Reports will receive a light review (we will check for the correctness of the format, the exactness of results and ranking, and overall exposition). Reports should be submitted using the START submission page of the workshop (TBA).

Participants are allowed to use any approach (e.g. from traditional machine learning algorithms to Large Language Models) and any resource (annotated and non-annotated data, embeddings): all approaches and resources are expected to be described in the systems' reports.

***
<p style="text-align: center;">Back to the <a href="https://circse.github.io/LT4HALA/"><b>Main Page</b></a></p>
***
