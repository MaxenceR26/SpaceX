from pystyle import Colorate, Colors, Center, System, Anime
from sys import platform

from data.Ships import ships_requests
from data.capsules import capsules_requests
from data.history import history_requests
from data.landingpads import landspad_requests
from data.missions import missions_requests
from data.payloads import payloads_requests
from data.roadster import roadsters_requests
from data.spacex import info_spacex
from data.rockets import rockets_requests
from data.cores import cores_requests

# https://api.spacexdata.com/v3

logo = """                                                   -- __
                                                 ~ (@)  ~~~---_
                                               {     `-_~,,,,,,)
                                               {    (_  ',
                                                ~    . = _',
                                                 ~    '.  =-'
                                                   ~     :
.                                                -~     ('');
'.                                         --~        \  \ ;
  '.-_                                   -~            \  \;      _-=,.
     -~- _                          -~                 {  '---- _'-=,.
       ~- _~-  _              _ -~                     ~---------=,.`
            ~-  ~~-----~~~~~~       .+++~~~~~~~~-__   /
                ~-   __            {   -     +   }   /
                         ~- ______{_    _ -=\ / /_ ~
                             :      ~--~    // /         ..-
                             :   / /      // /         ((
                             :  / /      {   `-------,. ))
                             :   /        ''=--------. }o
                .=._________,'  )                     ))
                )  _________ -''                     ~~
               / /  _ _
              (_.-.'O'-'.


                    By Kijusu#2614 | IG : _maxence26
"""


def initialization():
    System.Size(180, 50)
    System.Title("SpaceX")
    Anime.Fade(text=Center.Center(logo), color=Colors.purple_to_blue, mode=Colorate.Vertical, enter=True)


def title():
    title_text = """
    

  ________  _______     __       ______    _______  ___  ___  
 /"       )|   __ "\   /""\     /" _  "\  /"     "||"  \/"  | 
(:   \___/ (. |__) :) /    \   (: ( \___)(: ______) \   \  /  
 \___  \   |:  ____/ /' /\  \   \/ \      \/    |    \\  \/   
  __/  \\  (|  /    //  __'  \  //  \ _   // ___)_   /\.  \   
 /" \   :)/|__/ \  /   /  \\  \(:   _) \ (:      "| /  \   \  
(_______/(_______)(___/    \___)\_______) \_______)|___/\___| 
                                                              


        - 1 : Look Capsules         - 6 : Info SpaceX
        - 2 : Look Rockets          - 7 : Look Cores
        - 3 : Look Roadsters        - 8 : Look Ships
        - 4 : Look Payloads         - 9 : Look Missions
        - 5 : Look Landing Pads     - 10 : Look History

                        
                        - 11 : Exit

    """

    print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(title_text)))


def switch(number, system):
    numbers = {
        1: capsules_requests,
        2: rockets_requests,
        3: roadsters_requests,
        4: payloads_requests,
        5: landspad_requests,
        6: info_spacex,
        7: cores_requests,
        8: ships_requests,
        9: missions_requests,
        10: history_requests,
        11: exit,

    }
    clearScreen(system)
    title()
    numbers.get(number)()
    yes_or_no = input("Exit ? ( Y - N ) -> ")
    if yes_or_no.lower()[0:1] == 'y':
        exit()
    elif yes_or_no.lower()[0:1] == 'n':
        main()


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
    # Checking the system's OS
    if platform not in ('win32', 'cygwin'):
        os = 'unix'
    else:
        os = 'windows'

    clearScreen(os)
    title()
    while True:
        choose = int(input("SpaceX -> "))
        switch(number=choose, system=os)
        break


if __name__ == '__main__':
    initialization()
    main()
