import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = aa.Recognizer()

machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print('listening')
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if 'Jarvis' in instruction:
                instruction = instruction.replace('Jarvis ' , ' ' )
                print(instruction)
    except:
        pass
    return instruction

def play_jarvis():
    instruction = input_instruction()
    print(instruction)
    if 'play' in instruction:
        song = instruction.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk('Current time' + time)
    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d/%m/%Y')
        talk("Today's date is " + date)
    elif 'how are you' in instruction:
        talk('I am doing well, thank you for asking! How about you?')
    elif 'what is your name' in instruction:
        talk('My name is Jarvis. Nice to meet you!')
    elif 'who is' in instruction:
        human = instruction.replace('Who is' , ' ')
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)
    elif 'what is ' in instruction:
        noun = instruction.replace('what is' , ' ')
        information = wikipedia.summary(noun, 1)
        print(information)
        talk(information)
    elif 'thank you' in instruction:
        talk('You\'re welcome! Please let me know how I can assist you further.')
    else:
        talk('Sorry I did not catch that. Could you please repeat? ')
    
    


play_jarvis()