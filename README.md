
# Nmap Automated Scripts Runner

A Python-based tool designed to automate the execution of Nmap scripts (`.nse` files) against a specified target IP address. This repository includes a Python script and a collection of Nmap scripts to perform security scans efficiently.

## Overview

This tool simplifies the process of running multiple Nmap scripts stored in a folder by automating the execution and saving the results with timestamps for easy reference. It is ideal for security researchers, penetration testers, and system administrators who need to perform network scans with custom scripts.

## Prerequisites

Before using this tool, ensure the following are installed and configured on your system:

- **Python 3.x**: Verify installation by running `python3 --version` or `python --version` in your terminal.
- **Nmap**: Install Nmap, the network scanning tool, which is required to execute the scripts.
  - On Ubuntu/Debian: `sudo apt-get update && sudo apt-get install nmap`
  - On macOS (with Homebrew): `brew install nmap`
  - On Windows: Download and install from [nmap.org](https://nmap.org/download.html)
- **Root/Admin Privileges**: Some Nmap scans require elevated privileges. Use `sudo` on Linux/macOS or run as Administrator on Windows.
- **Internet Connection**: Required to download Nmap if not already installed.

## Installation

1. **Clone the Repository**:
   Open a terminal and run the following commands:
```bash
   git clone https://github.com/atmajkhatavkar404/nmap_scripts_runner.git
   cd nmap-script-runner
   ```

2. **Verify Contents**:
   - The repository includes `nmap_scripts_runner.py` and a folder `nmap_automated_scripts` containing `.nse` files.
   - Unzip nmap_automated_scripts
   - Ensure the `nmap_automated_scripts` folder is present and contains valid Nmap scripts.


## Usage

### Running the Script

Execute the script by providing the path to the scripts folder and the target IP address:

python3 nmap_script_runner.py /path/to/nmapscripts 192.168.1.1

- **Example**:
- Without Specifying a Port (Scans all ports):
  ```bash
  python3 nmap_script_runner.py /path/to/nmapscripts 192.168.1.1
  ```
  - Replace `192.168.1.1` with the IP address or hostname of the target you have permission to scan.
  - 
  - With a Specific Port (Scans only the specified port):
```bash
  python3 nmap_script_runner.py /path/to/nmapscripts 192.168.1.1 80
  ```
  This will run all scripts against the target IP, but only on port 80.
    Replace 80 with any valid port number (e.g., 443, 22, etc.) you want to scan.

### Command-Line Arguments
- `<script_folder>`: Path to the folder containing `.nse` files (e.g., `./nmap_automated_scripts`).
- `<target_ip>`: The IP address or hostname to scan (e.g., `192.168.1.1` or `example.com`).

### Output
- Results are saved in a folder named `nmap_output` created in the same directory as the script.
- Each script’s output is stored in a timestamped `.txt` file (e.g., `scriptname_20250621_092800.txt`).
- Progress and any errors are displayed in the terminal.

## Features
- Automatically detects and runs all `.nse` files in the specified folder.
- Creates a dedicated `nmap_output` directory for organized results.
- Handles errors gracefully and continues with the next script if one fails.
- Uses timestamps to avoid overwriting previous scan results.

## Troubleshooting

- **"No .nse scripts found"**: Ensure the `nmap_automated_scripts` folder contains valid `.nse` files. Check the folder path and file extensions.
- **Permission Denied**: Run the script with `sudo` or as an Administrator if Nmap requires elevated privileges.
- **Nmap Not Found**: Verify Nmap is installed and accessible in your system’s PATH.
- **Invalid Target IP**: Ensure the target IP is correct and you have permission to scan it. Unauthorized scanning is illegal.
- **Errors During Execution**: Check the terminal output for specific error messages and consult Nmap documentation or the script’s error logs.

