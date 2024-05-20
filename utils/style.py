import random


class Banner:
    def __init__(self):
        self.genders = ["His", "Her"]  # lol, should always be a list of these two
        self.animal_names = [
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
            "Bagheera",
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

    def print_name(self):
        print(f"{random.choice(self.genders)} name is {random.choice(self.animal_names)} :) \n")

    def home(self):
        print(r"""
    ____                      __                __        ____                         _                
   / __ \____ _      ______  / /___  ____ _____/ /____   / __ \_________ _____ _____  (_)___  ___  _____
  / / / / __ \ | /| / / __ \/ / __ \/ __ `/ __  / ___/  / / / / ___/ __ `/ __ `/ __ \/ /_  / / _ \/ ___/
 / /_/ / /_/ / |/ |/ / / / / / /_/ / /_/ / /_/ (__  )  / /_/ / /  / /_/ / /_/ / / / / / / /_/  __/ /    
/_____/\____/|__/|__/_/ /_/_/\____/\__,_/\__,_/____/   \____/_/   \__, /\__,_/_/ /_/_/ /___/\___/_/     
                                                                 /____/                                 
    """)
        print("\n")

    def rabbit(self):
        print("To say thanks, here's a rabbit for you!")
        print(r"""
             ,\
             \\\,_
              \` ,\
         __,.-" =__)
       ."        )
    ,_/   ,    \/\_
    \_|    )_-\ \_-`
      `-----` `--`
        """)
        print("\n")
        self.print_name()

    def horse(self):
        print("To say thanks, here's a horse for you!")
        print(r"""
            .''
  ._.-.___.' (`\
 //(        ( `'
'/ )\ ).__. ) 
' <' `\ ._/'\
   `   \     \
       """)
        print("\n")
        self.print_name()

    def dog(self):
        print("To say thanks, here's a dog for you!")
        print(r"""
  __      _
o'')}____//
 `_/      )
 (_(_/-(_/
        """)
        print("\n")
        self.print_name()

    def cat(self):
        print("To say thanks, here's a cat for you!")
        print(r"""
 /\_/\
( o.o )
 > ^ <
        """)
        print("\n")
        self.print_name()

    def elephant(self):
        print("To say thanks, here's a elephant for you!")
        print(r"""
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
        print("\n")

    def dolphin(self):
        print("To say thanks, here's a dolphin for you!")
        print(r"""
                ;'-. 
    `;-._        )  '---.._
      >  `-.__.-'          `'.__
     /_.-'-._         _,   ^ ---)
     `       `'------/_.'----```
                     `
        """)
        print("\n")
        self.print_name()

    def random_animal(self):
        random_int = random.randint(0, 5)
        match random_int:
            case 0:
                self.rabbit()
            case 1:
                self.horse()
            case 2:
                self.dog()
            case 3:
                self.cat()
            case 4:
                self.elephant()
            case 5:
                self.dolphin()
            case _:
                print("No animal for you!")
