import os
import random
import time

# customize density and speed of snowstorm
snow_density = 5
delay = 0.5

# List of snowflakes in unicode
snowflakes = ["❄", "❅", "❆", "❉", "❊", "❋", "❆", "❅", "❄", ".", "*"]

# get terminal size using os commands
term_size = os.get_terminal_size()

# define width and height of terminal
width = term_size.columns
height = term_size.lines

#print(width, height) testing

grid = []

# generate empty grid that is the size of the terminal
for i in range(height):
    grid.append([' '] * width)
    
def draw_grid():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print('\033[?25l') # Characters to remove cursor
    
    output = ''
    
    for row in grid:
        output += ''.join(row) + '\n'
        
    output = output.strip('\n')
    
    print(output, end='')

while True: 
    row = []
    
    for i in range(width):
        if random.random() < snow_density / 100:
            row.append(random.choice(snowflakes))
        else:
            row.append(' ')
            
    grid.insert(0, row)
    grid.pop()
    draw_grid()
    
    time.sleep(delay)