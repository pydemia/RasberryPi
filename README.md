# RasberryPi

## Setup

[Rasberry Pi Download](https://www.raspberrypi.org/downloads/)

```sh
sudo useradd -m -d /home/NewUser NewUser
```



Localisation Wi-Fi Country US

```sh
wpa_passphrase [network ESSID] [newwork password]

network={
         ssid="ddddd"
         #psk="aaaa"
         psk=aaa13jkllhlkljbser3r412ioo231lkj1lk2j3l1nvsdaisdraer3924jsefweu5
}
sudo vi /etc/wpa_supplicant/wpa_supplicant.conf
```

```sh
sudo chmod u+s /sbin/iwconfig
```

```sh
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh
```


```sh
conda install pip
pip install rrb3
pip install RPi.GPIO


```

```sh
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-de
sudo apt-get install build-essential cmake pkg-config
```

### Setup `vnc`

```sh
sudo apt-get install x11vnc xinetd
x11vnc storepasswd
```

### Install `openCV`

```sh
sudo apt-get install libopencv-dev python-opencv
sudo apt-get install libatlas-base-dev
```
