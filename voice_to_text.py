import speech_recognition as sr

def main():
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Use the microphone as source for input
    with sr.Microphone() as source:
        print("Adjusting for ambient noise. Please wait...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        
        # Capture the audio
        audio = recognizer.listen(source)

        print("Recognizing...")
        try:
            # Using Google Web Speech API for recognition
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")

if __name__ == "__main__":
    main()
