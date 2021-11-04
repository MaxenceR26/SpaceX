from pycenter import center
from pystyle import Colorate, Colors
from sys import platform

from data.capsules import capsules_requests
from data.roadster import roadsters_requests
from data.spacex import info_spacex
from data.rockets import rockets_requests
from data.cores import cores_requests


# https://api.spacexdata.com/v3

def title():
    title_text = """
    

  ________  _______     __       ______    _______  ___  ___  
 /"       )|   __ "\   /""\     /" _  "\  /"     "||"  \/"  | 
(:   \___/ (. |__) :) /    \   (: ( \___)(: ______) \   \  /  
 \___  \   |:  ____/ /' /\  \   \/ \      \/    |    \\  \/   
  __/  \\  (|  /    //  __'  \  //  \ _   // ___)_   /\.  \   
 /" \   :)/|__/ \  /   /  \\  \(:   _) \ (:      "| /  \   \  
(_______/(_______)(___/    \___)\_______) \_______)|___/\___| 
                                                              


        - 1 : Look Capsules         - 4 : Info SpaceX
        - 2 : Look Rockets          - 5 : Look Cores
        - 3 : Look Roadsters    
                        
                        - 10 : Exit

    """

    print(Colorate.Horizontal(Colors.purple_to_blue, center(title_text)))
    
    

    

def clearScreen(os):
    """
    Function to clear terminal/cmd screen compatible with Linux, Mac and Windows
    """
    from subprocess import call
    if os == 'unix':
        command = 'clear'
    else:
        command = 'cls'
    call(command, shell=True)

def main():
    ## Cheking the system's OS
    if platform not in ('win32', 'cygwin'):
        os = 'unix'
    else:
        os = 'windows'

    clearScreen(os)
    title()
    while True:
        choose = int(input("SpaceX -> "))
        if choose == 1:
            clearScreen(os)
            title()
            capsules_requests()
            return_choice = input(Colorate.Color(Colors.purple, "Exit ? Y - N : "))
            if return_choice.lower()[0:1] == "y":
                exit()
            if return_choice.lower()[0:1] == "n":
                main()
        if choose == 2:
            clearScreen(os)
            title()
            rockets_requests()
            return_choice = input(Colorate.Color(Colors.purple, "Exit ? Y - N : "))
            if return_choice.lower()[0:1] == "y":
                exit()
            if return_choice.lower()[0:1] == "n":
                main()
        if choose == 3:
            clearScreen(os)
            title()
            roadsters_requests()
            return_choice = input(Colorate.Color(Colors.purple, "Exit ? Y - N : "))
            if return_choice.lower()[0:1] == "y":
                exit()
            if return_choice.lower()[0:1] == "n":
                main()
        if choose == 4:
            clearScreen(os)
            title()
            info_spacex()
            return_choice = input(Colorate.Color(Colors.purple, "Exit ? Y - N : "))
            if return_choice.lower()[0:1] == "y":
                exit()
            if return_choice.lower()[0:1] == "n":
                main()
        if choose == 5:
            clearScreen(os)
            title()
            cores_requests()
            return_choice = input(Colorate.Color(Colors.purple, "Exit ? Y - N : "))
            if return_choice.lower()[0:1] == "y":
                exit()
            if return_choice.lower()[0:1] == "n":
                main()
        if choose == 10:
            exit()


if __name__ == '__main__':
    main()
