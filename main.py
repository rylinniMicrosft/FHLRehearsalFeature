#import openai
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

# Set your OpenAI API key
# openai.api_key = 'your-api-key'

# Record audio from the user
fs = 44100  # Sample rate
seconds = 3  # Duration of recording

print("Start speaking now!")
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished

# Save as WAV file
wav.write('output.wav', fs, myrecording)  

# Use the Whisper ASR API to convert the audio to text
with open("output.wav", "rb") as f:
    data = f.read()
#response = openai.Whisper.asr(data)

# Print the transcribed text

#print(response['choices'][0]['text'])