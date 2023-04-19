# Imagination-Dataset

A dataset of 100 piano music with imaginative and scenic captions

To create new numpy arrays:

1. Create 2 empty folders at the root of the project named "audio" and "numpy".
2. Add the .mp3 or .wav file into the audio folder
3. In the terminal, navigate to the project folder.
4. Run `python convert.py`. This will create a numpy array file for any audio file that has not been converted.

To add captions:

1. Add a new line in the captions/captions.csv file with phrases separated by commas.
   The order of the phrases should be as followed:
   [title], [mood/theme], [objects/people], [action], [location], [time of day], [season], [feeling], [additional #1], [additional #2]
   Try to repeat as many phrases in the existing phrases as possible.
2. Then, delete everything in the captions/dataset.json file.
3. Navigate to the captions folder. Run `python csv2json.py`.
4. Split the dataset to dataset_train.json, dataset_test.json, and dataset_val.json in a reasonable ratio.
