import win32com.client as wincom



speak = wincom.Dispatch("SAPI.SpVoice")

text =input("Enter text to speak")
speak.Speak(text)
