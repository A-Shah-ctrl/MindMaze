import pygame
import time
import random
from pylsl import StreamInlet, resolve_byprop

LSL_STREAM = ''
STREAM_TYPE = 'Markers' # or 'Triggers'

def get_data():
    # Find the stream by type
    print("Finding LSL stream '{}'...".format(STREAM_TYPE))
    streams = resolve_byprop('type', STREAM_TYPE, timeout=5)
    # Find stream by name
    if not streams:
        print("Stream of type '{}' not found. Trying name...".format(STREAM_TYPE))
        streams = resolve_byprop('name', LSL_STREAM, timeout=5)
        if not streams:
            print("Error: Couldn' find stream :(")
            exit()

    # Connecting it to stream
    stream_info = streams[0]
    inlet = StreamInlet(stream_info)
    
    print(f"Successfully connected to stream: {stream_info.name()} ({stream_info.type()})")

    while True:
        sample, timestamp = inlet.pull_sample(timeout=0.0) # no blocking - keeps pulling samples

        if sample:
            print(f"[{timestamp:.4f}] BCI Command Received: {sample}")
            value = sample[0] # Classification value
            if value == 'L':
                chosen_key = pygame.K_LEFT
            elif value == 'R':
                chosen_key = pygame.K_RIGHT
            elif value == 'U':
                chosen_key = pygame.K_UP
            else:
                chosen_key = pygame.K_DOWN

            event = pygame.event.Event(pygame.KEYDOWN, key=chosen_key)
            pygame.event.post(event)  