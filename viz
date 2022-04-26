from unittest import result
import matplotlib.pyplot as plt
import os
import sqlite3
import json
import numpy as np

def ranking_vs_home_points(cur, conn):
    cur.execute("""
    SELECT Ranking.Rank, Names.TOTAL_Home_Points 
    FROM Names
    JOIN Ranking ON Names.Name = Ranking.Name
    GROUP BY Ranking.Rank
    """)
    db_results = cur.fetchall()
    results_dict = {}
    for r in db_results:
        results_dict[int(r[0])] = r[1]

    y = list(results_dict.values())
    x = list(results_dict.keys())
    plt.scatter(x,y, c="green")
    
    y_arr = np.array(y)
    x_arr = np.array(x)    
    a, b = np.polyfit(x_arr, y_arr, 1)
    plt.plot(x_arr, a*x_arr+b)
    
    plt.title("Ranking vs Home Points Scored")
    plt.xlabel("Ranking")
    plt.ylabel("Home Points Scored")
    plt.show()

    source_dir = os.path.dirname(__file__)
    full_path = os.path.join(source_dir, 'ranking_vs_home_points.json')
    with open(full_path, 'w') as f:
        json.dump(results_dict, f)

    
def wins_vs_points_scored(cur, conn):
    cur.execute("""
    SELECT Points.Wins, Points.Average_Points_Scored
    FROM Points 
    """)
    db_results = cur.fetchall()
    results_dict = {}
    for r in db_results:
        results_dict[r[0]] = r[1]

    y = list(results_dict.values())
    x = list(results_dict.keys())
    plt.scatter(x,y, c="green")
    
    y_arr = np.array(y)
    x_arr = np.array(x)    
    a, b = np.polyfit(x_arr, y_arr, 1)
    plt.plot(x_arr, a*x_arr+b)
    
    plt.title("Wins vs Average Points Scored")
    plt.xlabel("Wins")
    plt.ylabel("Average Points Scored")
    plt.show()

    source_dir = os.path.dirname(__file__)
    full_path = os.path.join(source_dir, 'wins_vs_points_scored.json')
    with open(full_path, 'w') as f:
        json.dump(results_dict, f)

def average_points_per_game_vs_ranking(cur, conn):
    cur.execute("""
    SELECT SUM(Names.TOTAL_Home_Points + Names.TOTAL_Away_Points), SUM(Points.Wins + Points.Losses), Ranking.Rank
    FROM Names
    JOIN Points ON Names.Name = Points.Name
    JOIN Ranking ON Names.Name = Ranking.Name
    GROUP BY Ranking.Rank
    """)
    db_results = cur.fetchall()
    results_dict = {}
    for r in db_results:
        results_dict[r[2]] = int(r[0] / r[1])
    
    y = list(results_dict.values())
    x = list(results_dict.keys())
    plt.scatter(x,y, c="green")
    
    y_arr = np.array(y)
    x_arr = np.array(x)    
    a, b = np.polyfit(x_arr, y_arr, 1)
    plt.plot(x_arr, a*x_arr+b)
    
    plt.title("Average Points Per Game vs Ranking")
    plt.xlabel("Average Points Per Game")
    plt.ylabel("Ranking")
    plt.show()

    source_dir = os.path.dirname(__file__)
    full_path = os.path.join(source_dir, 'average_points_per_game_vs_ranking.json')
    with open(full_path, 'w') as f:
        json.dump(results_dict, f)

def main():
    source_dir = os.path.dirname(__file__)
    full_path = os.path.join(source_dir, 'Testbase.db')
    conn = sqlite3.connect(full_path)
    cur = conn.cursor()
    ranking_vs_home_points(cur, conn)
    wins_vs_points_scored(cur, conn)
    average_points_per_game_vs_ranking(cur, conn)
    cur.close()

if __name__ == "__main__":
    main()