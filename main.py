import pyautogui
import random
import time

# Display a message box with an input field
result = pyautogui.prompt("Enter your account name:")

# Initialize the counter
counter = 0

while True:
    # Display the header with black background and white text
    pyautogui.alert(text='Robux Miner', title='Robux Miner', button='OK', bg='black', fg='white')

    # Increase the counter by a random amount
    counter += random.randint(5, 13)

    # Print the message
    pyautogui.alert(text=f"{result}: Robux mined {counter}", title='Robux Miner', button='OK', bg='black', fg='white')

    # Sleep for 6 seconds
    time.sleep(6)
