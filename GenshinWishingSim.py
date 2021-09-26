import random
class Gacha:
    def __init__(self, promotionalfivestar, promotionalfourstars):
        self.fivestars = [["QiQi","Mona","Diluc","Jean","Keqing"]]
        self.fourstars = [['Amber', 'Barbara', 'Beidou', 'Bennett', 'Chongyun', 'Diona', 'Fischl', 'Kaeya', 'Lisa', 'Ningguang', 'Noelle', 'Razor', 'Rosaria', 'Sucrose', 'Xiangling', 'Xingqiu', 'Xinyan', 'Yanfei','Alley Hunter', 'Amenoma Kageuchi', 'Blackcliff Agate', 'Blackcliff Longsword', 'Blackcliff Pole', 'Blackcliff Slasher', 'Blackcliff Warbow', 'Compound Bow', 'Crescent Pike', 'Deathmatch', 'Dodoco Tales', "Dragon's Bane", 'Dragonspine Spear', 'Eye of Perception', 'Favonius Codex', 'Favonius Greatsword', 'Favonius Lance', 'Favonius Sword', 'Favonius Warbow', 'Festering Desire', 'Frostbearer', 'Hakushin Ring', 'Hamayumi', 'Iron Sting', 'Katsuragikiri Nagamasa', 'Kitain Cross Spear', "Lion's Roar", 'Lithic Blade', 'Lithic Spear', 'Mappa Mare', 'Mitternachts Waltz', 'Prototype Amber', 'Prototype Archaic', 'Prototype Crescent', 'Prototype Rancour', 'Prototype Starglitter', 'Rainslasher', 'Royal Bow', 'Royal Greatsword', 'Royal Grimoire', 'Royal Longsword', 'Royal Spear', 'Rust', 'Sacrificial Bow', 'Sacrificial Fragments', 'Sacrificial Greatsword', 'Sacrificial Sword', 'Serpent Spine', 'Snow-Tombed Starsilver', 'Solar Pearl', 'Sword of Descension', 'The Alley Flash', 'The Bell', 'The Black Sword', 'The Flute', 'The Stringless', 'The Viridescent Hunt', 'The Widsith', 'Whiteblind', 'Windblume Ode', 'Wine and Song']]
        self.threestars = ['Amber Catalyst', 'Black Tassel', 'Bloodtainted Greatsword', 'Cool Steel', 'Dark Iron Sword', 'Debate Club', 'Ebony Bow', 'Emerald Orb', 'Ferrous Shadow', 'Fillet Blade', 'Halberd', 'Harbinger of Dawn', 'Magic Guide', 'Messenger', 'Otherworldly Story', 'Quartz', 'Raven Bow', 'Recurve Bow', "Sharpshooter's Oath", 'Skyrider Greatsword', 'Skyrider Sword', 'Slingshot', 'Thrilling Tales of Dragon Slayers', "Traveler's Handy Sword", 'Twin Nephrite', 'White Iron Greatsword', 'White Tassel']
        self.promotionalfivestar = promotionalfivestar
        self.promotionalfourstar = promotionalfourstars
        self.fivestars.append(self.promotionalfivestar)
        self.fourstars.append(self.promotionalfourstar)
        self.fourstarpity = 0
        self.fivestarpity = 0
        self.wishes = 0
        self.primosspent = 0
        self.guranteedfourstar = False
        self.guranteedfivestar = False
    def Wish(self, rolls):
        items = []
        self.wishes += int(rolls)
        self.primosspent += (int(rolls)*160)
        if self.fivestarpity >= 75:
            bonus_chance = 10
        else:
            bonus_chance = 0
        for i in range(int(rolls)):
            threestar = False
            fourstar = False
            fivestar = False
            obtained = ""
            stars = ""
            if self.fivestarpity >= 90:
                fivestar = True
            elif self.fourstarpity >= 10:
                item = random.randint(0, 100)
                if item in range(1, 100):
                    fourstar = True
                elif item in range(0,bonus_chance):
                    fivestar = True
            else:
                item = random.randint(0, 100)
                if item in range(11+bonus_chance, 100):
                    threestar = True
                elif item in range(1+bonus_chance, 10):
                    fourstar = True
                elif item in range(0, bonus_chance):
                    fivestar = True
            if threestar:
                stars = "3"
                obtained = random.choice(self.threestars)
            elif fourstar:
                stars = "4"
                if not self.guranteedfourstar:
                    roll = random.randint(0, 1)
                    if roll == 0:
                        self.guranteedfourstar = True
                    else:
                        self.guranteedfourstar = False
                else:
                    roll = 1
                    self.guranteedfourstar = False
                obtained = random.choice(self.fourstars[roll])
                self.fourstarpity = 0
            elif fivestar:
                stars = "5"
                if not self.guranteedfivestar:
                    roll = random.randint(0, 1)
                    if roll == 0:
                        self.guranteedfivestar = True
                    else:
                        self.guranteedfivestar = False
                else:
                    roll = 1
                    self.guranteedfivestar = False
                obtained = random.choice(self.fivestars[roll])
                self.fivestarpity = 0
            if not fourstar:
                self.fourstarpity += 1
            if not fivestar:
                self.fivestarpity += 1
            items.append(f"({stars} star) {obtained}")
        print(f"\n[+] Results of the {rolls} pull:\n[+] {items}\n\n[+] Wish Stats:\n[+] Wishes: {self.wishes}\n[+] Primos Spent: {self.primosspent}\n[+] 5 Star Pity: {self.fivestarpity}\n[+] 4 Star Pity: {self.fourstarpity}")
