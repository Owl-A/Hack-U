# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
BING_KEY = "52e9c316859948b1a61daaeefa27d899" # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
#try:
print("Microsoft Bing Voice Recognition thinks you said ::" + r.recognize_sphinx(audio))
#except sr.UnknownValueError:
#    print("Microsoft Bing Voice Recognition could not understand audio")
#except sr.RequestError as e:
#    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))