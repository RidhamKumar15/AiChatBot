from stt.recognizer import listen            # Speech input
from tts.speaker import speak                # Text-to-speech
from llm.chatbot import ask                  # Local LLM (Ollama)
from automation.scheduler import schedule_reminder  # Reminders
from ui.core import create_main_window

def main():
    while True:
        try:
            user_input = listen()            # Voice input
            if user_input:
                print(f"👤 You: {user_input}")
                
                # 🧠 Reminder logic
                if 'remind me' in user_input or 'set a reminder' in user_input:
                    schedule_reminder(user_input)
                else:
                    # 💬 Normal LLM chat
                    response = ask(user_input)
                    speak(response)

        except KeyboardInterrupt:
            print("\n👋 Exiting JARVIS.")
            break

if __name__ == "__main__":
    create_main_window()
    main()