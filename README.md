# Devialet Remote
This project is a command line tool written in **Python** to control **Devialet** speakers using the **DOS2** operating system.

I created this project because I needed to control the volume of my **Devialet** speaker from my **Apple TV** remote. The speaker is connected to my TV with an optical cable, which does not allow the TV to change the speaker's volume.

After a lot of unsuccessful attemps to implement **HDMI-CEC** with my **Samsung TV**, I decided to use a **FLIRC USB IR receiver** and it works flawlessly.

If you have any TV remote compatible with IR control (**Apple TV Remote**, **Samsung Smart TV Remote**, etc.), you can use the remote with this tool to control your speaker.

This tool will also enable you to switch the speaker's input source to anything you wish by double-pressing the mute button on your remote.

# Requirements

I'm running this tool on a Raspberry Pi 3B, and if you wish to use the **FLIRC dongle** on a **Raspberry Pi**, I suggest using **Raspberry Pi OS Full (32-bit) Bullseye** as an operating system because I have had issued with the **FLIRC** software on lite and standard versions.

## Setting-up the Pi for FLIRC (optional)

This is more of a reminder of what I did in case I need to reinstall my Raspberry Pi.

Image the MicroSD card using Raspberry Pi Imager, select **Raspberry Pi OS Full (32-bit)** as the operating system.

Change advanced options:
- Set hostname: devialet-remote.local
- Enable SSH
- Set username and password
- Set locale settings

Once the Pi has booted:

```console
sudo raspi-config
```

Enable RealVNC in **Interface Options**.

Access the Pi's graphical interface using VNC Viewer and install FLIRC:

```console
curl apt.flirc.tv/install.sh | sudo bash 
```

Open the Flirc GUI from **Accessories** and switch the controller to **Full Keyboard**.

Record all the keys you with to use to control your Devialet speaker, I suggest doing the following bindings because they are set as default in the code:

- **F1:** Volume Down
- **F2:** Volume Up
- **F3:** Mute

## Setting-up the tool

Retrieve the project:

```console
git clone https://github.com/lucasarnulphy/devialet-remote.git
cd devialet-remote
```

If you wish to use venv:

```console
python -m venv .venv
source .venv/bin/activate
```

Install the dependancies:

```console
python -m pip install -r requirements.txt
```

# Using the tool

The main script for the tool is the remote.py script. You can get help for any command by using the **--help** option.

There are two ways of using this tool, you can either specify:

- The Devialet speaker's **IP address**, if it is fixed.
- The Devialet speaker's **DeviceId**, if the speaker's IP address might change.

## List

To get the speaker's IP address or DeviceId, you can use the list devices tool.

```console
python remote.py list devices
```

To get a more organized view of your speaker system, you can use the list systems tool.

```console
python remote.py list systems
```

To get information about the available sources on each device, you can use the list sources tool.

```console
python remote.py list sources
```

## Configuration

For this tool to work, you need to set some values in the **config.py** file.

1. If you want to use your speaker's **DeviceId**, set the *config_devialet_device_id* variable to your speaker's DeviceId). (Skip if using IP)

2. If you want to use your speaker's **IP address**, set the *config_devialet_ip* variable to your speaker's IP address. (Skip if using DeviceId)

3. If you want to specify a source to switch to when using playback functions (play, pause, mute, unmute), set the *config_devialet_source_id* to your source's SourceId.

4. If you need to edit the listener's configuration (change default keys, add other bindings, etc.), everything happens in the *config_listener_dict* variable.

### Actions

To get a list of all the actions you can run, use the **--help** option.

The actions names are self-explanatory.

```console
python remote.py action --help
```

## Listener

The listener allows you to execute actions when pressing certain keys on your keyboard. Before using the listener, try running some actions to make sure everything is working as expected.

To start the listener, you can use the listener start command.

```console
python remote.py listener start
```

> If you've set the *config_devialet_source_id* variable to something else than current, you can use any of the play, pause, mute, unmute actions to switch your speaker's source. For instance, if you're listening music on spotify and want to switch to the optical source, you can double press the mute_toggle button, which will mute then unmute the speaker, and change the source.