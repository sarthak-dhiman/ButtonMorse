#started
#this project will be continued after completion of git learning dated 29/3/2024
#dated- 1/4/2024 , circuitpython selected as programming language
import board
import digitalio
import time
import busio
import character_lcd
lcd_columns = 20
lcd_rows = 4
# Initialize I2C bus
i2c = busio.I2C(board.GP14, board.GP15)  # Change GP0 and GP1 to your SDA and SCL pins

# Initialize L~CD class
lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows)

# Clear the LCD screen
lcd.clear()
lcd.move_to(0, 1)
lcd.message = "Welcome to ButtonMorse"
lcd.clear()
lcd.move_to(0, 1)
lcd.message ='Enter Morse'
Enter = digitalio.DigitalInOut(board.GP16)

Dot = digitalio.DigitalInOut(board.GP17)

Dash = digitalio.DigitalInOut(board.GP18)
#dot= 0, dash=1
morse_dictonary = {
'a' : (0,1),
'b' : (1,0,0,0),
'c' : (1,0,1,0),
'd' : (1,0,0),
'e' : (0),
'f' : (0,0,1,0),
'g' : (1,1,0),
'h' : (0,0,0,0),
'i' : (0,0),
'j' : (0,1,1,1),
'k' : (1,0,1),
'l' : (0,1,0,0),
'm' : (1,1),
'n' : (1,0),
'o' : (1,1,1),
'p' : (0,1,1,0),
'q' : (1,1,0,1),
'r' : (0,1,0),
's' : (0,0,0),
't' : (1),
'u' : (0,0,1),
'v' : (0,0,0,1),
'w' : (0,1,1),
'x' : (1,0,0,1),
'y' : (1,0,1,1),
'z' : (1,1,0,0),
'1' : (0,1,1,1,1),
'2' : (0,0,1,1,1),
'3' : (0,0,0,1,1),
'4' : (0,0,0,0,1),
'5' : (0,0,0,0,0),
'6' :  (1,0,0,0,0),
'7' : (1,1,0,0,0),
'8' : (1,1,1,0,0),
'9' : (1,1,1,1,0),
'0' : (1,1,1,1,1),
'?' : (0,0,1,1,0,0),
'1' : (1,0,1,0,1,1),
'.' : (0,1,0,1,0,1),
';' : (1,1,0,0,1,1),
':' : (1,1,1,0,0,0),
'+' : (0,1,0,1,0),
'-' : (1,0,0,0,1),
'/' : (1,0,0,1,0),
'=' : (1,0,0,0,1) }
# morse dictionary completed and represented in form of tuples
input_value = []
while not Enter.value:
    if Dot.value:
        input_value.append('0')
    elif Dash.value:
        input_value.append('1')

translated_text = ''
for symbol in input_value:
    for letter, morse_code in morse_dictonary.items():
        if symbol == ''.join(map(str, morse_code)):
            translated_text += letter
            break

lcd.move_to(0, 1)

lcd.message =translated_text
    