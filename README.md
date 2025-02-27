ButtonMorse is a non conventional morse decoder based upon microcontrollers , coded with Python or C++ depending upon the
microcontroller used.
the standalone windows version provides decoding without use of any support hardware of the original version

Morse is older binary communication method that uses dashes and dots to encode the data.
the goal of this project is to create a decoder that helps with visual and interactive learning of the learning.
the basic idea is to use two switches , to feed dots and dashes whilst the third switch can act as enter to denote the sequence 
of a single charachter has been entered and is ready to be decoded or act as a delete key if the user feels like the entered 
sequence is flawed

**the dictionary for input conversion of morse is typed assuming dots as 0 and dashes as 1.**
a = (0,1)
b = (1,0,0,0)
c = (1,0,1,0)
d = (1,0,0)
e = (0)
f = (0,0,1,0)
g = (1,1,0)
h = (0,0,0,0)
i = (0,0)
j = (0,1,1,1)
k = (1,0,1)
l = (0,1,0,0)
m = (1,1)
n = (1,0)
o = (1,1,1)
p = (0,1,1,0)
q = (1,1,0,1)
r = (0,1,0)
s = (0,0,0)
t = (1)
u = (0,0,1)
v = (0,0,0,1)
w = (0,1,1)
x = (1,0,0,1)
y = (1,0,1,1)
z = (1,1,0,0)
one = (0,1,1,1,1)
two = (0,0,1,1,1)
three =(0,0,0,1,1)
four = (0,0,0,0,1)
five = (0,0,0,0,0)
six =  (1,0,0,0,0)
seven = (1,1,0,0,0)
eight = (1,1,1,0,0)
nine = (1,1,1,1,0)
ten = (1,1,1,1,1)
question = (0,0,1,1,0,0)
exclamation = (1,0,1,0,1,1)
dot = (0,1,0,1,0,1)
semicolon = (1,1,0,0,1,1)
colon = (1,1,1,0,0,0)
plus = (0,1,0,1,0)
minus =(1,0,0,0,1)
slash = (1,0,0,1,0)
equal = (1,0,0,0,1)


**PREQUISITES for ButtonMorse**
-->RP2040 driven board with the micropython firmware loaded into it
-->arduino based boards can also be used but with no HID interface(*HID to be implemented as of yet*) 
-->I2C based display , preferably an oled due to input voltage and code adjustment ease

**The Instructions to use the translator are as follows(for ver-0.1)**
1) Power on the microcontroller , ensuring the wiring is as per schematics
*GP38-GND,GP36-3.3V,GP01-SDA,GP02-SCL,GP18-DOT_SWITCH,GP22-DASH_SWITCH,GP28-ENTER_SWITCH*
2) Wait until the buttonMorse splash screen is over and the prompt is asked for
3) For this rev translation can only be done per alphabet at a time(*later versions will work to have support for words) so enter the morse code and press the enter
4) The next screen should display your translated alphabet
5) Press enter to clear screen and get prompt for next input

**Features to be implemented in future revesions**
1) Input support for a word at a time, instead of alphabet
2) Desktop application verison that can inputs from standard keyboards or the rp2040
3) Making RP2040 translator dual act as a morsepad(keypad for morse)
4) Wireless interconnectivity between application and the board
5) Modes to configure translator to work on a single key or the easier 3 key mode
6) Addition of relays to mimic the clicking and clacking sounds
7) Animating the button logo to look as if its pressed to start

**Revisions**   

***VER-0.1*** *Released- 23/06/2024*
--> Implemented basic translation functions for a single alphabet output 
--> Added 126x64 oled support
--> Basic splash and ui for the newly added oled
--> Rudamentry input stream using gateron red switches

***VER-0.2*** *Released- 16/8/2024*
-->Added splash screen
-->Changed and refined the way input is taken
-->Rebuilt the translation method
-->Added enough backend to support the animating logo
