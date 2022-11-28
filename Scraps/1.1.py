import random
from time import sleep

#Story
intro_path = 'C:\\Users\\cobax\\OneDrive\\Desktop\\CPTR 226\\labs\\Lab 10\\Files\\SCRPS\\intro.txt'
#EPILOGUE
bus_stop_path = 'C:\\Users\\cobax\\OneDrive\\Desktop\\CPTR 226\\labs\\Lab 10\\Files\\SCRPS\\bus stop.txt'

#CASEY'S MENUS
shop_menu_path = 'C:\\Users\\cobax\\OneDrive\\Desktop\\CPTR 226\\labs\\Lab 10\\Files\\SCRPS\\shop menu.txt'
shop_wpns_path = 'C:\\Users\\cobax\\OneDrive\\Desktop\\CPTR 226\\labs\\Lab 10\\Files\\SCRPS\\shop weapons.txt'
shop_food_path = 'C:\\Users\\cobax\\OneDrive\\Desktop\\CPTR 226\\labs\\Lab 10\\Files\\SCRPS\\shop food.txt'
shop_armr_path = 'C:\\Users\\cobax\\OneDrive\\Desktop\\CPTR 226\\labs\\Lab 10\\Files\\SCRPS\\shop armor.txt'



class Player():
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.attack = 10
        self.points = 10
    
    def intro(self):
        caseys = Shop()
        intro = open(intro_path, "r")
        for i in range(7):
            print(intro.readline())
            sleep(0.5)
        intro.close()
        caseys.shop_menu()


    def checkout(self, cost, powerup):
        if self.points >= cost:
            player1.power_up(powerup)
            self.points -= cost
            print(f"Your balance is now {self.points}")


        else:
            print("Sorry, you do not have enough to purchase this item.")

    def gain_health(self, health):
        self.health + health
    
    def power_up(self, power):
        
        self.attack += power

        print(f"Attack Value is Now {self.attack}")

    def reg_reward(self):
        reg = random.randrange(10, 26, 5)
        self.points += reg
        print(f"You won {reg} points")

    def jack_reward(self):
        jackpot = random.randrange(25, 51, 5)
        self.points += jackpot
        print(f"You won {jackpot} points")


class Shop():
    def __init__(self):
        self.name = "caseys"

    def shop_menu(self):
        menu = open(shop_menu_path, "r")
        for i in range(7):
            print(menu.readline())
            sleep(0.3)
        menu.close()
        self.navigator()


    def navigator(self):
        print("Please enter a number or 0 to exit")
        nav = int(input(""))

        if nav == 1:
            self.weapons()

        if nav == 0:
            self.exit_shop()

    def weapons(self):
        with open(shop_wpns_path) as sw:
            wpns = sw.read()
            print(wpns.rstrip())
            sw.close()
        
        print("Enter a number or 0 to exit")
        wpnnav = int(input(""))

        if wpnnav == 1:
            player1.checkout(10, 50)
            


        self.navigator()


    def exit_shop(self):
        print("goodbye")


class Standard_enemy():
    def __init__(self, name):
        self.name = name
        self.attack = random.randrange(10, 50, 5)
        self.health = 250

    def defeat(self):
        player1.reg_prize()
        print(f"{self.name} defeated")




#objects
player1 = Player("jj")
opp1 = Standard_enemy("opp1")

player1.intro()


