from pycenter import center
from pystyle import Colorate, Colors
from os import system

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


def main():
    system("cls")
    title()
    while True:
        choose = int(input("SpaceX -> "))
        if choose == 1:
            system("cls")
            title()
            capsules_requests()
            return_choice = input(Colorate.Color(Colors.purple, "Exit ? Y - N : "))
            if return_choice.lower()[0:1] == "y":
                exit()
            if return_choice.lower()[0:1] == "n":
                main()
        if choose == 2:
            system("cls")
            title()
            rockets_requests()
            return_choice = input(Colorate.Color(Colors.purple, "Exit ? Y - N : "))
            if return_choice.lower()[0:1] == "y":
                break
            if return_choice.lower()[0:1] == "n":
                main()
        if choose == 3:
            system("cls")
            title()
            roadsters_requests()
            return_choice = input(Colorate.Color(Colors.purple, "Exit ? Y - N : "))
            if return_choice.lower()[0:1] == "y":
                break
            if return_choice.lower()[0:1] == "n":
                main()
        if choose == 4:
            system("cls")
            title()
            info_spacex()
            return_choice = input(Colorate.Color(Colors.purple, "Exit ? Y - N : "))
            if return_choice.lower()[0:1] == "y":
                break
            if return_choice.lower()[0:1] == "n":
                main()
        if choose == 5:
            system("cls")
            title()
            cores_requests()
            return_choice = input(Colorate.Color(Colors.purple, "Exit ? Y - N : "))
            if return_choice.lower()[0:1] == "y":
                break
            if return_choice.lower()[0:1] == "n":
                main()
        if choose == 10:
            break


main()
