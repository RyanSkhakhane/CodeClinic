from pickle import TRUE
import sys 
import colorama
from colorama import Fore, Back, Style

import time
colorama.init( autoreset=True)

####################################################
#                                                  #
#                                                  #
#                                                  #
####################################################

def get_input():
    commands = input('Waiting for command input ')
    return commands

commands_list = ["help","list_events","exit","create_event","login","update_event","volunteer_slot"]

def cc():
    print('\033[1;32;40mWTC Code Clinic version 0.0.1(Unstable)\nTo view valid commands type in help.')
    print('\033[39m')
    commands = ''
    while commands != 'exit':
        commands = get_input()
        if commands in commands_list:

            if commands.lower() == "exit":
                print("\033[4;31;40mClearing session data...")
                time.sleep(1)
                print(Fore.LIGHTGREEN_EX+ 'Session data cleared!')
                # time.sleep(3)
                print(Fore.RED+'Logging user out...')
                time.sleep(3)
                print(Fore.LIGHTGREEN_EX+'Success!')
                time.sleep(0.5)
                print(Fore.RED+"Exiting...")
                exit()
            elif commands.lower() == "login":
                print("\033[2;32;40mFeature comming soon!")
                print('\033[39m')
                continue
            
            elif commands.lower() == 'update_event':
                import update_event
                update_event
            
            elif commands.lower() == 'help':
                import info
                info
                
            elif commands.lower() == "list_events":
                import list_events
                list_events
          

            elif commands.lower() == "volunteer_slot":
                import volunteer_slot
                volunteer_slot

        else:
            print("Command not recognized ⚠️")
            
    


if __name__ == "__main__":
   
    cc()