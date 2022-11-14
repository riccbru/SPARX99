# SPARX99 - Anemometer


For this project you will need:
1. Inspeed Vortex
2. Arduino MKR1000 with Wi-Fi Shield
3. HTTP Server in LAN or WAN

Firstly I built the Arduino board connecting the power cable and the Vortex (check PDF file).
The HTTP server was run on an Apache Server on a Linux computer in my LAN (I used a repeater from my apartment to the building top to make sure the Arduino could connect to same LAN), and I moved all the php file under /var/www/html with standard Apache configuration.
Lastly I programmed Arduino with anemometer.ino file and made sure it was all running!

Once got the samples I exported database rows in a csv file.
I then created a DataFrame in Pandas to understand the data (check python file).
