
 <div align="center">
  <hr>
  
  ![PwnPalVideo_Banner](https://github.com/Shlucus/ThePwnPal/assets/111912000/ceb6b3aa-dacb-4e9c-8449-2380e0ed763e)
  
  <hr>
  <h3 align="center">
 Creating a standalone and pocket-sized pentesting device for on-the-go ethical hacking proceedures. <br><br>
  <a href="#">
    <img src="https://awesome.re/badge.svg" alt="Awesome" height=24>
    <img src="https://img.shields.io/badge/Powered%20by-Raspberry%20Pi-c01355" alt="Powered by Raspberry Pi" height=24>
    <img src="https://img.shields.io/badge/Developed%20by-Shlucus-brightgreen" alt="Developed by Shlucus" height=24 title="Developer of this project">
    <img src="https://img.shields.io/badge/Hack-The%20Planet-orange" alt="Hack the planet" height=24>
    <img src="https://img.shields.io/badge/Version-1.1-lightblue" alt="Version 1.1" height=24>
  </a>

<div align="center">
 
   [!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoffee.com/Shlucus)
   
</div>
</h3>
</div>




## 📚 Table of Contents:
 - [Overview](https://github.com/Shlucus/TheRaspberryPwn?tab=readme-ov-file#-overview)
 - [Features](https://github.com/Shlucus/TheRaspberryPwn?tab=readme-ov-file#-features)
 - [Components](https://github.com/Shlucus/TheRaspberryPwn?tab=readme-ov-file#-components)
 - [Guide](https://github.com/Shlucus/TheRaspberryPwn?tab=readme-ov-file#%EF%B8%8F-guide)
   
## 📝 Overview
This project transforms a Raspberry Pi into a portable penetration testing device, combining the versatility of Kali Linux with the compact form factor of the Raspberry Pi. It enables security professionals and enthusiasts to tactically conduct mobile pentesting and ethical hacking activities on-the-go. Inspired by the [Pwnagotchi Project](https://pwnagotchi.ai/), my goal was to create my own pocket-sized pentesting or 'pwning' device but offering the same tools and capabilities of a complete linux desktop. Not only does it allow mobile pentesting, but also remote attacks thanks to Secure Shell (SSH) and it's small size, allowing you to easily plant the device in a target organization and monitor network traffic by running commands from anywhere in the world. 
<br>

<div align="center">
<img src="https://github.com/Shlucus/TheRaspberryPwn/assets/111912000/f612bb55-2c71-42b9-aee7-ae2f6df4076d" alt="PwnPal Pic" width="350">
<img src="https://github.com/Shlucus/TheRaspberryPwn/assets/111912000/35e0eb22-1a37-4aa8-b60c-8be9987f23c0" alt="PwnPal GIF" width="350">
</div>

## ✨ Features
- <ins>Raspberry Pi Integration</ins>: Utilizes the Raspberry Pi for its compact size and portability.
- <ins>Standalone Power:</ins> Includes a battery with 5000mAh and output current of 3A, providing 8 - 10 hours of consistant power.
- <ins>Integrated Display:</ins> Compact touchscreen display for improved user interface.
- <ins>Extensive range:</ins> Supports both 2.4 Ghz and 5 Ghz bands with packet injection and monitor mode.
- <ins>Mobile Accessibility:</ins> Conduct security assessments and penetration tests from a stealthy handheld device.
- <ins>Kali Linux:</ins> Configured with Kali Linux tools for a comprehensive penetration testing environment.

## 🔧 Components

| Component         | Purchase Link                                                                                               | Image                                                                                                                                                      |
|-------------------|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Board             | [Raspberry Pi 4 Model B (8GB)](https://www.amazon.ca/Raspberry-Pi-Model-Bluetooth-Enabled/dp/B09TTKT94J/ref=sr_1_11?keywords=Raspberry+pi+4&sr=8-11&ufe=app_do%3Aamzn1.fos.b06bdbbe-20fd-4ebc-88cf-fa04f1ca0da8) |   <img src="https://github.com/Shlucus/TheRaspberryPwn/assets/111912000/8dc0354c-b954-46d2-bd63-9412a2e3605d" alt="Board" width="350">                     |
| Display           | [Waveshare 3.5inch Touch Screen RPi LCD (C)](https://www.waveshare.com/3.5inch-rpi-lcd-c.htm)             |   <img src="https://github.com/Shlucus/TheRaspberryPwn/assets/111912000/f7338ae7-e87a-496b-bdb3-3976ddd19736" alt="Display (Top)" width="250"><img src="https://github.com/Shlucus/TheRaspberryPwn/assets/111912000/2f5d04aa-55be-41dc-9495-2dd5e4008d78" alt="Display (Bottom)" width="250"> |
| Battery           | [PiSugar S Plus](https://www.tindie.com/products/pisugar/pisugar-s-plus-battery-for-raspberry-pi-3b3b4b/) |   <img src="https://github.com/Shlucus/TheRaspberryPwn/assets/111912000/ab007f11-0f02-4b0c-b28e-bb038a390f64" alt="Battery" width="300">                      |
| Network Adapter   | [ALPHA AWUS036ACS](https://www.amazon.ca/ALFA-NETWORK-AWUS036ACS-Alfa-Adapter/dp/B0752CTSGD/ref=sr_1_2?keywords=ALPHA+AWUS036ACS&sr=8-2) |   <img src="https://github.com/Shlucus/TheRaspberryPwn/assets/111912000/aa81f1ed-4bd0-4201-b2ae-de06449dceaa" alt="ALPHA Adapter" width="250">                     |
| Heatsink (optional) | [Aluminum Alloy Cooling Case by WEIYIXING](https://www.amazon.ca/dp/B0BBPPYV76?ref=ppx_yo2ov_dt_b_product_details&th=1)      |    <img src="https://github.com/Shlucus/TheRaspberryPwn/assets/111912000/3d8a635f-773b-4cfe-8487-ec58db65ffed" alt="Heatsink" width="250">                             |


##  🗺️ Guide

 - Youtube video coming soon!
   
### Step 1: Flashing Kali Linux

The first thing to do is flash the Kali Linux ARM image into your designated Micro SD. Any Imaging software can be used (I suggest the offical [Raspberry Pi Imager](https://www.raspberrypi.com/software/)).
You can download the Kali Linux ARM image here -> [Kali Linux ARM](https://www.kali.org/get-kali/#kali-arm)

Make sure you have:
- a) Selected Raspberry Pi 4 as the Device.
- b) Operating System > Use Custom > *Kali Linux ARM Image*
- c) Grade 10 MicroSD with 16Gb or above.

<div align="center">
 <img src="https://github.com/Shlucus/TheRaspberryPwn/assets/111912000/36ccdba4-c032-456b-a3a4-dfc3fe0735cb" alt="Board (Bottom)" width="500">
</div>

### Step 2: Installing LCD Display

Due to the Waveshare screen's simple design, installing it is as easy as plugging it's GPIO ports directly to the Pi's GPIO pins. If done correctly, the screen should rest on top of the the Pi's USB 2.0 and 3.0 USB ports.

> [!TIP]
> If using the Heatsink mentioned in the 'Components' section, the aluminum will interfere with the screen's own components on the underside. This will prevent the screen from sitting flush against the device.  To fix this, you can either alter the heatsink directly by reducing its surface, or like I did, make supports on the corners of the screen between the heatsink with adhesive putty. (Ensures stability and keep  the screen glued to the device)

<div align="center">
 <img src="https://github.com/Shlucus/TheRaspberryPwn/assets/111912000/90756a6b-c6ad-4068-be0c-bb6cd0749652" alt="Board Side1" width="300">
 <img src="https://github.com/Shlucus/TheRaspberryPwn/assets/111912000/4d4fd66e-8615-431e-9833-ef367741ab30" alt="Board Side2" width="300">
 <img src="https://github.com/Shlucus/TheRaspberryPwn/assets/111912000/6d1af7e1-6128-46de-85c4-ae6942a8f37a" alt="Board Angle" width="300">
</div>
Once the MicroSD is inserted and Screen is connected, you will notice powering ON the Pi that the screen will remain white (this is normal). We have yet to install the drivers for the Pi to communicate with it

>[!NOTE]  
> The official Waveshare drivers for this screen will NOT work! They have a hard time working with 64Bit Kali OS.

To do so (either through Secure Shell (SSH) or through HDMI), run the following on your Pi:
  - Make sure your Pi is connected to internet!

```
sudo rm -rf LCD-show-kali
git clone https://github.com/lcdwiki/LCD-show-kali.git
chmod -R 755 LCD-show-kali
cd LCD-show-kali/
sudo ./LCD35-show
```

This should reboot your Pi and finally have the screen working!

### Step 3: Installing PiSugar Battery

First, make sure to unplug the battery from the PiSugar (JST PH 2.0 connector)

Then, take the four M2.5 screws provided from the PiSugar S Plus and screw it in from the Underside of the Pi like so:
> [!NOTE]  
> If using Heatsink, use the case's/heatsink's M2.5 screws INSTEAD, since they are longer and will allow to screw in both the battery and Heatsink at the same time.

<div align="center">
   <img src="https://github.com/Shlucus/TheRaspberryPwn/assets/111912000/9fef0136-21a9-4e96-9d45-e45975c70587" alt="Bottom" width="500">
</div>

The way this possible is thanks to the Pogo Pins on the PiSugar that allows access to the GPIO pins from the underside of the Pi! So make sure the pogo pins are properly in contact with the GPIO pins.

<div align="center">
 <img src="https://github.com/Shlucus/TheRaspberryPwn/assets/111912000/109ec049-f0a4-44d4-a827-885c8a351ebd" alt="Pogo Pins" width="500">
</div>

I strongly suggest watching this Youtube video for help with the installation -> [Pi Sugar S Plus Review](https://youtu.be/HUL5Ii0dD7E?si=tGOrOx8UDh8VqgeL)

### Step 4: Configuration

TODO...

