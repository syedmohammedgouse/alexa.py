import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import python_weather
import asyncio









listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)






def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I am already committed to internet')
    elif 'are you single' in command:
        talk('I am in a relationship with amazon')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'weather' in command:
        async def getweather():
            client = python_weather.Client(format=python_weather.IMPERIAL)
            weather = await client.find("chirala")
            print(weather.current. temperature)
            for forecast in weather.forecasts:
                print(str(forecast.date), forecast.sky_text, forecast.temperature)
                await client.close()

        if __name__ == "__main__":
            loop = asyncio.get_event_loop()
            loop.run_until_complete(getweather())

    else:
        talk('Please repeat the command again.')
        

       

while True:
    run_alexa()
 
