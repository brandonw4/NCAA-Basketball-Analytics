import requests
import sqlite3
import pprint
import os
import json
import time
start_time = time.time()
source_dir = os.path.dirname(__file__)
full_path = os.path.join(source_dir, 'Testbase.db')
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


for i in data2:
	url = "https://api-basketball.p.rapidapi.com/statistics"
	querystring = {"season":"2021-2022","league":"116","team":"{}".format(i)}

	headers = {
		"X-RapidAPI-Host": "api-basketball.p.rapidapi.com",
		"X-RapidAPI-Key": "4a9ae85127msh66e82c4bcc504b3p1dcd57jsn35a9ff4b2773"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	test = (json.loads(response.text))
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
print("Done!")
print("--- %s seconds ---" % (time.time() - start_time))
c.close()
conn.close()

