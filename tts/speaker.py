# tts/speaker.py

import pyttsx3
import platform

engine = pyttsx3.init()
engine.setProperty('rate', 180)
engine.setProperty('volume', 1.0)

def speak(text: str):
    print(f"🗣️ JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def beep():
    system = platform.system()
    try:
        if system == "Windows":
            import winsound
            winsound.Beep(1000, 500)  # frequency, duration
        else:
            # Unix-based fallback (e.g., macOS/Linux)
            print('\a')
    except Exception as e:
        print(f"[!] Beep failed: {e}")
