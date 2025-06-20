import dearpygui.dearpygui as dpg
from PIL import Image
import numpy as np
import os
from ui.callbacks import toggle_listening

# Dummy callbacks (replace with real functions in your app)
dpg.add_button(
    label="Start Listening", 
    tag="btn_listen",
    callback=toggle_listening
)

def send_text_command(sender, app_data, user_data):
    print("User typed:", dpg.get_value("user_input"))

def toggle_listening():
    print("🎙️ Listening toggled")

def show_memory_window():
    print("🧠 Memory view")

def apply_theme():
    dpg.set_global_font_scale(1.1)

def load_texture(path):
    if not os.path.exists(path):
        print(f"[ERROR] Image not found: {path}")
        return None, None, None, None

    image = Image.open(path).convert("RGBA")
    image = image.transpose(Image.FLIP_TOP_BOTTOM)  # DPG expects this
    width, height = image.size
    channels = 4
    data = np.frombuffer(image.tobytes(), dtype=np.uint8).astype(np.float32) / 255.0

    return width, height, channels, data

def create_main_window():
    dpg.create_context()

    # Load logo image
    logo_path = "ui/assets/icons/logo.png"
    width, height, channels, data = load_texture(logo_path)
    if data is not None:
        with dpg.texture_registry():
            texture_id = dpg.add_static_texture(width, height, data, tag="logo_texture")

    # Main window
    with dpg.window(tag="main_window", width=1000, height=700):
        with dpg.group(horizontal=True):
            if data is not None:
                dpg.add_image_button("logo_texture", tag="btn_logo")
            dpg.add_text("JARVIS v1.0", tag="header_title")
            dpg.add_spacer(width=20)
            dpg.add_button(label="Settings", tag="btn_settings")

        with dpg.group(horizontal=True):
            with dpg.child_window(width=700):
                dpg.add_text("Conversation Log:")
                dpg.add_input_text(tag="chat_log", multiline=True, height=400, readonly=True)
                dpg.add_input_text(tag="user_input", hint="Type command or speak...", callback=send_text_command)

            with dpg.child_window(width=280):
                with dpg.group():
                    dpg.add_text("Voice Status:")
                    dpg.add_progress_bar(tag="voice_level", default_value=0.5, overlay="Listening...")

                with dpg.collapsing_header(label="Scheduled Reminders"):
                    dpg.add_listbox(tag="reminders_list", items=[], num_items=5)

                with dpg.group():
                    dpg.add_button(label="Start Listening", tag="btn_listen", callback=toggle_listening)
                    dpg.add_button(label="View Memory", callback=show_memory_window)

    apply_theme()
    dpg.create_viewport(title='JARVIS', width=1000, height=700)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

# Entry point
if __name__ == "__main__":
    create_main_window()
