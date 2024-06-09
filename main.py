import os
import pyfiglet
import argparse
import warnings
from concurrent.futures import ThreadPoolExecutor, as_completed

# Suppress specific sklearn warnings about model unpickling
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

def run_PE(file):
    os.system(f"python3 Extract/PE_main.py {file}")

def start(folder_path):
    print(pyfiglet.figlet_format("Malware Detector"))
    print(" Welcome to antimalware detector PE scanner\n")
    files = os.listdir(folder_path)
    
    # Use ThreadPoolExecutor to run scans in parallel
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(run_PE, os.path.join(folder_path, file)): file for file in files if os.path.isfile(os.path.join(folder_path, file))}
        
        try:
            for future in as_completed(futures):
                file = futures[future]
                try:
                    future.result()
                    print(f"Completed scanning file: {file}")
                except Exception as exc:
                    print(f"File {file} generated an exception: {exc}")
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt detected, shutting down...")
            executor.shutdown(wait=False)
            print("Shutdown complete. Exiting program.")
            return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Antimalware PE scanner")
    parser.add_argument("folder_path", help="The path to the folder containing files to scan")
    args = parser.parse_args()
    start(args.folder_path)
