import random

class SplendorGame:
    def __init__(self):
        self.gems = {}
        self.players = []
        self.all_cards = []
        self.all_nobles = []

        self.fields = {
            "gems": [],
            "cards": [],
            "nobles": [],
        }

    def initialize_cards(self):
        for i in range(40):
            card = {
                "name": f"Card {i}",
                "cost": {
                    "diamond": random.randint(0, 3),
                    "sapphire": random.randint(0, 3),
                    "emerald": random.randint(0, 3),
                    "ruby": random.randint(0, 3),
                    "onyx": random.randint(0, 3)
                },
                "points": random.randint(0, 3)
            }
            self.all_cards.append(card)
        print("Deck is ready")

    def initialize_nobles(self):
        for i in range(3):
            noble = {
                "cost": {
                    "diamond": random.randint(3, 4),
                    "sapphire": random.randint(3, 4),
                    "emerald": random.randint(3, 4),
                    "ruby": random.randint(3, 4),
                    "onyx": random.randint(3, 4)
                },
                "points": random.randint(3, 4)
            }
            self.all_nobles.append(noble)
        print("Nobles are ready")

    def initialize_gems(self):
        self.gems = {
            "diamond": 7,
            "sapphire": 7,
            "emerald": 7,
            "ruby": 7,
            "onyx": 7,
            "gold": 5
        }
        print("Gems are ready")

    def initialize_players(self):
        num_players = int(input("Enter the number of players: "))
        for i in range(num_players):
            name = input(f"Enter player {i+1}'s name: ")
            self.add_player(name)
        print(f"{num_players} players are ready")

    def choose_random(self, lst, num):
        result = []
        for i in range(num):
            # need to pop the element from the list so it doesn't get chosen again
            result.append(lst.pop(random.randint(0, len(lst)-1)))
        return result

    def add_player(self, name):
        if name in [player["name"] for player in self.players]:
            print(f"{name} is already in use")
            self.add_player(input("Please enter a different name: ")) 
        else:
            self.players.append({"name": name, "gems": {}, "cards": [], "points": 0})

    def collect_gems(self, name, gem_colors):
        # TODO: Check if the player has enough gems to reserve
        gem_list = gem_colors.split()
        for gem in gem_list:
            if self.gems[gem] > 0:
                self.gems[gem] -= 1
                self.players[name]["gems"][gem] += 1
            else:
                print(f"{gem} is not available")
                break


    def turn_action(self, name, action):
        # Collect
        if action == 1:
            choices = input("""Would you like to collect two gems of the same type or three gems of different types?
                 1: Two gems of the same type
                 2: Three gems of different types""")
            if choices == "1":
                prompt = """Which gem would you like to collect twice?
                1: Diamond
                2: Sapphire
                3: Emerald
                4: Ruby
                5: Onyx"""
                self.collect_gems(name, input(prompt))
            elif choices == "2":
                prompt = """Which gems would you like to collect? (Select 3) ex. '1 2 3'
                1: Diamond
                2: Sapphire
                3: Emerald
                4: Ruby
                5: Onyx"""
                self.collect_gems(name, input(prompt))

    def debug_print(self):
        print("Gems:")
        print(self.gems)
        print("Players:")
        print(self.players)

    def play_game(self):
        self.initialize_cards()
        self.initialize_nobles()
        self.initialize_gems()
        self.initialize_players()

        while True:
            for player in self.players:
                print(f"{player['name']}'s turn")
                action = input(
                    """What would you like to do?
1: Collect
2: Reserve
3: Buy\n""")
                self.turn_action(player["name"], int(action))
                self.debug_print()



game = SplendorGame()
game.play_game()
