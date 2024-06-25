import random
import argparse
from colorama import (
    Fore,
    Back,
    Style
)


class Banner:
    def __init__(self, args: argparse.Namespace) -> None:
        self.args: argparse.Namespace = args
        self.genders: list = [
            f"{Fore.BLUE}His{Style.RESET_ALL}",
            f"{Fore.MAGENTA}Her{Style.RESET_ALL}"
        ]  # lol, should always be a list of these two

        self.animal_names: list = [
            "Simba",
            "Mufasa",
            "Baloo",
            "Bambi",
            "Thumper",
            "Tramp",
            "Copper",
            "Nemo",
            "Marlin",
            "Pumbaa",
            "Barrera",
            "Kovu",
            "Shere Khan",
            "Tigger",
            "Winnie",
            "Chip",
            "Dale",
            "Mushu",
            "Sebastian",
            "Flounder"
        ]

    def print_animal_name(self) -> None:
        print(f"{random.choice(self.genders)} name is {random.choice(self.animal_names)} :) \n")

    def print_home(self) -> None:
        print(Fore.MAGENTA + r"""
    ____                      __                __        ____                         _
   / __ \____ _      ______  / /___  ____ _____/ /____   / __ \_________ _____ _____  (_)___  ___  _____
  / / / / __ \ | /| / / __ \/ / __ \/ __ `/ __  / ___/  / / / / ___/ __ `/ __ `/ __ \/ /_  / / _ \/ ___/
 / /_/ / /_/ / |/ |/ / / / / / /_/ / /_/ / /_/ (__  )  / /_/ / /  / /_/ / /_/ / / / / / / /_/  __/ /
/_____/\____/|__/|__/_/ /_/_/\____/\__,_/\__,_/____/   \____/_/   \__, /\__,_/_/ /_/_/ /___/\___/_/
                                                                 /____/

        """)

    def print_rabbit(self) -> None:
        print("To say thanks, here's a rabbit for you!")
        print(Fore.MAGENTA + r"""
             ,\
             \\\,_
              \` ,\
         __,.-" =__)
       ."        )
    ,_/   ,    \/\_
    \_|    )_-\ \_-`
      `-----` `--`

        """)
        self.print_animal_name()

    def print_horse(self) -> None:
        print("To say thanks, here's a horse for you!")
        print(Fore.MAGENTA + r"""
            .''
  ._.-.___.' (`\
 //(        ( `'
'/ )\ ).__. ) 
' <' `\ ._/'\
   `   \     \

        """)
        self.print_animal_name()

    def print_dog(self) -> None:
        print("To say thanks, here's a dog for you!")
        print(Fore.MAGENTA + r"""
  __      _
o'')}____//
 `_/      )
 (_(_/-(_/
        """)
        self.print_animal_name()

    def print_cat(self):
        print("To say thanks, here's a cat for you!")
        print(Fore.MAGENTA + r"""
 /\_/\
( o.o )
 > ^ <

        """)
        self.print_animal_name()

    def print_elephant(self) -> None:
        print("To say thanks, here's a elephant for you!")
        print(Fore.MAGENTA + r"""
     _.-- ,.--.
   .'   .'    /
   | @       |'..--------._
  /      \._/              '.
 /  .-.-                     \
(  /    \                     \
 \\      '.                  | #
  \\       \   -.           /
   :\       |    )._____.'   \
    "       |   /  \  |  \    )
            |   |./'  :__ \.-'
            '--'

        """)
        self.print_animal_name()

    def print_dolphin(self) -> None:
        print("To say thanks, here's a dolphin for you!")
        print(Fore.MAGENTA + r"""
                ;'-.
    `;-._        )  '---.._
      >  `-.__.-'          `'.__
     /_.-'-._         _,   ^ ---)
     `       `'------/_.'----```
                     `

        """)
        self.print_animal_name()

    def random_animal(self):
        random_int = random.randint(0, 5)
        match random_int:
            case 0:
                self.print_rabbit()
            case 1:
                self.print_horse()
            case 2:
                self.print_dog()
            case 3:
                self.print_cat()
            case 4:
                self.print_elephant()
            case 5:
                self.print_dolphin()
            case _:
                print("No animal for you!")
