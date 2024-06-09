import os
import pyfiglet

def run_PE(file):
    os.system("python3 Extract/PE_main.py {}".format(file))

def start():
    print(pyfiglet.figlet_format("Malware Detector"))
    print(" Welcome to antimalware detector PE scanner\n")
    folder_path = input("Enter the folder path: ")
    files = os.listdir(folder_path)
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            print("Scanning file:", file)
            run_PE(file_path)
        else:
            print("Skipping directory:", file)

start()
