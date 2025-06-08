from pythonosc import udp_client, dispatcher, osc_server
import threading

# QLab Connection Settings
ip = "192.168.2.240"  
port = 53000
client = udp_client.SimpleUDPClient(ip, port)

# Workspace and Cue Identification
workspace_id = "Workspace 1" 
cue_number = 5  

# Function to Handle Cue Information Response
def cue_info_handler(address, *args):
    cue_info = args[0]
    try:
        cue_name = cue_info['name']
        print(f"Cue Name: {cue_name}")
    except KeyError:
        print("Error: Invalid cue number or workspace ID")
    finally:
        # Stop the server after handling the response
        server.shutdown()

# Flag to indicate if the cue information has been received
cue_info_received = False

# Set Up OSC Dispatcher and Server
dispatcher = dispatcher.Dispatcher()
dispatcher.map(f"/workspace/{workspace_id}/cue/{cue_number}", cue_info_handler)

server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcher)

# Function to monitor if the cue information has been received
def monitor_cue_info():
    global cue_info_received
    while not cue_info_received:
        pass
    server.shutdown()

# Start monitoring thread
threading.Thread(target=monitor_cue_info).start()

# Send Request for Cue Information
client.send_message(f"/workspace/{workspace_id}/cue/{cue_number}", [])

# Start Listening for Responses
server.serve_forever() 
