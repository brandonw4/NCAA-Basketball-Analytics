from bs4 import BeautifulSoup
import requests
import sqlite3
import os
import json
import time

start_time = time.time()
source_dir = os.path.dirname(__file__)
full_path = os.path.join(source_dir, 'Testbase.db')
new_path = os.path.join(source_dir, 'team_stats.json')
conn = sqlite3.connect(full_path)
c = conn.cursor()
def create_table():
	c.executescript('CREATE TABLE IF NOT EXISTS Points (Name TEXT, Wins INT, Losses INT, Average_Points_Scored REAL, Average_Points_Given REAL)')
create_table()
def data_entry():
	for i in list3:
		name2 = i[0]
		win4 = i[1]
		loss4 = i[2]
		num2 = i[3]
		num3 = i[4]
		c.execute("INSERT INTO Points (Name, Wins, Losses, Average_Points_Scored, Average_Points_Given) VALUES(?, ?, ?, ?, ?)", (name2, win4, loss4, num2, num3))
	conn.commit()

def create_table_name():
	c.executescript('CREATE TABLE IF NOT EXISTS Names (Id INT, Name TEXT)')
def data_entry_name():
	for i in list2:
		Id = i[0]
		Name = i[1]
		c.execute("INSERT INTO Names (Id, Name) VALUES(?, ?)", (Id, Name))
	conn.commit()
def get_team_rankings():
    page_link = "https://www.ncaa.com/rankings/basketball-men/d1/ncaa-mens-basketball-net-rankings"
    page = requests.get(page_link)
    soup = BeautifulSoup(page.text, 'html.parser')
    full_table = soup.find_all('tr')
    testRow1 = full_table[1]

    data_dict = {}
    for row in full_table:
        try:
            row_data = row.find_all('td')
            team_name = row_data[2].text
            team_ranking = int(row_data[0].text)
            data_dict[team_name] = team_ranking
        except:
            continue

    return((data_dict))

def create_table_rank():
	    c.executescript('CREATE TABLE IF NOT EXISTS Ranking (Name TEXT, Rank INT)')
create_table_rank()
def count_columns():
    c.execute("SELECT COUNT(Rank) FROM Ranking")
    results = c.fetchall()
    data = results[0]
    data6 = data[0]
    return data6
def ranking_data():
    limitor = 0
    for i in testlst[count_columns():]:
        Name = i[0]
        Rank = i[1]
        limitor = limitor + 1
        if limitor < 25:
            c.execute("INSERT INTO Ranking (Name, Rank) VALUES(?, ?)", (Name, Rank))
        elif limitor > 25:
            break
    conn.commit()
testlst = []
namelst = []
for x, y in get_team_rankings().items():
    testlst.append((x,y))
limitor = 0
for i in testlst[count_columns():]:
	limitor = limitor + 1
	Nametest = i[0]
	if limitor < 25:
		namelst.append(Nametest)
	elif limitor > 25:
		break


create_table_rank()
ranking_data()
print("Welcome to NCAA Basketball Analytics!")
print("Gathering up-to-date team info...")
url = "https://api-basketball.p.rapidapi.com/teams"

querystring = {"league":"116","season":"2021-2022"}

headers = {
	"X-RapidAPI-Host": "api-basketball.p.rapidapi.com",
	"X-RapidAPI-Key": "4a9ae85127msh66e82c4bcc504b3p1dcd57jsn35a9ff4b2773"
}

response = requests.request("GET", url, headers=headers, params=querystring)
test = (json.loads(response.text))
value = test['response']
create_table_name()
list2 = []
Idlist = []
for i in value:
	Id = i['id']
	Name = i['name']
	if Name in namelst:
		list2.append((Id,Name))
		Idlist.append(Id)
data2 = []
def read_data():
	c.execute('SELECT Id FROM Names')
	data = c.fetchall()
	for i in data:
		data2.append(i[0])
read_data()
Adrian = data2
data_entry_name()
read_data()

data_set = []
list3 = []
Question = input("Would you like to use cached data? y/n")
if Question ==('n'):
	count = 0
	for i in Idlist:
		url = "https://api-basketball.p.rapidapi.com/statistics"
		querystring = {"season":"2021-2022","league":"116","team":"{}".format(i)}

		headers = {
			"X-RapidAPI-Host": "api-basketball.p.rapidapi.com",
			"X-RapidAPI-Key": "4a9ae85127msh66e82c4bcc504b3p1dcd57jsn35a9ff4b2773"
		}

		response = requests.request("GET", url, headers=headers, params=querystring)
		test = (json.loads(response.text))
		data_set.append(test)
		value = test['response']
		name1 = value['team']
		name2 = name1['name']
		val2 = (value['points'])
		val3 = val2['for']
		val4 = val3['average']
		val5 = val2['against']
		val6 = val5['average']
		game = value['games']
		win2 = game['wins']
		win3 = win2['all']
		win4 = win3['total']
		loss2 = game['loses']
		loss3 = loss2['all']
		loss4 = loss3['total']
		num2 = float(val4['all'])
		num3 = float(val6['all'])
		if win4 and loss4 != 0:
			list3.append((name2, win4, loss4, num2, num3))
elif Question ==('y'):
	f = open(new_path)
	xi = json.load(f)
	print("This won't take long! Please wait a moment")
	for i in xi:
		value = i['response']
		name1 = value['team']
		name2 = name1['name']
		val2 = (value['points'])
		val3 = val2['for']
		val4 = val3['average']
		val5 = val2['against']
		val6 = val5['average']
		game = value['games']
		win2 = game['wins']
		win3 = win2['all']
		win4 = win3['total']
		loss2 = game['loses']
		loss3 = loss2['all']
		loss4 = loss3['total']
		num2 = float(val4['all'])
		num3 = float(val6['all'])
		if win4 and loss4 != 0:
			list3.append((name2, win4, loss4, num2, num3))
data_entry()
print("Done!")
print("--- %s seconds ---" % (time.time() - start_time))
c.close()
conn.close()

