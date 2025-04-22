import os, time
from colorama import Fore

PATH = os.path.dirname(os.path.abspath(__file__))
wordlist = os.path.join(PATH, "wordlist.txt")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def title():
    print('''
                _________    __    __  _______
               /_  __/   |  / /   / / / / ___/
                / / / /| | / /   / / / /\__ \ 
               / / / ___ |/ /___/ /_/ /___/ / 
              /_/ /_/  |_/_____/\____//____/
                   
                @Author: github.com/DevEzro
           @Repository: github.com/DevEzro/Talus       
    ''')

def info():
    print(f'''
        Talus is a wordlist generator that allows the user to create his own wordlists, based on
        asked info text by the him. Once the info is introduced, this tool creates a file that contains
        three permutations of this data, changing the order of the info. introduced.
        {time.sleep(0.5)}
            
        This tool offers various options:
        1. Generate wordlist: create the wordlist with the data provided by the user.
        2. About Talus: shows this information.
        3. Check updates: search for a new GitHub repository version, allowing the user to decide whether to update or not.
        4. Exit Talus: close Talus.
    ''')
    
def art():
    print('''
                    %%%*                                       
               *%@##%%%+==                           
              %@@@%###+=--==-=--==-======--====             
              +**+=++++==-======--======----===--===        
             ====+++*#++=+===========================       
             #**+=*++=+*+*+===========++---=====+++++       
            #%##%@@@@#+==*#*+++=-===-==+*===++==++++        
            ++*####**#%%%***==--====++==*#++*+=++++         
           #@%#****+====++#%#*++==+=+++++++++**+**=         
           %@@@%%%*===++*+*#%*+*+**+**#***+***++***         
          ===+++==+%@%%+=*%%@%##@##%%****#+==+*#====*       
         +==--======%@@@@#+#%%%%@@@#+++**##++++++*+++*      
      +*+======--==+%@@@@%%##***#*+=++++****++++++*+=+      
   +++++======+++=*%%%%@@%@%#*+=+*##%@%%@@%%%#*%%++=====    
 ++****#+==--==++#@@@@@@%%@@@@%%%%%%%%%%%%#%@%%#**+======   
 **++++#++++===+++=*@@@@%@@@%%%%%%%%#%%    %#***+++======-  
 ##*+**=+++++**#*+**#@@@@@@@@@@@%%%       ##*#%@%*==++===-- 
 %%%*#++**++*+*+++++%@@@@@@@@@@@@@%%      %%#***=---======- 
 @@@#+++**+=+*+++++*@@%%     @@@@@@%       %#++++#*+++***+= 
  %%***+++++*+++**+*@         @@@%#%       %%#*##%%%%%%%##  
   %#*+*****+*####++*                                       
      ##%%                                                  
    ''')

def ops(option):
    clear_screen()
    if option == "1":
        w1 = input("[-] Enter the first data, like a name: ")
        w2 = input("[-] Enter the second data, like a date: ")
        w3 = input("[-] Enter the third data, like special characters: ")
        fw1 = w1+w2+w3
        fw2 = w1+w3+w2
        fw3 = w2+w1+w3
        fw4 = w2+w3+w1
        fw5 = w3+w1+w2
        fw6 = w3+w2+w1
        with open(wordlist, "w") as f:
            f.write(fw1 + "\n")
            f.write(fw2 + "\n")
            f.write(fw3 + "\n")
            f.write(fw4 + "\n")
            f.write(fw5 + "\n")
            f.write(fw6 + "\n")
        print(f'''
            {Fore.GREEN}
            [+] Wordlist created successfully!
            {Fore.RESET}
        ''')
        print("These are the permutations of the data you introduced:")
        print(f'''
            {Fore.GREEN}
            [+] {fw1}
            [+] {fw2}
            [+] {fw3}
            [+] {fw4}
            [+] {fw5}
            [+] {fw6}
        ''')
        print_menu()
    elif option == "2":
        clear_screen()
        title()
        time.sleep(0.5)
        art()
        time.sleep(0.5)
        info()
        print_menu()
    elif option == "3":
        clear_screen()
        print("In progress...")
        print_menu()

def print_menu():
    print(Fore.CYAN +'''
 ****************************      
 *   [1] Generate wordlist  *
 *   [2] About Talus        *
 *   [3] Check updates      *
 *   [0] Exit Talus         *
 ****************************
    ''' + Fore.RESET)
    option = input(Fore.YELLOW + "[-] Select an option above: " + Fore.RESET)
    if option == "0":
        clear_screen()
        print("\nThanks for using Talus!\n")
        exit()
    else:
        ops(option)
    
title()
time.sleep(0.5)
art()
time.sleep(0.5)
print_menu()