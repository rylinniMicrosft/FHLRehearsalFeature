import numpy as np
import scipy.io.wavfile as wav
import sounddevice as sd
import keyboard

def get_audio_save_to_file(file_path):
    fs = 44100  # Sample rate
    
    # Start the recording in a stream
    with sd.InputStream(samplerate=fs, channels=2) as stream:
        print("Start speaking now! Press 'q' to stop recording.")
        
        frames = []
        while True:
            audio_chunk, overflowed = stream.read(fs)  # Read chunks of audio
            frames.append(audio_chunk)
            
            # Check if 'q' key is pressed
            if keyboard.is_pressed('q'):
                print("\nRecording ended!")
                break

    # Concatenate all audio chunks
    myrecording = np.concatenate(frames, axis=0)

    # Save as WAV file
    wav.write(file_path, fs, myrecording)
