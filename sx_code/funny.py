from typing import TypeVar

from pyfiglet import Figlet
from pyfiglet import print_figlet


f = Figlet(font='starwars', width=20)
Mascot = TypeVar('Mascot')


def funny(app_name: str) -> Mascot:
    mascot = """
                             .-'''-..' \                         
                   _______ .'       -   \                           
                 <<<<<<<< );__   ,,,_)   \                      
                    <<<<<<<<< ) ;C ./     \               
                      <<<<<< (.-'-.  )====_)_=======>      
                        <<<<< \    '''''''   )           
                        ;  <<<     .......__/       
                   .-'''         (         )          
                .-'              ;.       /            
               /  .-'     .     =  .     /
           _-''\+/         '. .'    .   /
        .-'  )  ;\          '''.     . /
       ;   .''''  `.       '    ;     (
       O -'        .'''       .'                      
                 .'   .-'''''`                   
                 'o-'                         """
    print("\033[033m", mascot, "\033[0m")
    print_figlet(app_name, colors='YELLOW:RESET')
    return mascot


def main(app_name: str):
    funny(app_name)
