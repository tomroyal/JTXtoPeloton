# JTX to Peloton

### Read estimated Peloton resistance from a Cyclo Studio v5 spin bike

NOTE - I have no affiliation with either JTX or Peloton, and this code is endorsed by neither. It is a prototype only, and you use this code entirely at your own risk.

This little project works with the JTX Cyclo Studio v5 spin bike:

https://www.jtxfitness.com/jtx-cyclo-studio-bike

The bike is great, and it has an analogue resistance control - also great! But then the provided computer reads the resistance as a value between 1 and 10, which is very limiting if you're using something like the Peloton app. The aim of this project is to use the stock sensor to provide a more useful resistance reading for the Peloton app. Here's a photo of my prototype:

<img src="https://tomroyal.com/wp-content/uploads/2024/05/IMG_1953-1-1536x2048.jpeg" alt="Prototype photo" style="width:300px;"/>

The code runs on a Feather (I'm using an RP2040), and connects to the bike via its 3-wire resistance meter socket - just unplug the stock computer, and plug this in. 

It reads the resistance meter (it's a 5k ohm linear potentiometer) and displays it on an Adafruit 7-segment LED display (https://www.adafruit.com/product/879). 

The display shows an estimated Peloton resistance value based on the potentiometer reading. This is based on power (W) readings taken using Assioma power meter pedals. The data used for that calculation is here:

https://docs.google.com/spreadsheets/d/1phBzvnZTu-vwDQL-BnK64fzGEx6X7WDXilE5ZM7WXug/

I also integrated a LiPo battery monitor using the MAX17048 (https://www.adafruit.com/product/5580), so when powered on the display shows a battery %, and experimented with measuring the cadence, too - that works, but is commented out.

Details: https://tomroyal.com/2024/05/27/jtx-cyclo-studio-v5-to-peloton/
