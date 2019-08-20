import pyttsx3
import configparser
import os
from datetime import *
import wolframalpha


# Config Set-up
config = configparser.ConfigParser()
config.read('config.int')
#######################################
api_id = config.get('jarvis', 'api_id')
g_key = config.get('jarvis', 'g_key')
prefix = config.get('jarvis', 'prefix')
name = config.get('jarvis', 'name')

wolf = wolframalpha.Client(api_id)

# Voice Setup
engine = pyttsx3.init('sapi5')
voices: object = engine.getProperty('voices')

# noinspection PyTypeChecker
engine.setProperty('voices', voices[len(voices)-1].id)


def speak(audio):
    print('JARVIS: ' + audio)
    engine.say(audio)
    engine.runAndWait()


today = datetime.now()
speak(f"Hello {prefix} {name}, I am Jarvis. Your AI assistant in Python.")
speak('Today is ' + today.strftime("%A, %B %d, %Y"))
speak('The Time is ' + today.strftime('%I:%M %p'))
speak("How may I help?")


if __name__ == '__main__':
    while True:

        response = input("Input: ").lower()

        # TODO Add Pizzapy stuff.

        if 'pizza' and 'order' in response:
            os.system("python pizza.py")

        elif 'pizza' and 'order' in response and os.system("python pizza.py") == False:
            speak('The Pizza App has not been installed')
            break

        # TODO Add Voice Rec

        # Time
        if 'what' and 'time is it' in response:
            today = datetime.now()
            speak('The time is ' + today.strftime('%I:%M %p'))

        if 'what' and 'day is it' or 'what' and 'today' in response:
            today = datetime.now()
            speak('Today is ' + today.strftime("%A, %B %d, %Y"))


        if 'who' and 'you' in response or 'what' and 'you' in response:

            speak('My name is Jarvis.')
            speak('I am a AI assistant created by Tony Stark to help him with his tasks.')
            speak('Now a days, I help you with what ever you need.')

        if 'tony' in response and 'stark' in response or 'stark' in response:

            speak('The information you requested has been denied.')

        if 'my name is' in response:

            new_name = response.replace("my name is ", "").capitalize()

            # Checks for Prefix set
            res = wolf.query('what gender is for the name ' + new_name)
            results = next(res.results).text

            if results == 'male':
                config.set('jarvis', 'prefix', 'Sir')
                prefix = config.get('jarvis', 'prefix')
            if results == 'female':
                config.set('jarvis', 'prefix', 'Miss')
                prefix = config.get('jarvis', 'prefix')

            config.set('jarvis', 'name', new_name.capitalize())
            name = config.get('jarvis', 'name')

            with open('config.int', 'w') as configfile:
                config.write(configfile)

            speak(f'Ok {prefix}, I have set your name to {name}')

        # Uses Wolfram-Alpha to look up any un-programmed questions.
        elif 'you' not in response and api_id != "":
            try:

                res = wolf.query(response)
                results = next(res.results).text

                speak(f'The answer is {results}')

            finally:

                # result = wikipedia.summary(response, sentences=2)
                speak('I can\'t seem to find an answer to that question')
        else:
            speak(f'I\'m Sorry {prefix}')
            speak('Seems as though you forgot to implement the API key that is needed for me to Research.')
            speak('Please get the API key and I\'ll be able to search the web.')
            speak('The API key is for "Wolfram-Alpha". Create a free account and add a API.')

        speak(f'Is there anything else you would like {prefix}?')
