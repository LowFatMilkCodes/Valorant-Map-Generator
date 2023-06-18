#Imports
from time import sleep
import time
import sys
import os
import random
#Map List
def generate_random_map():
    maps = ['Lotus', 'Pearl', 'Fracture', 'Icebox', 'Haven', 'Split', 'Ascent', 'Bind', 'Breeze']
    random.shuffle(maps)
    return maps[0]
#Clear Prompt
def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')  
    else:
        _ = os.system('cls')  

        #Loading Animation
def loading_animation():
    animation = "|/-\\"
    for i in range(20):
        time.sleep(0.1)
        print(f"\rLoading... {animation[i % len(animation)]}", end="")
    print("\nLoading complete!")
    time.sleep(2)  # Wait for 2 seconds
    clear_screen()

loading_animation()

#Loading BAR
def loading_bar():
    duration = 3  # Duration of the loading process in seconds
    interval = 0.1  # Refresh interval for the loading animation
    
    total_ticks = int(duration / interval)
    bar_length = 40  # Length of the loading bar
    
    for tick in range(total_ticks):
        progress = (tick + 1) / total_ticks
        filled_length = int(bar_length * progress)
        empty_length = bar_length - filled_length
        
        bar = '█' * filled_length + '-' * empty_length
        
        print(f'\r[{bar}] {int(progress * 100)}%', end='', flush=True)
        
        time.sleep(interval)
    
    print("\nLoading complete!")




print('Welcome to LowFatMilk Codes')
print('---------------------------')
print('Valorant Map Generator')
sleep(1)
print('This was made for fun and has no real use :)')
sleep(2)
clear_screen()
loading_bar()


while True:
    
    clear_screen()
    random_map = generate_random_map()
    print(f"Generated Map: {random_map}")
    input("Press Enter to generate a new map...")
    clear_screen()
