import sys
from pythonosc import udp_client


# 1. OSC Configuration
osc_ip = "192.168.2.240"  # Replace with the actual IP of your OSC receiver
osc_ip2 = "192.168.2.112"
osc_port = 53000       # Replace with the actual port of your OSC receiver
osc_client = udp_client.SimpleUDPClient(osc_ip, osc_port)
osc_client2 = udp_client.SimpleUDPClient(osc_ip2, osc_port)

# 2. Command Line Argument Handling
def play_cue():
    # osc_client.send_message(f"/cue/{cue_num}/go", 1)
    # osc_client2.send_message(f"/cue/{cue_num}/go", 1)
    osc_client.send_message(f"/cue/{cue_num}/go", 1)
    osc_client2.send_message(f"/cue/{cue_num}/go", 1)
    # osc_client.send_message("/runningCues/shallow", 1)


    print()
    print("*" * 50)
    print(f"Playing cue {cue_num}")
     
def stop_cue():
    osc_client.send_message(f"/cue/{cue_num}/panic", 1)
    osc_client2.send_message(f"/cue/{cue_num}/panic", 1)

    print()
    print("*" * 50)
    print(f"Stopping cue {cue_num}...")

def panic_all():
    osc_client.send_message("/panic", 1)
    osc_client2.send_message("/panic", 1)

    print()
    print("*" * 50)
    print("Stopping all cue...")



while True :
    cue_num = input("Enter the cue number: ")

    case = input("Enter : \n (P) for play \n (S) for stop \n (QQ) to panic all \n (Q) to quit ").lower()
    if case == "p":
        play_cue()

    elif case == "s":
        stop_cue()

    elif case == "qq":
        panic_all()
    
    elif case == "q":
        break
    else:
        print("Invalid input. Please enter 'p' for play or 's' for stop.")