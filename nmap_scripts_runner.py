import os
import subprocess
import sys
from datetime import datetime

def run_nmap_scripts(script_folder, target_ip, output_dir="nmap_output"):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get list of all .nse scripts in the folder
    script_files = [f for f in os.listdir(script_folder) if f.endswith('.nse')]
    
    if not script_files:
        print("No .nse scripts found in the specified folder!")
        return

    print(f"Found {len(script_files)} Nmap scripts to execute")
    
    # Run each script
    for script in script_files:
        script_path = os.path.join(script_folder, script)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(output_dir, f"{script}_{timestamp}.txt")
        
        # Construct Nmap command
        nmap_command = [
            "nmap",
            "--script", script_path,
            target_ip,
            "-oN", output_file
        ]
        
        print(f"\nRunning script: {script}")
        try:
            # Execute Nmap command
            result = subprocess.run(
                nmap_command,
                capture_output=True,
                text=True,
                check=True
            )
            print(f"Completed: {script}")
            print(f"Output saved to: {output_file}")
            
        except subprocess.CalledProcessError as e:
            print(f"Error running script {script}: {e}")
            print(f"Error output: {e.stderr}")
        except Exception as e:
            print(f"Unexpected error with script {script}: {str(e)}")

def main():
    # Check if correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python nmap_script_runner.py <script_folder> <target_ip>")
        sys.exit(1)
    
    script_folder = sys.argv[1]
    target_ip = sys.argv[2]
    
    # Validate folder exists
    if not os.path.isdir(script_folder):
        print(f"Error: {script_folder} is not a valid directory")
        sys.exit(1)
    
    run_nmap_scripts(script_folder, target_ip)

if __name__ == "__main__":
    main()
