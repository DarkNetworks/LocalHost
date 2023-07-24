# LocalHost

<p align="center">
  <img src="https://github.com/DarkNetworks/LocalHost/assets/108237499/fa4f3f58-19fc-49ab-a182-8d8447b2b391" alt="LocalHost Logo" width="575" height="163">
</p>

Welcome to LocalHost! 🚀

## Overview

LocalHost is a lightweight and user-friendly Python tool that allows you to effortlessly host files from your local directory using a simple HTTP server. It's a convenient way to serve static content, such as HTML, CSS, JavaScript, images, and more, right from your local machine.

## Features

- 📁 Serve Files: Host files from any directory on your computer with ease.
- 🌐 Web Server: Turn your local machine into a mini web server.
- 🚀 Easy-to-Use: Simple setup and one-click hosting.
- 🔧 Customizable: Configure the server settings to your preferences.
- 📜 Logging: Optional logging feature to keep track of server activity.

## Installation

To get started with LocalHost, follow these steps:

1. Clone this repository to your local machine.

With GIT
```console
git clone https://github.com/DarkNetworks/LocalHost.git
```

2. Ensure you have Python installed (Python 3 recommended).
3. Install the required dependencies:

```console
pip install -r requirements.txt
```

## Usage

1. Customize the server settings in `settings.json`:
```json
{
  "server": {
    "host": "localhost",
    "port": 8080,
    "directory": "Directory Path"
  },
  "logging": {
    "enabled": true,
    "log_file": "logs/log.txt",
    "log_level": "INFO"
  }
}
```

Replace 'Directory Path' with the absolute path of the directory you want to serve.

2. Run the `LocalHost.py` script

```console
python LocalHost.py
```
3. Your server is now up and running! Access your files by navigating to http://localhost:8080/ in your web browser (replace 8080 with the port specified in settings.json).

## Customization
You can customize the server behavior by adjusting the settings in settings.json:

- "host": Set the hostname (default is "localhost").
- "port": Set the port number (default is 8080).
- "directory": Set the absolute path of the directory you want to serve.

## Logging (Optional)
LocalHost offers logging functionality to keep track of server activity. To enable logging, set `"enabled": true` in `settings.json`. Additionally, customize to your likings!

- "enabled": Enable or disable logging
- "log_file": Set the file to write logs to (default is "logs/log.txt")
- "log_level": Set the level of logging (DEBUG, INFO, WARNING, ERROR, CRITICAL)

## Contributions
Contributions to LocalHost are welcome! Feel free to open issues, submit feature requests, or create pull requests.

## License
LocalHost is released under the [MIT License](https://github.com/DarkNetworks/LocalHost/blob/main/LICENSE).

Happy hosting! 🎉