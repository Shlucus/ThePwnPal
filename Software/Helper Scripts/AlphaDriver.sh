sudo apt install -y kalipi-kernel-headers build-essential bc dkms git
mkdir -p ~/src
cd ~/src
git clone https://github.com/morrownr/8821au-20210708.git
cd ~/src/8821au-20210708
sudo ./install-driver.sh