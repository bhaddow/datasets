---
annotations_creators:
- expert-generated
language:
- en
- es
- fr
- ru
- pt
- ro
- nl
- it
- de
language_creators:
- found
license:
- cc-by-nc-nd-4.0
multilinguality:
- translation
pretty_name: A Multilingual speech translation corpus.
size_categories:
- 100K<n<1M
source_datasets:
- original
tags: []
task_categories:
- translation
- automatic-speech-recognition
task_ids: []
---

# Dataset Card for MuST-C v1.0

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:  https://ict.fbk.eu/must-c/**
- **Repository: n/a**
- **Paper: https://doi.org/10.1016/j.csl.2020.101155**
- **Leaderboard: n/a**
- **Point of Contact: Barry Haddow (bhaddow@ed.ac.uk), for the datasets integration. See the paper for the authors of the dataset.**

### Dataset Summary

MuST-C is a multilingual speech translation corpus whose size and quality facilitates the training of end-to-end systems for speech translation from English into several languages. For each target language, MuST-C comprises several hundred hours of audio recordings from English TED Talks, which are automatically aligned at the sentence level with their manual transcriptions and translations.

### Supported Tasks and Leaderboards

MuST-C has been used in several recent IWSLT shared tasks

### Languages

English audio, translated into Dutch, French, German, Italian, Portugese,  Romanian, Russian and Spanish. 

## Dataset Structure

The data set consists of TED talks, and their translations into the target language.

### Data Instances

The number of instances can be found in the `dataset_infos.json` file.

### Data Fields

Each instances contains the following foelds:
- `audio` : An array containing the audio data.
- `transcript` : The transcription in the target language (English)
- `translation` : The translation into the target language
- `doc_id` : The identifier of the TED talk
- `offset` : The offset of the audio in the talk (in seconds)
- `duraction` : The length of the audio (in seconds)
- `speaker_id` : An identifier for the speaker 

### Data Splits

There are three splits in the data: `train`, `dev` and `test`. The last coresponds to `tst-COMMON` in the released data set.

## Dataset Creation

### Curation Rationale

The data was gathered from TED talks, whenever they could be aligned with translated captions.

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@bhaddow](https://github.com/bhaddow) for adding this dataset.
