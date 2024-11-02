import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
import time

def main():
    lcd_columns = 16 # How many characters we can fit on the screen
    lcd_rows = 2     # How many rows of characters we have

    # Replace x with the pin number, board.GPx in CircuitPython is the same as machine.Pin(x) in MicroPython
    scl_pin = board.GP1
    sda_pin = board.GP0

    i2c = busio.I2C(scl_pin, sda_pin)
    # Initialize the LCD
    lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

    while True:
        if lcd.select_button:
            lcd.clear()
            lcd.message = "pressed"
        
        else:
            lcd.message = "Not pressed"


if __name__ == "__main__":
    main()