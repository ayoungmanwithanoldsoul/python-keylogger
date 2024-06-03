import subprocess
import sys

def install_requirements():
    try:
        # Open the requirements.txt file and read the dependencies
        with open('requirements.txt', 'r') as file:
            packages = file.read().splitlines()
        
        # Install each package using pip
        for package in packages:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        print("All dependencies installed successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    install_requirements()
