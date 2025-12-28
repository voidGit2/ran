import os,sys,time,random 

code = '''
'''

red =  "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"
reset = "\033[0m"

def slow(text, delay=0.01):
   for c in text:
       sys.stdout.write(c)
       sys.stdout.flush()  

def logo():
   os.system('clear') or  os.system('cls')
   print(f'''
⠀⠀⠀{red}⣤⣴⣾⣿⣿⣿⣿⣿⣶⡄⠀{green}⠀⠀⠀⠀⠀⠀⠀⠀⣠⡄
⠀⠀{red}⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀{green}⢰⣦⣄⣀⣀⣠⣴⣾⣿⠃
⠀⠀{red}⢸⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀{green}⣼⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀{red}⣼⣿⡿⠿⠛⠻⠿⣿⣿⡇⠀⠀{green}⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀
⠀⠀{red}⠉⠀⠀⠀⢀⠀⠀⠀⠈⠁⠀{green}⢰⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀
⠀⠀{blue}⣠⣴⣶⣿⣿⣿⣷⣶⣤⠀⠀{yellow}⠀⠈⠉⠛⠛⠛⠉⠉⠀⠀⠀
⠀{blue}⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀{yellow}⣶⣦⣄⣀⣀⣀⣤⣤⣶⠀⠀
⠀{blue}⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀{yellow}⢀⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀
⠀{blue}⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀{yellow}⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
{blue}⢠⣿⡿⠿⠛⠉⠉⠉⠛⠿⠀⠀{yellow}⢸⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀
{blue}⠘⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{yellow}⠻⢿⣿⣿⣿⣿⣿⠿⠛ {reset}⠀⠀⠀''')

logo()
