# Copyright 2020 The HuggingFace Datasets Authors and the current dataset script contributor.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# TODO: Address all TODOs and remove all explanatory comments
"""MuST-C direct speech translation dataset, derived from TED talks"""


import csv
import json
import librosa
import os
import sys
import yaml

from pathlib import Path

import datasets
from datasets.tasks import AutomaticSpeechRecognition



_CITATION = """\
@inproceedings{di_gangi_must-c_2019,
	address = {Minneapolis, Minnesota},
	title = {{MuST}-{C}: a {Multilingual} {Speech} {Translation} {Corpus}},
	url = {https://www.aclweb.org/anthology/N19-1202},
	doi = {10.18653/v1/N19-1202},
	abstract = {Current research on spoken language translation (SLT) has to confront with the scarcity of sizeable and publicly available training corpora. This problem hinders the adoption of neural end-to-end approaches, which represent the state of the art in the two parent tasks of SLT: automatic speech recognition and machine translation. To fill this gap, we created MuST-C, a multilingual speech translation corpus whose size and quality will facilitate the training of end-to-end systems for SLT from English into 8 languages. For each target language, MuST-C comprises at least 385 hours of audio recordings from English TED Talks, which are automatically aligned at the sentence level with their manual transcriptions and translations. Together with a description of the corpus creation methodology (scalable to add new data and cover new languages), we provide an empirical verification of its quality and SLT results computed with a state-of-the-art approach on each language direction.},
	booktitle = {Proceedings of the 2019 {Conference} of the {North} {American} {Chapter} of the {Association} for {Computational} {Linguistics}: {Human} {Language} {Technologies}, {Volume} 1 ({Long} and {Short} {Papers})},
	publisher = {Association for Computational Linguistics},
	author = {Di Gangi, Mattia A. and Cattoni, Roldano and Bentivogli, Luisa and Negri, Matteo and Turchi, Marco},
}
"""


_DESCRIPTION = """\
 MuST-C is a multilingual speech transla-
tion corpus whose size and quality will facili-
tate the training of end-to-end systems for SLT
from English into 8 languages. 

TODO: complete this
"""

# TODO: Add a link to an official homepage for the dataset here
_HOMEPAGE = ""

# TODO: Add the licence for the dataset here if you can find it
_LICENSE = ""

_LANGUAGES = ("de", "es", "fr", "it" , "nl",  "pt", "ro", "ru")

_SRC = "en"


class MustCConfig(datasets.BuilderConfig):
    """BuilderConfig for MuST-C"""

    def __init__(self, language=None, **kwargs):
        """
        Args:
          data_dir: `string`, the path to the folder containing the files in the
            downloaded .tar
          citation: `string`, citation for the data set
          url: `string`, url for information about the data set
          **kwargs: keyword arguments forwarded to super.
        """
        name = f"{language}"
        assert language in _LANGUAGES, f"Invalid language code: {language}"
        super(MustCConfig, self).__init__(version=datasets.Version("2.3.3", ""), name=name, **kwargs)

        self.language = language


# TODO: Name of the dataset usually match the script name with CamelCase instead of snake_case
class MustC(datasets.GeneratorBasedBuilder):
    """MustC dataset"""

    BUILDER_CONFIG_CLASS = MustCConfig

    BUILDER_CONFIGS = [MustCConfig(language = language) for language in _LANGUAGES]

    @property
    def manual_download_instructions(self):
        return (
            "To use MuST-C you must download it manually."
            "Then load the dataset with: "
            "`datasets.load_dataset('mustc', data_dir='path/to/foldername'" 
        )


    def _info(self):
        features = datasets.Features(
            {
                "duration": datasets.Value("float"),
                "offset" : datasets.Value("float"),
                "speaker_id": datasets.Value("string"),
                "doc_id" : datasets.Value("string"),
                "audio" : datasets.Audio(sampling_rate=16_000),
                "transcript" : datasets.Value("string"),
                "translation" : datasets.Value("string"),
            }
        )
        return datasets.DatasetInfo(
            # This is the description that will appear on the datasets page.
            description=_DESCRIPTION,
            # This defines the different columns of the dataset and their types
            features=features,  # Here we define them above because they are different between the two configurations
            # If there's a common (input, target) tuple from the features, uncomment supervised_keys line below and
            # specify them. They'll be used if as_supervised=True in builder.as_dataset.
            # supervised_keys=("sentence", "label"),
            # Homepage of the dataset for documentation
            homepage=_HOMEPAGE,
            # License for the dataset if available
            license=_LICENSE,
            # Citation for the dataset
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):

        
        language = self.config.language
        data_dir = Path(dl_manager.manual_dir) / f"{_SRC}-{language}"

        if not os.path.exists(data_dir):
            raise FileNotFoundError(
                f"""{data_dir} does not exist. Make sure you insert a 
                manual dir via `datasets.load_dataset('timit_asr', data_dir=...)` that 
                includes the dowloaded dataset. See
                 {self.manual_download_instructions}"""
            )

        return [
            #datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"split": "train", "data_dir": data_dir}),
            datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={"language" : language, "split": "dev", "data_dir": data_dir}),
            datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"language" : language, "split": "tst-COMMON", "data_dir": data_dir}),
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"language" : language, "split": "train", "data_dir": data_dir}),
        ]
        


    def _generate_examples(self,  language, split, data_dir):
        audio_segments = yaml.load(open(data_dir / "data" / split / "txt" / f"{split}.yaml"), Loader=yaml.BaseLoader)
        sources = open(data_dir / "data" / split / "txt" / f"{split}.{_SRC}").readlines()
        targets = open(data_dir / "data" / split / "txt" / f"{split}.{language}").readlines()


        for key, (source,target,audio_segment) in enumerate(zip(sources,targets,audio_segments)):
            #if key >= 1: break
            
            
            filename = (data_dir / "data" / split / "wav" / audio_segment["wav"]).as_posix()
            audio_bytes, sampling_rate = librosa.load(
                filename,
                duration = float(audio_segment['duration']),
                offset = float(audio_segment['offset']),
                mono = True,
                sr = 16000  )
            
            
            #print(audio_bytes)


            example = {
                "duration" : audio_segment["duration"],
                "offset" : audio_segment["offset"],
                "speaker_id" : audio_segment["speaker_id"],
                "doc_id" : audio_segment["wav"],
                "audio" : {
                    "array" : audio_bytes,
                    "path" : audio_segment["wav"],
                    "sampling_rate" : sampling_rate,
                },
                "transcript" : source.strip(),
                "translation" : target.strip(),
            }

            yield key,example
