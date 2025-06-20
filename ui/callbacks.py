import threading
from stt.recognizer import listen  # Make sure this import matches your project

listening_flag = False

def listen_loop():
    global listening_flag
    while listening_flag:
        user_input = listen()  # Your speech-to-text function
        if user_input:
            # Process user_input, e.g., update UI, send to LLM, etc.
            print(f"You said: {user_input}")

def toggle_listening():
    global listening_flag
    import dearpygui.dearpygui as dpg
    if dpg.get_item_label("btn_listen") == "Start Listening":
        dpg.configure_item("btn_listen", label="Stop Listening")
        listening_flag = True
        threading.Thread(target=listen_loop, daemon=True).start()
    else:
        dpg.configure_item("btn_listen", label="Start Listening")
        listening_flag = False
