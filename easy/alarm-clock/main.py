import time
import datetime
import pygame


def set_alarm(alarm_time):
    print(f"Alarm set from {alarm_time}")
    sound_file = "alarm.mp3"
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        print(current_time)

        time.sleep(1)

        if current_time == alarm_time:
            print("Wake Up!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.get_busy():
                time.sleep(1)

            pygame.mixer.music.stop()
            pygame.quit()
            is_running = False


def main():
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)


if __name__ == '__main__':
    main()
