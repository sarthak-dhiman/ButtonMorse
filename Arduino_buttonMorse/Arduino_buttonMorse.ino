#includ
e <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);// Define pin numbers
const int enter = 13 ;
const int dot = 12;
const int dash = 11;

// Define Morse code dictionary
const char* morse_dict[] = {
    "01:A",
    "1000:B",
    "1010:C",
    "100:D",
    "0:E",
    "0010:F",
    "110:G",
    "0000:H",
    "00:I",
    "0111:J",
    "101:K",
    "0100:L",
    "11:M",
    "10:N",
    "111:O",
    "0110:P",
    "1101:Q",
    "010:R",
    "000:S",
    "1:T",
    "001:U",
    "0001:V",
    "011:W",
    "1001:X",
    "1011:Y",
    "1100:Z",
    "11111:0",
    "01111:1",
    "00111:2",
    "00011:3",
    "00001:4",
    "00000:5",
    "10000:6",
    "11000:7",
    "11100:8",
    "11110:9",
    "010101:.",
    "110011:,",
    "001100:?",
    "10101:'",
    "100001:!",
    "01010:/",
    "10010:(",
    "001001:)",
    "01010:&",
    "00001:",
    "11011:;",
    "1100:=",
    "10001:+",
    "010010:-",
    "00100:\"",
    "10101:$",
    "010101:@"
};


// Initialize Morse code input variables
String input_value = "";

// Define constants for Morse code timing
const unsigned long dotDuration = 100; // Duration of a dot in milliseconds
const unsigned long dashDuration = dotDuration * 3; // Duration of a dash (3 times the duration of a dot)
const unsigned long spaceDuration = dotDuration * 7; // Duration of space between letters (7 times the duration of a dot)
const unsigned long wordSpaceDuration = dotDuration * 15; // Duration of space between words (15 times the duration of a dot)

// Last time a dot or dash was received
unsigned long lastPressTime = 0;

void setup() {
    Wire.begin();
    lcd.init();                      // Initialize the LCD
    lcd.backlight();
    // Initialize GPIO pins
    pinMode(enter, INPUT);
    pinMode(dot, INPUT);
    pinMode(dash, INPUT);
    
    // Initialize serial communication
    Serial.begin(9600);
    lcd.setCursor(0, 0);
    lcd.print("ButtonMorse");
    lcd.setCursor(0, 1);
    lcd.print("Enter Morse Code:");
}

void loop() {
    // Read Morse code input
    while (!digitalRead(enter)) {
        if (digitalRead(dots)) {
            processInput('0');
        } else if (digitalRead(dash)) {
            processInput('1');
        }
    }
}

void processInput(char input) {
    unsigned long currentTime = millis();

    if (input == '0' || input == '1') {
        input_value += input;
        lastPressTime = currentTime;
    } else {
        // Check if it's time to process the Morse code
        if (currentTime - lastPressTime >= spaceDuration) {
            // Translate Morse code to letters
            String translated_text = "";
            for (int i = 0; i < sizeof(morse_dict) / sizeof(morse_dict[0]); i++) {
                if (input_value == morse_dict[i]) {
                    translated_text += (char)('A' + i);
                    break;
                }
            }

            // Print translated text
            Serial.print(translated_text);
             // Print translated text on LCD
            lcd.clear();
            lcd.setCursor(0, 1);
            lcd.print("Translated: ");
            lcd.print(translated_text);

            // Check if it's a word space
            if (currentTime - lastPressTime >= wordSpaceDuration) {
                Serial.print(' '); // Print space between words
                
                // Print space between words on LCD
                lcd.setCursor(0, 0);
                lcd.print("Enter Morse Code:");
            }
            
            
            input_value = ""; // Clear input for the next Morse code input
        }
    }
}

