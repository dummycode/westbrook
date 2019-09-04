import shelve

def getStats():
    shelf = shelve.open('stats')
    return [shelf['points'], shelf['assists'], shelf['rebounds']];

def isAveragingTripleDouble():
    return True
    stats = getStats()
    for stat in stats:
        if (int(float(stat)) <  10):
            return False
    return True
