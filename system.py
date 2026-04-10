import os
import pyttsx3
import time
import speech_recognition

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 160)
engine.setProperty("volume", 0.5)

def say(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except:
        print("Sorry!😮 There is a problem")

def listen():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry!😮 I didn't catch that. Please say that again.")
        return "None"
    return query

def main():
    print("please choice the following options: \n1. shutdown \n2. Restart \n3. sleep")
    choice = input("Enter your choice: ")
    match choice:
        case '1':
            minter = int(input("Enter your minuters: "))
            diple = minter * 60
            say(f"The system is shut down in {minter} minutes .")
            try:
                time.sleep(diple)
                os.system("shutdown /s /t 1")
            except Exception as e:
                print(f"Error occurred while shutting down: {e}")
        case '2':
            minter = int(input("Enter your minuters: "))
            diple = minter * 60
            say(f"The system will restart in {minter} minutes .")
            try:
                time.sleep(diple)
                os.system("shutdown /r /t 1")
            except Exception as e:
                print(f"Error occurred while restarting: {e}")
        case '3':
            minter = int(input("Enter your minuters: "))
            diple = minter * 60
            say(f"The system will sleep in {minter} minutes .")
            try:
                time.sleep(diple)
                os.system("shutdown /h /t 1")
            except Exception as e:
                print(f"Error occurred while putting system to sleep: {e}")
        case _:
            print("Invalid input")

def file_manager():
    print("1. Create a file\n2. Delete a file\n3. Exit")
    choice = input("Enter your choice: ")
    match choice:
        case '1':
            filename = input("Enter the file name: ")
            path = input("Enter the file path: ")
            try:
                full_path = os.path.join(path, filename)
                with open(full_path, "w") as f:
                    f.write("")
                print(f"{filename} created successfully.")
                say(f"{filename} created successfully.")
            except Exception as e:
                print(f"Error occurred while creating file: {e}")
        case '2':
            filename = input("Enter the file name: ")
            path = input("Enter the file path: ")
            full_path = os.path.join(path, filename)
            try:
                if os.path.exists(full_path):
                    os.remove(full_path)
                    print(f"{filename} deleted successfully.")
                    say(f"{filename} deleted successfully.")
                else:
                    print(f"{filename} does not exist.")
                    say(f"{filename} does not exist.")
            except Exception as e:
                print(f"Error occurred while deleting file: {e}")
        case '3':
            print("Exiting...")
            say("Exiting...")
        case _:
            print("Invalid input")

def find_file():
    filename = input("Enter the file name: ")
    path = input("Enter the file path: ")
    full_path = os.path.join(path, filename)
    try:
        if os.path.exists(full_path):
            print(f"{filename} found at {full_path}.")
            say(f"{filename} found at {full_path}.")
        else:
            print(f"{filename} not found in {path}.")
            say(f"{filename} not found in {path}.")
    except Exception as e:
        print(f"Error occurred while searching for file: {e}")

def list_files():
    path = input("Enter the directory path: ")
    try:
        if os.path.exists(path):
            files = os.listdir(path)
            print(f"Files in {path}:")
            for file in files:
                print(file)
        else:
            print(f"{path} does not exist.")
            say(f"{path} does not exist.")
    except Exception as e:
        print(f"Error occurred while listing files: {e}")

def create_directory():
    dir_name = input("Enter the directory name: ")
    path = input("Enter the directory path: ")
    full_path = os.path.join(path, dir_name)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
        print(f"{dir_name} created successfully at {full_path}.")
        say(f"{dir_name} created successfully at {full_path}.")
    else:
        print(f"{dir_name} already exists at {full_path}.")

def delete_directory():
    dir_name = input("Enter the directory name: ")
    path = input("Enter the directory path: ")
    full_path = os.path.join(path, dir_name)
    try:
        if os.path.exists(full_path):
            os.rmdir(full_path)
            print(f"{dir_name} deleted successfully from {full_path}.")
            say(f"{dir_name} deleted successfully from {full_path}.")
    except Exception as e:
        print(f"Error occurred while deleting directory: {e}")
    else:
        print(f"{dir_name} does not exist at {full_path}.")


def list_directories():
    path = input("Enter the directory path: ")
    try:
        if os.path.exists(path):
            dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
            print(f"Directories in {path}:")
            for dir in dirs:
                print(dir)
        else:
            print(f"{path} does not exist.")
            say(f"{path} does not exist.")
    except Exception as e:
        print(f"Error occurred while listing directories: {e}")

def main_menu():
    print("1. Shutdown\n2. File Manager\n3. Find File\n4. List Files\n5. Create Directory\n6. Delete Directory\n7. List Directories\n8. Exit")
    say("Please choose an option from the menu.")
    choice = input("Enter your choice: ")
    match choice:
        case '1':
            main()
        case '2':
            file_manager()
        case '3':
            find_file()
        case '4':
            list_files()
        case '5':
            create_directory()
        case '6':
            delete_directory()
        case '7':
            list_directories()
        case '8':
            print("Exiting...")
        case _:
            print("Invalid input")

command = input("Do you want to use voice commands? (yes/no): ").lower()
if command == "yes":
    say("Voice commands activated. Please say your command.")
    user_command = listen()
    if user_command != "None":
        print(f"You said: {user_command}")
        say(f"You said: {user_command}")
        # Here you can add code to process the user's voice command and call the appropriate functions
else:
    main_menu()
if __name__ == "__main__":
    main_menu()