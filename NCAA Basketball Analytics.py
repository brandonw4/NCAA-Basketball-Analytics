import requests
import sqlite3
import pprint
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
	c.executescript('DROP TABLE IF EXISTS Points; CREATE TABLE IF NOT EXISTS Points (Name TEXT, Wins INT, Losses INT, Average_Points_Scored REAL, Average_Points_Given REAL)')
create_table()
def data_entry():
	c.execute("INSERT INTO Points (Name, Wins, Losses, Average_Points_Scored, Average_Points_Given) VALUES(?, ?, ?, ?, ?)", (name2, win4, loss4, num2, num3))
	conn.commit()

def create_table_name():
	c.executescript('DROP TABLE IF EXISTS Names; CREATE TABLE IF NOT EXISTS Names (Id INT, Name TEXT)')
def data_entry_name():
	c.execute("INSERT INTO Names (Id, Name) VALUES(?, ?)", (Id, Name))
	conn.commit()
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
for i in value:
    Id = i['id']
    Name = i['name']
    data_entry_name()
data2 = []
def read_data():
	c.execute('SELECT Id FROM Names')
	data = c.fetchall()
	for i in data:
		data2.append(i[0])
read_data()
data_set = []
Question = input("Would you like to use cached data? y/n")
if Question ==('n'):
	count = 0
	for i in data2:
		url = "https://api-basketball.p.rapidapi.com/statistics"
		querystring = {"season":"2021-2022","league":"116","team":"{}".format(i)}

		headers = {
			"X-RapidAPI-Host": "api-basketball.p.rapidapi.com",
			"X-RapidAPI-Key": "4a9ae85127msh66e82c4bcc504b3p1dcd57jsn35a9ff4b2773"
		}

		response = requests.request("GET", url, headers=headers, params=querystring)
		test = (json.loads(response.text))
		data_set.append(test)
		count = count + 1
		if count == 1:
			print("Gathering Up-to-Date Data! This process will take awhile.")
		elif count == 68:
			print("10% Complete")
		elif count == 136:
			print("20% Complete")
		elif count == 204:
			print("30% Complete")
		elif count == 272:
			print("40% Complete")
		elif count == 340:
			print("50% Complete")
		elif count == 408:
			print("60% Complete")
		elif count == 476:
			print("70% Complete")
		elif count == 544:
			print("80% Complete")
		elif count == 612:
			print("90% Complete")
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
			data_entry()
	with open(new_path, 'w') as f:
		json.dump(data_set, f, ensure_ascii=False, indent=4)
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
			data_entry()

print("Done!")
print("--- %s seconds ---" % (time.time() - start_time))
c.close()
conn.close()