class Main:
    def __init__(self):
        self.eventbanners = [["Invitation to Mundane Life",["Xiao"],["Beidou","Xinyan","Diona"]],["Dance Of The Lanterns",["Keqing"],["Barbara","Ningguang","Bennet"]],["Moment Of Bloom",["Hu Tao"],["Xiangling","Chongyun","Xinqiu"]],["Ballad in Goblets",["Venti"],["Razor","Sucrose","Noelle"]],["Farewell of Snezhnaya",["Tartaglia"],["Barbara","Fischl","Rosaria"]],["Gentry of Hermitage",["Zhongli"],["Yanfei","Noelle","Diona"]],["Adrift in the Harbor",["Ganyu"],["Xiangling","Xingqiu","Noelle"]],["The Heron's Court",["Ayaka"],["Yanfei","Chongyun","Ningguang"]], ["Reign Of Serenity", ["Raiden Shogun"],["Xiangling","Kujou Sara","Sucrose"]]]
        self.Logo()
        self.Config()
    def Logo(self):
        print("""
  _____                _     _        __          ___     _     _                _____ _                  ___    ___  
 / ____|              | |   (_)       \ \        / (_)   | |   (_)              / ____(_)                |__ \  / _ \ 
| |  __  ___ _ __  ___| |__  _ _ __    \ \  /\  / / _ ___| |__  _ _ __   __ _  | (___  _ _ __ ___   __   __ ) || | | |
| | |_ |/ _ \ '_ \/ __| '_ \| | '_ \    \ \/  \/ / | / __| '_ \| | '_ \ / _` |  \___ \| | '_ ` _ \  \ \ / // / | | | |
| |__| |  __/ | | \__ \ | | | | | | |    \  /\  /  | \__ \ | | | | | | | (_| |  ____) | | | | | | |  \ V // /_ | |_| |
 \_____|\___|_| |_|___/_| |_|_|_| |_|     \/  \/   |_|___/_| |_|_|_| |_|\__, | |_____/|_|_| |_| |_|   \_/|____(_)___/ 
                                                                         __/ |                                        
                                                                        |___/                                          
Wishing Simulator By DrSquid
""")
    def Config(self):
        print("[+] Here are all of the character Banners you can wish for: ")
        for i in self.eventbanners:
            print(f"\n[+] Banner Name: {i[0]}")
            print(f"[+] Event 5 Star: {i[1][0]}")
            print(f"[+] Event 4 Stars: {i[2]}")
        while True:
            properbanner = False
            banner = input(f"\n[+] Which banner would you like to wish on?: ")
            for i in self.eventbanners:
                if banner.strip().lower() == i[0].strip().lower():
                    properbanner = True
                    self.banner = i
                    self.fivestar = self.banner[1]
                    self.fourstars = self.banner[2]
                    self.gacha = Gacha(self.fivestar, self.fourstars)
                    break
            if properbanner:
                break
            else:
                print("[+] You need to input a proper banner name.")
        self.Wish()
    def Wish(self):
        print("[+] Input 'stop' to wish on another banner.")
        while True:
            try:
                pulls = input("[+] How many pulls would you like to do?(Max 10 at a time): ")
                if int(pulls) > 10:
                    pulls = 10
                elif int(pulls) < 1:
                    pulls = 1
                self.gacha.Wish(pulls)
            except:
                if pulls == "stop":
                    break
                else:
                    print("[+] Please Enter an integer.")
        self.Config()
Item = Main()
