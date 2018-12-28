import requests, bs4, shelve

url = "http://www.espn.com/nba/player/stats/_/id/3468/russell-westbrook"
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Get all tables
tables = soup.findChildren('table')

# This season
thisSeasonAverages = tables[0]
rows = thisSeasonAverages.findChildren('tr')

# Loop throw first row
cells = rows[0].findChildren('td')
stats = []
for i in range(3):
    value = float(cells[i].string)
    stats.append(value)

shelf = shelve.open('stats')
shelf['points'] = stats[0]
shelf['assists'] = stats[1]
shelf['rebounds'] = stats[2]
shelf.close()

