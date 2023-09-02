class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.score = 0
        self.rounds_history = {}

    def __str__(self):
        return(f"{self.rounds_history}")
    
    def update_score(self, score):
        self.score += score

class EsmFamilGame:
    def __init__(self):
        self.categories = ["Name", "City", "Object"]
        self.round = 0
        self.r_words = {} #words for each round
        self.players = []
        self.letters = []

    def add_player(self, player_name, i):
        self.players.append(Player(str(i + 1).zfill(3), player_name))

    def letter_repeated(self, letter):
        if letter in self.letters:

            return True
        self.letters.append(letter)
        return False

    def word_process(self):
        for cat, words in self.r_words.items():
            uniques = [word for word in words if word not in ['', None] and words.count(word) == 1]
            duplicates = list(set(word for word in words if word not in ['', None] and words.count(word) > 1))
            self.r_words[cat] = {'uniques': uniques, 'duplicates': duplicates}

    def calc_round(self, letter):

        for player in self.players:
            score = 0
            pt = 0
            for category, word in player.rounds_history[letter]['words'].items():
                if word in self.r_words[category]['uniques']:
                    pt = 10
                elif word in self.r_words[category]['duplicates']:
                    pt = 5
                else:
                    pt = 0
                score += pt
            player.rounds_history[letter]['score'] = score
            player.update_score(score)                                      


    def play_round(self, letter):
        self.r_words = {cat: [] for cat in self.categories}
        #update the number of the rounds
        self.round += 1

        #getting the entries
        for player in self.players:
            player_words = {}

            for cat in self.categories:
                new_word = input(f"{player.name}, enter a word starting with '{letter}' for {cat}: ").strip()
                player_words[cat] = new_word
                if not new_word or new_word[0].lower() != letter:
                    new_word = None
                self.r_words[cat].append(new_word)
            
            player.rounds_history[letter] = {'words': player_words}
        self.word_process()
        self.calc_round(letter)



    def display_scores(self):
        print(f"\nCurrent Scores for round {self.round}:")
        for player in self.players:
            print(f"{player.name}: {player.score} points")

if __name__ == "__main__":
    game = EsmFamilGame()

    # Add players
    num_players = int(input("Enter the number of players: "))
    for i in range(num_players):
        player_name = input("Enter player name: ")
        game.add_player(player_name, i)

    while True:
        letter = input("Enter a letter (or 'q' to quit): ").strip().lower()
        if letter == 'quit':
            break
        if not letter.isalpha() or len(letter) != 1:
            print("Invalid input. Please enter a single letter.")
            continue
        elif game.letter_repeated(letter):
            print(f"The letter {letter} is repeated, try entering another letter")
            continue

        game.play_round(letter)
        game.display_scores()