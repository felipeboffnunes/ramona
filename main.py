# !/usr/bin/env python3
import os
import speech_recognition as sr


def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Starting Ramona V1.0")
        while True:
            try:
                print("...")
                audio = r.listen(source, timeout=3, phrase_time_limit=5)
                print("processing")
                command = r.recognize_sphinx(audio)

                if "number" in command and "one" in command:
                    os.system("start C:\\Users\\KOR\\AppData\\Local\\slack\\slack.exe")
                else:
                    print(command)
                    print("E")
            except sr.WaitTimeoutError:
                pass
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))


if __name__ == '__main__':
    main()
