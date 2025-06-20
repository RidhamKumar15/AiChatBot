# stt/recognizer.py
import sounddevice as sd
import queue
import vosk
import json

q = queue.Queue()

model = vosk.Model("model")  # Put your Vosk model folder in the project root

def callback(indata, frames, time, status):
    if status:
        print("SoundDevice Status:", status)
    q.put(bytes(indata))

def listen() -> str:
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("🎤 Listening...")
        rec = vosk.KaldiRecognizer(model, 16000)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                return result.get("text", "")
