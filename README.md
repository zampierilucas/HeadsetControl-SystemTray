HeadsetControl-SystemTray
=====
A [Sapd/HeadsetControl](https://github.com/Sapd/HeadsetControl) system tray indicator for Windows.

For a list of supported devices please check [Sapd/HeadsetControl](https://github.com/Sapd/HeadsetControl).  

### Images
Over 25%                   |  Under 25%                |  Over     15%             | Charging 
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
![On Battery white](images/headset-battery-white-indicator.png)  |  ![On Battery yellow](images/headset-battery-yellow-indicator.png) | ![On Battery red](images/headset-battery-red-indicator.png) | ![Charging](images/headset-charge-indicator.png)


#### When disconnected/sleeping
The System tray icon hides itself, so it does't consumes space on your system tray.

## Usage
Download the latest release from the [github releases pages](https://github.com/zampierilucas/HeadsetControl-SystemTray/releases).  
Double-click to run, no installation needed.

## Start on Startup
Open Task Schedules, add the HeadsetControl_SystemTray.exe to the startup schedule.

## Building
### Requirements
[Python3 And pip](https://www.python.org/downloads/)

### Installation
```
git clone https://github.com/zampierilucas/HeadsetControl-SystemTray.git
cd HeadsetControl-SystemTray

pip install .
```

### Running
```
python _init_.py
```
