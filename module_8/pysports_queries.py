"""
Author:  Paul Lorenz III
Date: July 23, 2023
Assignment Number: Module 8.3
Description: Connecting to the MySQL and getting data from the player and team tables from pysports database.



"""


import mysql.connector
from mysql.connector import errorcode

config = { 
    "user":"pysports_user",
    "password":"MySQL8IsGreat!",
    "host":"127.0.0.1",
    "database":"pysports",
    "raise_on_warnings":True
}

try: 
    db=mysql.connector.connect(**config) 


    print("-- DISPLAYING TEAM RECORDS --")
    cursor = db.cursor() 
    cursor.execute("SELECT team_id, team_name, mascot FROM team") 
    teams = cursor.fetchall()
    for team in teams: 
       print("Team ID: {}".format(team[0]))
       print("Team Name: {}".format(team[1]))
       print("Mascot: {}".format(team[2]))
       print("\n")
    print("--DISPLAYING PLAYER RECORDS---")
    cursor1 = db.cursor() 
    cursor1.execute("SELECT player_id, first_name, last_name, team_id from player") 
    players = cursor1.fetchall() 
    for player in players: 
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team ID: {}".format(player[3]))
        print("\n")

    input("\n\n Press any key to continue.....")
    

except mysql.connector.Error as err: 
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid") 

    elif err.errno == errorcode.ER_BAD_DB_ERROR: 
        print(" The specified database does not exist")

    else: 
        print(err)



finally: 
    db.close()



