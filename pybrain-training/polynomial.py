from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
import numpy as np
import pymongo

def parse_game_stats(game):
    """
        Takes a game and formats it as an array of values
        Argument:
            game: a game property of a player
            
        Returns:
            An array of the statistics for that game
    """
    # Need to figure out how to deal with parsing all position data
    # create matrix to hold all features for each game (need to get num of features)
    #   1 passescompleted : Number,
    #   2 passesattempted : Number,
    #   3 passingyards : Number,
    #   4 passingtouchdowns : Number,
    #   5 passingInterceptions : Number,
    #   6 rushattempts : Number,
    #   7 rushyards : Number,
    #   8 rushtouchdowns : Number,
    #   9 - 12 reception infor
    #   13+ ideas (opponent average stats against for rush/rec/pass)
    return [game['passescompleted'] | 0,
            game['passesattempted'] | 0,
            game['passingyards'] | 0,
            game['passingtouchdowns'] | 0,
            game['passingInterceptions'] | 0,
            game['rushattempts'] | 0,
            game['rushyards'] | 0,
            game['rushtouchdowns'] | 0]


def get_player_data():
    """
        Gets player data formatted for machine learning
        Returns:
            A dictionary with 2 keys: 
                'train' - set of data to train on
                'target' - the target data for the training set
    """
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['professor-stats']
    collection = db.playerdatas
    players = list(collection.find())
    print("Retreived all players, total players is %s" % len(players))

    X = []
    y = []
    for player in players:
        print("generating training data for %s" % player['name'])
        if len(player['games']) >= 4:
            print("%s has 4 or more games so we can generate their data" % player['name'])
            for i in range(0,len(player['games'])-4):
                game1 = player['games'][i]
                game2 = player['games'][i + 1]
                game3 = player['games'][i + 2]
                target = player['games'][i + 3]
                set = []
                set = np.append(set, (parse_game_stats(game1),
                                      parse_game_stats(game2),
                                      parse_game_stats(game3)))
                X.append(set)
                
                print(" Last set appended was %s " % X[-1])
                y.append(parse_game_stats(target))
    return { 'train': X, 'target': y}


def train_linear_regression(train,target):
    """
        Trains via linear regression from the target and train data
            Arguments: 
                train : an array of training data
                target: an array of associated target data
            Returns:
                The trained model
    """
    model = Pipeline([('poly',PolynomialFeatures(degree=2)),
                  ('linear', LinearRegression(fit_intercept=False, normalize=False, copy_X=True))])
    model = model.fit(train, target)
    return model


data = get_player_data()
model = train_linear_regression(data['train'], data['target'])
#print(model.predict())
