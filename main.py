#started
#this project will be continued after completion of git learning dated 29/3/2024
#dated- 1/4/2024 , circuitpython selected as programming language
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

# OLED display dimensions
WIDTH = 128
HEIGHT = 64

# Initialize I2C interface
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)

# Initialize OLED display
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Messages to be displayed (split into two lines)
welcome_message_line1 = "Welcome to"
welcome_message_line2 = "ButtonMorse"
enter_text_message = "Enter Text To Be"
enter_text_message_line2 = "Translated"

# Define GPIO pins for dot, dash, and enter
dot_pin = Pin(17, Pin.IN, Pin.PULL_UP)
dash_pin = Pin(18, Pin.IN, Pin.PULL_UP)
enter_pin = Pin(16, Pin.IN, Pin.PULL_UP)

# Define Morse code dictionary
morse_dict = {
    "01": "a", "1000": "b", "1010": "c", "100": "d", "0": "e",
    "0010": "f", "110": "g", "0000": "h", "00": "i", "0111": "j",
    "101": "k", "0100": "l", "11": "m", "10": "n", "111": "o",
    "0110": "p", "1101": "q", "010": "r", "000": "s", "1": "t",
    "001": "u", "0001": "v", "011": "w", "1001": "x", "1011": "y",
    "1100": "z", "11111": "0", "01111": "1", "00111": "2", "00011": "3",
    "00001": "4", "00000": "5", "10000": "6", "11000": "7", "11100": "8",
    "11110": "9"
}

# Function to display typing effect for a single line
def typing_effect_line(line, y, start_time):
    for i in range(len(line) + 1):
        oled.fill(0)
        oled.text(line[:i], (WIDTH - len(line) * 8) // 2, y)  # Center the text horizontally

        # Calculate the elapsed time
        elapsed_time = time.time() - start_time
        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time % 60)
        timer_text = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)

        # Display the timer in the top-right corner
        oled.text(timer_text, WIDTH - len(timer_text) * 8, 0)

        oled.show()
        time.sleep(0.2)  # Adjust delay for typing speed

# Function to display typing effect for both lines
def typing_effect(line1, line2, start_time):
    typing_effect_line(line1, HEIGHT // 2 - 12, start_time)
    time.sleep(1)  # Pause before displaying the second line
    typing_effect_line(line2, HEIGHT // 2, start_time)

# Function to display the entered Morse code with a blinking cursor
def display_morse_code(input_text, cursor_pos, start_time):
    oled.fill(0)
    oled.text(enter_text_message, (WIDTH - len(enter_text_message) * 8) // 2, HEIGHT // 2 - 12)
    oled.text(enter_text_message_line2, (WIDTH - len(enter_text_message_line2) * 8) // 2, HEIGHT // 2)
    
    # Display entered Morse code
    oled.text(input_text, 0, HEIGHT // 2 + 12)
    
    # Display blinking cursor
    if int(time.time() * 2) % 2 == 0:  # Blinking interval for the cursor
        oled.fill_rect(cursor_pos * 8, HEIGHT // 2 + 12, 8, 8, 1)
    
    # Calculate the elapsed time
    elapsed_time = time.time() - start_time
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    timer_text = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)
    
    # Display the timer in the top-right corner
    oled.text(timer_text, WIDTH - len(timer_text) * 8, 0)
    
    oled.show()

# Function to translate Morse code to text
def translate_morse_code(morse_code):
    words = morse_code.split('   ')  # Split by 7 spaces for words
    translated_text = ''
    for word in words:
        letters = word.split(' ')  # Split by 3 spaces for letters
        for letter in letters:
            translated_text += morse_dict.get(letter, '?')  # '?' for unknown characters
        translated_text += ' '  # Space between words
    return translated_text.strip()

# Main loop to display welcome message, then enter Morse code
start_time = time.time()
typing_effect(welcome_message_line1, welcome_message_line2, start_time)
time.sleep(2)  # Pause before clearing the screen

oled.fill(0)  # Clear the screen
oled.show()

input_text = ""
cursor_pos = 0
morse_code = ""

while True:
    display_morse_code(input_text, cursor_pos, start_time)
    
    if not dot_pin.value():  # Dot button pressed
        input_text += "."
        morse_code += "0"
        cursor_pos += 1
        time.sleep(0.5)  # Debounce delay
    elif not dash_pin.value():  # Dash button pressed
        input_text += "-"
        morse_code += "1"
        cursor_pos += 1
        time.sleep(0.5)  # Debounce delay
    elif not enter_pin.value():  # Enter button pressed
        translated_text = translate_morse_code(morse_code)
        break  # Exit the loop to display the translated text
    time.sleep(0.1)

# Display translated text
oled.fill(0)  # Clear the screen
oled.text("Translated Text:", 0, HEIGHT // 2 - 12)
oled.text(translated_text, 0, HEIGHT // 2)
oled.show()
