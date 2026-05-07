import os
import time
import requests


URL = "http://localhost:8080"

def monitor():
    print("--- DevOps Self-Healing Monitor Started ---")
    print("Checking status every 10 seconds...")
    
    while True:
        try:
            response = requests.get(URL, timeout=5)
            if response.status_code == 200:
                print(f"[{time.ctime()}] ✅ Server is UP and Healthy!")
            else:
                print(f"[{time.ctime()}] ⚠️ Server Error: {response.status_code}")
        except Exception:
            print(f"[{time.ctime()}] ❌ ALERT: Server is DOWN!")
            print(f"[{time.ctime()}] ⚙️ Attempting to Restart Container: stest-container...")
            
            
            os.system("docker restart test-container")
            
            # Restart 
            time.sleep(5) 
        
        time.sleep(10) 

if __name__ == "__main__":
    monitor()
