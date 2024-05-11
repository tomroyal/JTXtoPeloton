# JTX to Peloton

### Read 0-100 resistance from a Cyclo Studio v5 spin bike

This little project works with the JTX Cyclo Studio v5 spin bike:

https://www.jtxfitness.com/jtx-cyclo-studio-bike

The bike is great, and it has an analogue resistance control - also great! But then the provided computer reads the resistance as a value between 1 and 10, which is very limiting if you're using something like the Peloton app. The aim of this project is to use the stock sensor to provide a more accurate resistance reading on a 0 to 100 scale.

This code runs on a Feather (I'm using an RP2040), and connects to the bike via its 3-wire resistance meter socket - just unplug the stock computer, and plug this in. 

It reads the resistance meter (it's a 5k ohm linear potentiometer) on a scale from 0 to 100, and displays it on an Adafruit 7-segment LED display (https://www.adafruit.com/product/879). 

I also integrated a LiPo battery monitor using the MAX17048 (https://www.adafruit.com/product/5580), so when powered on the display shows a battery %, and experimented with measuring the cadence, too - that works, but is commented out.

This is a prototype - any use is entirely at your own risk.
