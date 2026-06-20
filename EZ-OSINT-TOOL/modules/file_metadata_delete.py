import os
import time

def run():
    print("\n=== File Metadata Deleter ===")
    path = input("Enter file path: ").strip()

    if not os.path.exists(path):
        print("File not found.")
        return

    try:
        current_time = time.time()
        os.utime(path, (current_time, current_time))
        print("\nMetadata cleared successfully!")
    except Exception as e:
        print(f"Error: {e}")
