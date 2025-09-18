{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6bb92fec",
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import datetime\n",
    "import time\n",
    "from playsound import playsound  # You need to install this module\n",
    "\n",
    "def alarm_clock(alarm_time, sound_file):\n",
    "    print(f\"Alarm set for {alarm_time}...\")\n",
    "    while True:\n",
    "        current_time = datetime.now().strftime(\"%H:%M\")\n",
    "        if current_time == alarm_time:\n",
    "            print(\"Wake up! Playing alarm sound...\")\n",
    "            playsound(sound_file)\n",
    "            break\n",
    "        time.sleep(30)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    alarm_input = input(\"Enter the alarm time (HH:MM, 24-hour format): \")\n",
    "    sound_path = input(\"Enter the path to your alarm sound file (e.g., alarm.mp3): \")\n",
    "    alarm_clock(alarm_input, sound_path)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b34c9659",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
