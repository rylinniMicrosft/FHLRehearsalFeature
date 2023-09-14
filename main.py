import openai
import whisper
import numpy as np
import os

import audio_manager

# Set your OpenAI API key
openai.api_key = os.environ.get('OPEN_API_KEY')

audio_manager.get_audio_save_to_file("output.wav")

audio_file = open("output.wav", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

rehersal_text = transcript["text"]
with open('myfile.txt', 'w') as f:
    f.write(rehersal_text)

slides = rehersal_text.lower().split("next slide")
slides = [slide.strip() for slide in slides]
print(slides)

prompt = """the following is a powerpoint transcription. your job is to ask question and add comments corresponding to slides when clarification is warranted in the hope that you will help the presenter avoid misunderstandings. what is provided is only the dialog not the slides themselves. 
focus on possible unclear phrasings or wording
tagert audience: business \n The transcription of the presentation is here: """ + rehersal_text

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an expert at analyzing presentations and speeches."},
        {"role": "user", "content": prompt},
    ]
)

print(response['choices'][0]['message']['content'])