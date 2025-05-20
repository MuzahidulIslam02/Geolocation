# Geolocation
This project shows how to get a user's current location and display it on a map using the Geolocation API and a mapping service.
# 🗺️ Python Geolocation Map Viewer

A simple desktop application to search and view geographic locations on an interactive map using:

- **Tkinter** for the GUI
- **TkinterMapView** for OpenStreetMap rendering
- **Geopy** for geocoding (address to coordinates)

---

## 📸 Features

- 🔎 Search for any city, landmark, or address
- 📍 Display the location on a map with a marker
- 🌍 Pan and zoom with an interactive OpenStreetMap view

---

## ⚙️ Requirements

### ✅ Python Version:
- Python 3.7 or higher

### ✅ Python Packages:
These are installed via pip:


> You’ll install them using the `requirements.txt` file (see below).

---

## ⚠️ System Dependency

> `tkinter` is not installable via pip. You must install it using your system’s package manager:

### 🐧 Linux

#### Ubuntu/Debian:
```bash
sudo apt install python3-tk

Fedora/RHEL:

sudo dnf install python3-tkinter

Arch Linux:

sudo pacman -S tk

🍏 macOS

Usually included. If not:

brew install python-tk

🪟 Windows

Tkinter is included in standard Python installer. If not, reinstall Python and make sure the “tcl/tk and IDLE” option is selected.
📦 Installation
1. Clone or download the project:

git clone https://github.com/your-username/geolocation-app.git
cd geolocation-app

2. Install Python dependencies:

pip install -r requirements.txt

🚀 Running the App

python main.py

🧭 How to Use

    Enter a location name in the input box (e.g. New York, Tokyo, Eiffel Tower)

    Click the Search button

    The map will zoom in and show the location with a marker

📂 File Structure

geolocation-app/
├── goolemap.py              # Main application script
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

📃 License

This project is licensed under the MIT License.

