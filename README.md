
# Built Alarm Clock using Python
# Created a user-friendly clock with alarm sound integration using "datetime" and "playsound".
# Included error handling for invalid inputs and invalid file paths.
import time
from playsound import playsound

def set_alarm(alarm_time, sound_file):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            for _ in range(3):
                playsound(sound_file)
            break
        time.sleep(1)

def main():
    print("Welcome to the Alarm Clock")
    print("Enter the time in 24-hour format (e.g., 07:00:00 for 7:00 AM)")
    alarm_time = input("Set the alarm time: ")
    sound_file = input("Enter the path to the alarm sound file (e.g., alarm.mp3): ")

    try:
        time.strptime(alarm_time, "%H:%M:%S")
        print(f"Alarm set for {alarm_time}")
        set_alarm(alarm_time, sound_file)
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS (24-hour format).")

if __name__ == "__main__":
    main()
