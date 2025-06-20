# automation/scheduler.py

from apscheduler.schedulers.background import BackgroundScheduler
from tts.speaker import speak, beep
import datetime
import re

scheduler = BackgroundScheduler()
scheduler.start()

def schedule_reminder(text: str):
    """
    Smarter extraction for reminders:
    Supports:
    - "Remind me in 2 minutes to stretch"
    - "Set a reminder of 3 minutes"
    - "Set a timer for 5 minutes"
    - "In 10 minutes, remind me"
    - "At 6:30 PM, remind me to check email"
    """

    import re
    import datetime

    text = text.lower()

    # Fallback message
    fallback_message = "Reminder!"

    # Extract message
    message_match = re.search(r'to (.+)', text)
    message = message_match.group(1) if message_match else fallback_message

    # Match "in X minutes/hours", "after X minutes", "of X minutes"
    time_match = re.search(r'(in|after|of|for)\s+(\d+)\s*(minute|minutes|hour|hours)', text)
    if time_match:
        amount = int(time_match.group(2))
        unit = time_match.group(3)

        delay = datetime.datetime.now()
        if 'minute' in unit:
            delay += datetime.timedelta(minutes=amount)
        elif 'hour' in unit:
            delay += datetime.timedelta(hours=amount)

        scheduler.add_job(lambda: [beep(), speak(f"⏰ Reminder: {message}")], 'date', run_date=delay)
        print(f"[Scheduled] {message} at {delay.strftime('%I:%M:%S %p')}")
        speak(f"Reminder set in {amount} {unit} to {message}")
        return

    # Match "at HH:MM [AM/PM]" format
    time_match = re.search(r'at (\d{1,2}:\d{2}) ?(am|pm)?', text)
    if time_match:
        time_str = time_match.group(1)
        meridian = time_match.group(2)

        now = datetime.datetime.now()
        try:
            hour, minute = map(int, time_str.split(':'))
            if meridian:
                if meridian.lower() == 'pm' and hour != 12:
                    hour += 12
                elif meridian.lower() == 'am' and hour == 12:
                    hour = 0
            target_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            if target_time < now:
                target_time += datetime.timedelta(days=1)

            scheduler.add_job(lambda: [beep(), speak(f"⏰ Reminder: {message}")], 'date', run_date=target_time)
            print(f"[Scheduled] {message} at {target_time.strftime('%I:%M:%S %p')}")
            speak(f"Reminder set for {target_time.strftime('%I:%M %p')} to {message}")
            return
        except Exception as e:
            print("[!] Time parsing error:", e)
            speak("Sorry, I couldn't understand the time.")
            return

    speak("Sorry, I couldn't set the reminder. Please try again.")
