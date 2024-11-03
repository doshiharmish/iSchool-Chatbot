import subprocess
import sys
import os
import streamlit as st

#this function is used to verify and install all the dependencies:
def install_requirements():
    # Check if requirements.txt exists
    if os.path.isfile("requirements.txt"):
        try:
            # Install packages listed in requirements.txt, skipping already installed ones
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "--quiet", "--no-warn-script-location"])
            print("All required packages are installed.")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred during installation: {e}")
    else:
        print("requirements.txt file not found!")

# Call the function at the start of your script

install_requirements()


st.write("Hello World.")