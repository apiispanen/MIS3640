import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
def s(speech):
    speak.Speak(speech)
speak.Speak("Hello World")
initial = input('Place command: ')
if initial == 'hello' or initial == 'I want':
    s('What do you want?')
want = input()
user_wants = {}
user_wants[want] = 1
print(user_wants)