# SPARX99 - Anemometer


For this project you will need:
1. Inspeed Vortex
2. Arduino MKR1000 with Wi-Fi Shield
3. HTTP Server in LAN or WAN

First I built the Arduino board connecting the power cable and the Vortex.
The HTTP server was run on an Apache Server on a Linux computer in my LAN (I used a repeater from my apartment to the building top to make sure the Arduino could connect to same LAN), and I moved all the php file under /var/www/html with standard Apache configuration.
Lastly I programmed Arduino with anemometer.ino file and made sure it was all running!
