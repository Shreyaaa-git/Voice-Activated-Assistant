import requests
# from bs4 import BeautifulSoup
import pyttsx3
import speech_recognition as sr
import datetime

import openai
openai.api_key = "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"

# function to read out the query
def speak(data):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    engine.say(data)
    engine.runAndWait()

# function to get audio from the surroundings and extract meaningful words from it
def get_audio():
    engine = pyttsx3.init()
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak:")
        # r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        voice_command = r.recognize_google(audio)
    try:
        print(f"User said: {voice_command}")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        engine.say("Sorry, I did not understand that.")
        engine.runAndWait()
        exit()
    except sr.RequestError:
        print("Sorry, I could not process your request.")
        engine.say("Sorry, I could not process your request.")
        engine.runAndWait()
    return voice_command.lower()

# function to send a prompt to the ChatGPT API
def chatgpt(user_query):
    response = openai.Completion.create(engine='text-davinci-003',
                                        prompt=user_query,
                                        n=1,
                                        temperature=0.5,
                                        max_tokens=50,
                                        top_p=1)
    return response['choices'][0]['text']

WAKE = "hello" # declaring a wakeup command for the assitant
speak("Active")

# main loop of the script
while True:
    flag = 0
    print("Active")
    texts = get_audio()

    if texts.count(WAKE) > 0:
        print("I am listening")
        speak("I am listening")
        try:
            text = get_audio()


            if 'time now' in text:
                flag = 1
                now = datetime.datetime.now()
                time_string = now.strftime("The time is %I:%M %p.")
                speak(time_string)
                print(time_string)

            if 'date today' in text:
                flag = 1
                now = datetime.datetime.now()
                date_string = now.strftime("Today's date is %B %d, %Y.")
                speak(date_string)
                print(date_string)

            if 'weather' in text:
                flag = 1
                api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(text) # weahrer API provided by the IoT team
                response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
                if response.status_code == requests.codes.ok:
                    print(response.text)

            if flag != 1:
                result = chatgpt(text)
                print(result)
                speak(result)
        except sr.UnknownValueError:
            print('Sorry, I could not catch that')
            speak('Sorry, I could not catch that')

    if 'exit' in texts:
        speak("Thank you")
        print("Thank You")
        exit()
