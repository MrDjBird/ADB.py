<h1 align="center" >:wave:Hi it's ADB.py</h1>
<img src="https://github.com/MrDjBird/ADB.py/blob/master/the_logo.png?raw=true" height="320"/>

___
<h3>Information</h3>

ADB.py help you with using **ADB**(_Android Debug Bridge_, from _Android SDK_) with **Python**
___
<h3>Next plans for updates</h3>

1. Add fastboot commands
2. Adding FileDialog to get files from computer for flashing sidloade and pushing files
___
<h3>How to use (short guide)<h3>
  
To use this library in your program you must unzip **_adb tools_**([Windows](https://github.com/MrDjBird/ADB.py/raw/master/tools_r33.0.2-windows.zip) ([XP](https://github.com/MrDjBird/ADB.py/raw/master/tools_r23.1-for-windowsXP.zip)), [Linux](https://github.com/MrDjBird/ADB.py/raw/master/tools_r33.0.2-linux.zip), [macOS](https://github.com/MrDjBird/ADB.py/raw/master/tools_r33.0.2-macosx.zip)) to the work directory of you project. If you on Windows you 
must install [usb drivers](https://github.com/MrDjBird/ADB.py/blob/master/usb_driver_r13-windows.zip) (for [Windows XP](https://github.com/MrDjBird/ADB.py/raw/master/usb_driver_r11-for-windowsXP.zip)).
All *[adb commands]()(include adb [shell]())* are moved and add some [new scripts](). How to use: `adb reboot fastboot` => `adb.reboot("fastboot")`.
If you want to use _adb shell_, for example: `adb shell reboot -p` use this command `adb.shell("reboot -p")`.

More info at [docs]().
