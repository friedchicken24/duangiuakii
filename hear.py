import soundfile as sf
import librosa
import numpy as np
from transformers import Wav2Vec2Processor, TFWav2Vec2ForCTC
import tensorflow as tf

def load_audio(file_path):
    data, sample_rate = sf.read(file_path)
    # Chuyển đổi sample rate (nếu cần)
    if sample_rate != 16000:
        data = librosa.resample(data, sample_rate, 16000)
    return data, 16000

audio_data, sample_rate = load_audio('path_to_audio_file.wav')

processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = TFWav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

input_values = processor(audio_data, return_tensors="tf", sampling_rate=16000).input_values
logits = model(input_values).logits
predicted_ids = tf.argmax(logits, axis=-1)

transcription = processor.batch_decode(predicted_ids)[0]
print(transcription)
