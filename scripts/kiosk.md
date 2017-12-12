# Kiosk with `DAKboard`

## Korean Font Setting

```sh
sudo apt-get install ttf-unfonts-core
sudo apt-get install fonts-unfonts-core
```


## Configure `/boot/config.txt`

```sh
sudo vim /boot/config.txt
```

```sh
# rotate the screen
display_rotate=2

# use 24 bit colors
framebuffer_depth=24
```


## Kiosk Setting

```sh
sudo vim ~/.config/lxsession/LXDE-pi/autostart
```

Comment the existed one and add the following:
```sh
@xset s off
@xset -dpms
@xset s noblank
@chromium-browser --noerrdialogs --incognito --kiosk http://dakboard.com/app/?p=YOUR_PRIVATE_URL
```


## Disable `Screen Powersave Mode`

```sh
sudo vim /etc/lightdm/lightdm.conf
```

```sh
#xserver-command=X
#xserver-command=X -s 0 -dpms
```


## Disable `Screensaver`

```sh
sudo vim /etc/X11/xinit/xinitrc
```

```sh
/etc/Xll/Xsession

xset s off
xset -dpms
xset s noblank
```

## Enable to hide the mouse pointer

```sh
sudo apt-get install unclutter -y
```


