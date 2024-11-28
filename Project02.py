import speech_recognition as sr
import webbrowser
import pyttsx3
import musicofjarvis
# Dummy music dictionary for testing
## This is 
# ##

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Speaks the given text."""
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    """Processes recognized commands."""
    command = command.lower().strip()
    print(f"Recognized Command: {command}")  # Debugging output

    try:
        if "open google" in command:
            print("Opening Google...")
            webbrowser.open("https://google.com")
        elif "open facebook" in command:
            print("Opening Facebook...")
            webbrowser.open("https://facebook.com")
        elif "open chat gpt" in command:
            print("Opening ChatGPT...")
            webbrowser.open("https://chat.openai.com")
        elif "open youtube" in command:
            print("Opening YouTube...")
            webbrowser.open("https://youtube.com")
        elif "open linkedin" in command:
            print("Opening LinkedIn...")
            webbrowser.open("https://linkedin.com")
        elif command.startswith("play"):
            song = command.split(" ", 1)[1]  # Get the song name
            link = musicofjarvis.music.get(song, None)
            if link:
                print(f"Playing {song}...")
                webbrowser.open(link)
            else:
                print(f"Song '{song}' not found.")
                speak("Sorry, I couldn't find the song.")
        else:
            print("Command not recognized.")
            speak("I couldn't understand your command.")
    except Exception as e:
        print(f"Error in processing command: {e}")
        speak("There was an error processing your command.")

if __name__ == "__main__":
    speak("Hey Kaif Sir, how may I help you?")
    active = False  # Initially, assistant is inactive

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for 'Jarvis' to activate or 'stop' to deactivate...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                command = recognizer.recognize_google(audio).lower().strip()
                print(f"Recognized: {command}")

                if "jarvis" in command and not active:
                    active = True
                    speak("Yes, I am here.")
                    print("Assistant activated!")

                elif "stop" in command and active:
                    speak("Goodbye!")
                    print("Assistant deactivated!")
                    break

                elif active:
                    processCommand(command)

                else:
                    print("Waiting for activation keyword...")

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
