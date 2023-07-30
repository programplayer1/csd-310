"""
Author:  Paul Lorenz III
Date: July 30, 2023
Assignment Number: Module 9.3
Description: Connecting to the MySQL and Inserting, Updating , Deleting and  getting data  by Joining the player and team tables from pysports database.



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

    mycursor1 = db.cursor()


    Insertsql = "Insert into player(first_name,last_name,team_id) Values('Smeagol','Shire Folk',1) "
    mycursor1.execute(Insertsql)

    db.commit()

  
    print("--DISPLAYING PLAYER AFTER INSERT ---")
    mycursor1.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team  	ON player.team_id = team.team_id") 
    players = mycursor1.fetchall() 
    for player in players: 
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team Name: {}".format(player[3]))
        print("\n")

    mycursor2 = db.cursor()
    updatesql = "Update player SET team_id = 2 , first_name = 'Gollum' , last_name = 'Ring Stealer' where first_name = 'Smeagol'" 
    mycursor2.execute(updatesql) 

    db.commit() 


    print("--DISPLAYING PLAYER AFTER UPDATE ---")
    cursor2 = db.cursor() 
    cursor2.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team  	ON player.team_id = team.team_id") 
    players = cursor2.fetchall() 
    for player in players: 
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team Name: {}".format(player[3]))
        print("\n")

    mycursor3 = db.cursor()
    Deletesql = "Delete from player where first_name = 'Gollum' and last_name = 'Ring Stealer' "
    mycursor3.execute(Deletesql) 

    db.commit()

    print("-- DISPLAYING PLAYER AFTER DELETE ...")
    cursor3 = db.cursor() 
    cursor3.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team  	ON player.team_id = team.team_id") 
    players = cursor3.fetchall() 
    for player in players: 
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team Name: {}".format(player[3]))
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



