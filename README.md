# Linux-Switch-Heaphones-Mode
Command to automatically change bluetooth headphones mode.

## How to use
* Download python script
* Make script executable : 
```
# Download from github
git clone git@github.com:RomainDLS/Linux-Switch-Heaphones-Mode.git

# Run script to switch bluetooth profile (pulseaudio)
./bluetooth_switch_mode.py

# Run script to switch bluetooth profile (pipewire)
./pipewire_bluetooth_switch_mode.py
```
* Create ubuntu shortcut that will call this script in order to facilitate bluetooth profile switch.

## Limitation
* Supported `pacmd` profiles : `headset_head_unit` and `a2dp_sink`.
* Work with only one bluetooth device connected.