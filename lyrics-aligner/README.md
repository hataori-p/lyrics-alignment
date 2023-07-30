# Additional files for [schufo/lyrics-aligner](https://github.com/schufo/lyrics-aligner)
* aligner.yml - for installation via Conda environment
* onsets2textgrid.py - converts result of lyrics-aligner to Praat's TextGrid format
* cmu_word2phonemes.pickle - preprocessed CMU dictionary (copy to lyrics-aligner/files directory)

# Installation
* install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (takes less space) or [Anaconda](https://docs.anaconda.com/free/anaconda/install/index.html), there are also videos on YT, eg. [How to Install Miniconda](https://youtu.be/oHHbsMfyNR4)
* run Miniconda or Anaconda Prompt on your system
* change to a directory where you want to install the lyrics-aligner `cd C:\apps`
* if you have git, do this: `git clone https://github.com/schufo/lyrics-aligner.git`
* or you can [install git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for your system first
* or you can directly [download the repo](https://github.com/schufo/lyrics-aligner/archive/refs/heads/main.zip) and extract the folder with zip
* change to the repo directory `cd lyrics-aligner` or `cd lyrics-aligner-main`
* download following files:
* (if you don't have wget, download with your browser or however you want)
* `wget https://github.com/hataori-p/lyrics-alignment/raw/main/lyrics-aligner/aligner.yml`
* `wget https://github.com/hataori-p/lyrics-alignment/raw/main/lyrics-aligner/onsets2textgrid.py`
* `wget -P files https://github.com/hataori-p/lyrics-alignment/raw/main/lyrics-aligner/cmu_word2phonemes.pickle`
* make following directories `md audio lyrics`

## Install conda environment from yml file
```
conda env create -f aligner.yml -y
activate aligner
```

... or if it doesn't work, try this:

## Install conda environment (CPU only for easier installation)
```
conda create -n aligner python=3.10 numba
activate aligner
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 cpuonly -c pytorch
pip install pyqt5 decorator ffmpeg audioread resampy librosa pysoundfile praatio argparse
```
# Using the aligner
Place your wav files (eg. voice.wav) in the audio dir and corresponding lyrics (eg. voice.txt) files to the lyrics dir.
```
python align.py audio lyrics --lyrics-format w --onsets p --dataset-name cmu --vad-threshold 0
python onsets2textgrid.py lead
```
**If you run these commands again, first delete everything in the outputs directory!**

`del /S /Q outputs\*.txt`
