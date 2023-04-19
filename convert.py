import os
import librosa
import numpy as np

audio_dir = "audio_chosic"
numpy_dir = "numpy_chosic"
for audio_file in os.listdir(audio_dir):
    audio_path = os.path.join(audio_dir, audio_file)
    print(audio_path)
    array_path = audio_path.replace("audio", "numpy").replace("mp3", "npy").replace("wav", "npy")
    if not os.path.exists(array_path):
        audio, sr = librosa.load(audio_path, 16000)
        np.save(open(array_path, 'wb'), audio)