"""Retrieves a list of players with their most recent 3 seasons and other information for machine learning

    Usage:
        ./getplayers.py -mode <mode>
"""

import sys
import playerdb

def getPlayersFromServer(url, numSeasons):
    """Given a URL return a list of players

        Args:
            url: the URL to use to retrieve the players
            numSeasons:
        Returns:
            a list of players with their associated season information
        
        Usage:
            getPlayersFromServer(url[, numSeasons])
    """
    return []

def getPlayersFromDatabase(numSeasons):
    """Given a URL return a list of players
        
        Args:
        numSeasons:
        Returns:
        a list of players with their associated season information
        
        Usage:
        getPlayersFromServer(connectionString[, numSeasons])
        """
    players = player.getplayers(numSeasons)
    return players

def parseArgv(args):
    #do some parsing
    return "mode1"

def main(mode):
    print_words('fetching players from mode %',(mode))


if __name__ == '__main__':
    mode = parseArgv(sys.argv)
    main(mode)