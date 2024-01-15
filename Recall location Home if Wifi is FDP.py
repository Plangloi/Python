import subprocess
import time

# Execute the networksetup command to turn on Wi-Fi
subprocess.run(['networksetup', '-setairportpower', 'en0', 'on'])

#Time to find all Wifi
time.sleep(5)


# Define your desired network name or allowed network names
desired_network = 'FDP Power'
allowed_networks = ['FDP 2', 'FDP Power Ubi']

# Get the current Wi-Fi network name
result = subprocess.run(['networksetup', '-getairportnetwork', 'en0'], capture_output=True, text=True)
output = result.stdout.strip()

# Extract the network name from the output
network_name = output.split(': ')[-1]

# Compare the network name with the desired value or allowed list
if network_name == desired_network or network_name in allowed_networks:
    # Set the desired network location
    new_location = "Home"

    # Execute the networksetup command to change the network location
    subprocess.run(['networksetup', '-switchtolocation', new_location])

    print(f"Successfully changed the network location to '{new_location}' and turned on Wi-Fi.")
else:
    print("You are not on the desired network.")
