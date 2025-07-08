import os
os.environ['TERM'] = 'xterm'
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
