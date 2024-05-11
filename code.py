import board
import time
import digitalio
from adafruit_ht16k33.segments import Seg7x4
import adafruit_max1704x
from analogio import AnalogIn

# set up the 7 segment display
i2c = board.I2C()
display = Seg7x4(i2c)
display.brightness = 0.2

# read and show battery level on startup
max17 = adafruit_max1704x.MAX17048(i2c)
time.sleep(1)
display.print(round(max17.cell_percent))
time.sleep(2)
display.fill(0)
display.print("-")

# setup digital input for cadence counter - not currently used
# digital input used is A2
'''
cadenceSensor = digitalio.DigitalInOut(board.A2)
cadenceSensor.switch_to_input(pull=digitalio.Pull.UP)
cadence_last_state = True
cadence_last_value = 0
lastCrank = time.monotonic()
'''

# analog input for resistance measurement
# wires from sensor go to: 3v, A1, ground
resistancePot = AnalogIn(board.A1)
lastResVal = 1

while True:
    resVal = (round(resistancePot.value/100)) - 166
    # raw value of resistancePot on my bike is about 167 to 587
    # converted above to 1 to 422
    # now make a percentage
    resVal = round((resVal/422)*100)
    if (resVal != lastResVal):
        display.fill(0)
        display.print(resVal)
        lastResVal = resVal
        print(resVal)

    # as we're doing resistance, no need to read too often:
    time.sleep(1)
    
    # the below calculates cadence - not currently used
    '''
    if not cadenceSensor.value:
        # state false, button pushed
        if cadence_last_state == True:
            # changed
            cadence_last_state = False
    else:
        #state true, button released
        if cadence_last_state == False:
            # changed
            cadence_last_state = True
            # calculate cadence
            newCrank = time.monotonic()

            if newCrank != lastCrank:
                # valid crank
                revTime = newCrank - lastCrank

                cadenceRpm = (round(60/revTime))

                if not cadenceRpm > 200:
                    # valid cadence

                    lastCrank = newCrank

                    if cadenceRpm != cadence_last_value:
                        # update display
                        cadence_last_value = cadenceRpm
                        display.fill(0)
                        if cadenceRpm < 20:
                            display.print("-")
                        else:
                            display.print(cadenceRpm)
    '''

