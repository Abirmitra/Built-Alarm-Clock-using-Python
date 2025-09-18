
# Built Alarm Clock using Python
# First need to install pip install playsound==1.2.2 to play the sound of the alarm.
# Created a user-friendly clock with alarm sound integration using "datetime" and "playsound".
# Included error handling for invalid inputs and invalid file paths. 
from datetime import datetime
import time
from playsound import playsound  # You need to install this module

def alarm_clock(alarm_time, sound_file):
    print(f"Alarm set for {alarm_time}...")
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("Wake up! Playing alarm sound...")
            playsound(sound_file)
            break
        time.sleep(30)

if __name__ == "__main__":
    alarm_input = input("Enter the alarm time (HH:MM, 24-hour format): ")
    sound_path = input("Enter the path to your alarm sound file (e.g., alarm.mp3): ")
    alarm_clock(alarm_input, sound_path)

