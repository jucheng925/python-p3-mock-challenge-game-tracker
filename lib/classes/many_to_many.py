class Game:
    all = []
    def __init__(self, title):
        self.title = title
        Game.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not hasattr(self, "_title"):
            if type(title) == str and len(title) > 0:
                self._title = title
            else:
                pass
            

    def results(self):
        return [result for result in Result.all if result.game is self]

    def players(self):
        return list(set([result.player for result in Result.all if result.game is self]))

    def average_score(self, player):
        list_score = [result.score for result in Result.all if result.game is self and result.player is player]
        return sum(list_score)/len(list_score)

class Player:
    all = []
    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) in range(2,16):
            self._username = username
        else:
            pass

    def results(self):
        return [result for result in Result.all if result.player is self]

    def games_played(self):
        return list(set([result.game for result in Result.all if result.player is self]))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        # my_result = self.results()
        return len([result for result in Result.all if result.game == game and result.player is self])

    @classmethod
    def highest_scored(cls, game):
        if (len(game.players()) == 0):
            return None
        players_unique = game.players()
        player_dict = {}
        for player in players_unique:
            player_dict[player] = game.average_score(player)
        players = list(player_dict.keys())
        scores = list(player_dict.values())
        return players[scores.index(max(scores))] 
    

class Result:
    all = []
    def __init__(self, player, game, score):
        self._player = player
        self._game = game
        self._score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if not hasattr(self, "_score"):
            if isinstance(score, int) and score in range(1, 5000):
                self._score = score
            else:
                pass

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            pass

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            pass