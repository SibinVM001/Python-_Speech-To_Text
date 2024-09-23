import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.record(source, offset=4.7, duration=.5)

print("Google Speech Recognition thinks you said " + r.recognize_google(audio, language="de"))