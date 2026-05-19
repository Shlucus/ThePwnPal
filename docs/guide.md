##  🗺️ Guide

 - Youtube video coming soon!
   
### Step 1: Flashing Kali Linux

The first thing to do is flash the Kali Linux ARM image into your designated Micro SD. Any Imaging software can be used (I suggest the offical [Raspberry Pi Imager](https://www.raspberrypi.com/software/)).
You can download the Kali Linux ARM image here -> [Kali Linux ARM](https://www.kali.org/get-kali/#kali-arm)

Make sure you have:
- Selected Raspberry Pi 4 as the Device.
- Operating System > Use Custom > *Kali Linux ARM Image*
- Using a Grade 10 MicroSD with 16Gb or above.

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

#### 4.1 Installing Usefull Packages

```
sudo apt update
sudo apt full-upgrade -y
sudo apt install -y docker.io rtl-sdr
```

#### 4.2 Alpha Adapter Drivers
  - You can find the script here: [AlphaDriver.sh](../Software/Helper%20Scripts/AlphaDriver.sh)

```
sudo apt install -y kalipi-kernel-headers build-essential bc dkms git
mkdir -p ~/src
cd ~/src
git clone https://github.com/morrownr/8821au-20210708.git
cd ~/src/8821au-20210708
sudo ./install-driver.sh
```
