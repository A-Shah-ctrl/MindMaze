import pygame
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 1000       
BUFFER_SIZE = 1024   

def run_udp_listener():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((UDP_IP, UDP_PORT))
        print(f"Listening for UDP data on {UDP_IP}:{UDP_PORT}...")

        received_data = []
        while True:
            data, addr = sock.recvfrom(BUFFER_SIZE)
            message = data.decode('utf-8')
            print(f"Received from {addr}: {message}")
            received_data.append(message)

    except KeyboardInterrupt:
        print("\nStopping UDP listener.")
        
    except Exception as e:
        print(f"\nAn error occurred: {e}")

    if 'sock' in locals():
        sock.close()
        
    print("\nFinal P300 outputs collected:")
    for item in received_data:
        print(item)


# LSL_STREAM = ''
# STREAM_TYPE = 'Markers' # or 'Triggers'

# def get_data():
#     # Find the stream by type
#     print("Finding LSL stream '{}'...".format(STREAM_TYPE))
#     streams = resolve_byprop('type', STREAM_TYPE, timeout=5)
#     # Find stream by name
#     if not streams:
#         print("Stream of type '{}' not found. Trying name...".format(STREAM_TYPE))
#         streams = resolve_byprop('name', LSL_STREAM, timeout=5)
#         if not streams:
#             print("Error: Couldn' find stream :(")
#             exit()

#     # Connecting it to stream
#     stream_info = streams[0]
#     inlet = StreamInlet(stream_info)
    
#     print(f"Successfully connected to stream: {stream_info.name()} ({stream_info.type()})")

#     while True:
#         sample, timestamp = inlet.pull_sample(timeout=0.0) # no blocking - keeps pulling samples

#         if sample:
#             print(f"[{timestamp:.4f}] BCI Command Received: {sample}")
#             value = sample[0] # Classification value
#             if value == 'L':
#                 chosen_key = pygame.K_LEFT
#             elif value == 'R':
#                 chosen_key = pygame.K_RIGHT
#             elif value == 'U':
#                 chosen_key = pygame.K_UP
#             else:
#                 chosen_key = pygame.K_DOWN

#             event = pygame.event.Event(pygame.KEYDOWN, key=chosen_key)
#             pygame.event.post(event)  