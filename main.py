import openai
# import whisper
import numpy as np
import os

import json
import htmlCreater
import audio_manager

# Set your OpenAI API key
openai.api_key = ''

audio_manager.get_audio_save_to_file("output.wav")

audio_file = open("output.wav", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

rehersal_text = transcript["text"]
with open('myfile.txt', 'w') as f:
    f.write(rehersal_text)



slides = rehersal_text.lower().split("next slide")
slides = [slide.strip() for slide in slides]
print(slides)


# EXAMPLE
##################
# slides = ["Greetings, everyone. I appreciate your presence today. I’m here to talk to you about a new business possibility that I think you will be curious about. It’s called BizBee, and it’s a platform that connects small businesses with customers and suppliers in a fast and easy way.",
# "So, what is BizBee precisely? Well, it’s a website and an app that allows small businesses to create their own online profiles, showcase their products and services, and find new customers and suppliers in their area or across the country. BizBee also provides tools for managing orders, payments, inventory, and delivery.",
# "Why should you invest in BizBee? Because it’s a huge market with a lot of potential. According to some statistics, there are over 30 million small businesses in the US alone, and they generate more than $1.5 trillion in annual revenue. However, only 64 percent of them have a website, and only 36 percent use e-commerce platforms. That means there is a lot of room for growth and innovation in this sector."
# ]

slides[0] = """the following is a powerpoint transcription of a single slide. your job is to ask questions and add comments corresponding to slides when clarification is warranted in the hope that you will help the presenter avoid misunderstandings. what is provided is only the dialog not the slides themselves. 
key: focus on possible unclear phrasings or wording
tagert audience: business
 The transcription of the presentation slide is here:
 """ + slides[0]

slideResponses = []
for i, slide in enumerate(slides):
    slideResponse = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": """You are presentation and speech analyzer that only responds this json format that gives question to the speeker to help improve clarification: {"Slide": {"Question": ""}} """
         },
        {"role": "user", "content": slides[i]},
        {"role": "assistant", "content": "123"}
        ]
    )
    slideResponses.append(slideResponse)

questions =[]
with open('response.txt', 'w') as fr:
    for i, sr in enumerate(slideResponses):
        slideResult = json.loads(sr['choices'][0]['message']['content'])
        print(slideResult["Slide"]["Question"])
        questions.append('Slide '+ str(i+1) + ": " +slideResult["Slide"]["Question"])       
        fr.write(sr['choices'][0]['message']['content'])




htmlCreater.createSummary(questions)
