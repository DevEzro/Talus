from colorama import Fore
import time
# from pathlib import Path

#region Constants
BLUE = Fore.BLUE
RED = Fore.RED
GREEN = Fore.GREEN
RESET = Fore.RESET
#endregion

#region Functions
def title():
    print(
    BLUE+'''
    ::::::::::: :::     :::       :::    :::  :::::::: 
        :+:   :+: :+:   :+:       :+:    :+: :+:    :+: 
        +:+  +:+   +:+  +:+       +:+    +:+ +:+         
        +#+ +#++:++#++: +#+       +#+    +:+ +#++:++#++   
        +#+ +#+     +#+ +#+       +#+    +#+        +#+    
        #+# #+#     #+# #+#       #+#    #+# #+#    #+#     
        ### ###     ### ########## ########   ########
    ''')
    time.sleep(1)
    print('''             
                    WORDLIST GENERATOR
    '''
    +RESET)
    
    time.sleep(1)
    
    print(RED+
    '''             
                        ++========-        
                    ******+=+++++===        
                ++***=*#**#+=++==-=-        
            ####*+++*###+=+++=++*+==        
        ###*+**###***#**===++=====--      
        %######=+##**##+*+++==++=##**+    
        #######*####*#*#*++***++####*+    
    #*################*+=++** %###*++==  
    ##*=+####%  ############%     ####***+= 
    #########% ############       #####***==
    ########%  %###%    #*+*#    %###****+==
    %%##%%%    %%%      %%       %#%#+##** 
    ''')
    
    time.sleep(1)
    print('''
    @DevEzro
    github.com/DevEzro
    github.com/DevEzro/Talus
    '''
    + RESET)

def print_menu():
    print(''' 
    OPTIONS:
    1. Generate wordlist
    0. Exit      
    ''')

def generate_wordlist():
    print("[-] Introduce a FILE NAME: ")
    filename = input("[+] ")
    print("[-] Introduce a WORD: ")    
    name = input("[+] ")
    print("[-] Introduce a NUMBER: ")    
    date = input("[+] ")
    print("[-] Introduce A/SPECIAL CHARACTER/S: ")    
    character = input("[+] ")
        
    print("\nGenerating "+BLUE+filename+".txt"+RESET+" wordlist file...")
    for i in range (3):
        if i < 1:
            string1 = name+date+character
        elif i < 2:
            string2 = date+character+name
        else:
            string3 = character+name+date
    with open(filename+".txt", "w") as file:
        file.write(string1+"\n")
        file.write(string2+"\n")
        file.write(string3)
        
    print("\n::::::::::::::GENERATED WORDLIST::::::::::::::::::::")        
    print("Wordlist generated successfully.")
    print(BLUE+"[+] File name: "+RESET, filename+".txt")
    print(GREEN+"[+] First word: "+RESET, string1)    
    print(GREEN+"[+] Second word: "+RESET, string2)    
    print(GREEN+"[+] Third word: "+RESET, string3)
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::")

def end():
    print(BLUE+"Exiting..."+RESET)
    exit()
        
def try_again():
    print(RED+"Invalid option. Try again."+RESET)
        
def menu():
    option = ''
    while option != '0':
        print_menu()
        option = input("Enter an option: ")

        if option == '1':
            generate_wordlist()
        if option == '0':
            end()
        if option != '1' and option != '0':
            try_again()
#endregion

#region Main
title()
menu()
#endregion