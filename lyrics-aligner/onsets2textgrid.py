"""
Converts output TSV file of the aligner to Praat textgrid file
by hataori@protonmail.com
"""
import argparse
import os
from praatio import textgrid

def convert_onsets_tsv_to_textgrid(onset_file_path, grid_file_path):
    """

    Args:
        onset_file_path: file with phonemes onsets
        grid_file_path: output text grid

    Returns:
    """

    print(onset_file_path, '-->', grid_file_path)

    pointList = []
    with open(onset_file_path, 'r') as fi:
        for line in fi:
            data = line.split('\t')
            if data[0] == '>':
                data[0] = ''
            data[1] = float(data[1])
            pointList.append(data)
    pointList.append(('', pointList[len(pointList)-1][1] + 1.0))

    duration = pointList[len(pointList)-1][1]

    newEntries = []
    for i in range(len(pointList) - 1):
        newEntries.append((pointList[i][1], pointList[i + 1][1], pointList[i][0]))

    outputTG = textgrid.Textgrid()
    tier = textgrid.IntervalTier("phons", newEntries, 0, duration)
    outputTG.addTier(tier)

    outputTG.save(grid_file_path, "short_textgrid", True)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Onsets to TextGrid converter')

    parser.add_argument('file_name', type=str, help='file name without path and .txt extension')
    parser.add_argument('--dataset-name', '-D', type=str, default='cmu')
    args = parser.parse_args()

    onset_file_path = 'outputs/{}/phoneme_onsets/{}.txt'.format(args.dataset_name, args.file_name)
    grid_file_path = 'outputs/{}/phoneme_onsets/{}_TextGrid.txt'.format(args.dataset_name, args.file_name)

    convert_onsets_tsv_to_textgrid(onset_file_path, grid_file_path)

    print('done')
