import pygame
import socket
import re

UDP_IP = "127.0.0.1"
UDP_PORT = 8000       
BUFFER_SIZE = 65536
CONTROLS = {
            'left': 'L',
            'right': 'R',
            'up': 'T',
            'down': 'D',
            'empty': 'X'
            }   

def run_udp_listener():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((UDP_IP, UDP_PORT))
        print(f"Listening for UDP data on {UDP_IP}:{UDP_PORT}...")

        received_data = []
        while True:
            data, addr = sock.recvfrom(BUFFER_SIZE)
                    # Try decoding the binary data as UTF-8 and extract readable words
            try:
                text = data.decode('utf-8', errors='ignore')  # Ignore invalid characters
                # Optional: print raw decoded string for debugging
                #print(f"[Raw] {text}")
                #print(data)
                
                # Use regex to look for keywords
                match = re.search(r"\b(Left|Right|Up|Down|Empty)\b", text, re.IGNORECASE)
                if match:
                    value = match.group(1).lower()
                    print(value)
                    if value is None:
                        chosen_key = pygame.K_UP
                    else:
                        value = CONTROLS[value]
                        if value == 'L':
                            chosen_key = pygame.K_LEFT
                            event = pygame.event.Event(pygame.KEYDOWN, key=chosen_key)
                            pygame.event.post(event)
                        elif value == 'R':
                            chosen_key = pygame.K_RIGHT
                            event = pygame.event.Event(pygame.KEYDOWN, key=chosen_key)
                            pygame.event.post(event)
                        elif value == 'D':
                            chosen_key = pygame.K_DOWN
                            event = pygame.event.Event(pygame.KEYDOWN, key=chosen_key)
                            pygame.event.post(event)
                        elif value == "X":
                            pass

            except Exception as e:
                print(f"Error decoding: {e}")
            
            #message = data.decode('utf-8')
            #print(data)
            #print(f"Received from {addr}: {message}")
            #received_data.append(message)

    except KeyboardInterrupt:
        print("\nStopping UDP listener.")
        
    except Exception as e:
        print(f"\nAn error occurred: {e}")

    if 'sock' in locals():
        sock.close()

#if __name__ == "__main__":
#    run_udp_listener()