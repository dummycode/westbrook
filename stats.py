import shelve

def getStats():
    shelf = shelve.open('stats', flag='r')

    stats = [shelf['points'], shelf['assists'], shelf['rebounds']]

    shelf.close()

    return stats;

def isAveragingTripleDouble():
    return True
    stats = getStats()
    for stat in stats:
        if (int(float(stat)) <  10):
            return False
    return True
