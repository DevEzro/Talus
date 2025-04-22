import os, time, subprocess
from colorama import Fore

PATH = os.path.dirname(os.path.abspath(__file__))
wordlist = os.path.join(PATH, "wordlist.txt")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def title():
    print(r'''
                _________    __    __  _______
               /_  __/   |  / /   / / / / ___/
                / / / /| | / /   / / / /\__ \ 
               / / / ___ |/ /___/ /_/ /___/ / 
              /_/ /_/  |_/_____/\____//____/
                   
                @Author: github.com/DevEzro
           @Repository: github.com/DevEzro/Talus       
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

def permutations(): # 1. GENERATE WORDLIST
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
        ✅ Wordlist created successfully!
        {Fore.RESET}
    ''')
    print("These are the permutations of the data you introduced:")
    print(f'''
        {Fore.GREEN}
        ✅ {fw1}
        ✅ {fw2}
        ✅ {fw3}
        ✅ {fw4}
        ✅ {fw5}
        ✅ {fw6}
    ''')

def info(): # 2. ABOUT TALUS
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
    
def check_updates(): # 3. CHECK UPDATES
    try:
        subprocess.run(["git", "fetch", "origin"], check=True)
        
        local = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip()
        remote = subprocess.check_output(["git", "rev-parse", "origin/main"]).strip()
        
        if local != remote:
            print(f"{Fore.CYAN}⭐ New available update.{Fore.RESET}")
            answer = input("Do you want to install the update? (y/n): ").strip().lower()
            if answer == "y":
                subprocess.run(["git", "pull", "origin", "main"], check=True)
                print(f"{Fore.GREEN}✅ Repositorio actualizado.{Fore.RESET}")
            else:
                print(f"{Fore.RED}❌ Actualización cancelada.{Fore.RESET}")
        else:
            print(f"{Fore.CYAN}🆗 No hay actualizaciones disponibles.{Fore.RESET}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}❌ Error al comprobar actualizaciones: {e}{Fore.RESET}")

def print_menu(): # 0. EXIT TALUS
    print(Fore.CYAN +'''
 ****************************      
 *   [1] Generate wordlist  *
 *   [2] About Talus        *
 *   [3] Check updates      *
 *   [0] Exit Talus         *
 ****************************
    ''' + Fore.RESET)
    option = input(Fore.YELLOW + "[-] Select an option above: " + Fore.RESET)
    if option == "0": # Exit
        clear_screen()
        print("\nThanks for using Talus!\n")
        exit()
    elif option >= "1" and option <= "3":
        ops(option)
    else:
        print(f"{Fore.RED}\n❌ Invalid option.{Fore.RESET}")
        print(f"{Fore.RED}⚠️  You must select an option between 0 and 3")
        print_menu()
        
def ops(option):
    clear_screen() # Generate wordlist
    if option == "1":
        permutations()
        print_menu()
    elif option == "2": # Info
        clear_screen()
        title()
        time.sleep(0.5)
        art()
        time.sleep(0.5)
        info()
        print_menu()
    elif option == "3": # Check updates
        clear_screen()
        check_updates()
        print_menu()


title()
time.sleep(0.5)
art()
time.sleep(0.5)
print_menu()