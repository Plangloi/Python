import subprocess
import time

time_hold = input("Time to run ?/(Minute) ")

try:
    # Start the server process
    server_process = subprocess.Popen(["python3", "-m", "http.server", "8080"])
    
    # Wait for the specified time
    time.sleep(float(time_hold) * 60)
    
    print(f"Time over after {time_hold} minutes!")
    server_process.terminate()  # Stop the server
except KeyboardInterrupt:
    print("\nServer stopped by user")
    server_process.terminate()
except ValueError:
    print("Please enter a valid number for minutes")
