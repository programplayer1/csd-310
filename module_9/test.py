

    
    mycursor3 = db.cursor()
    sql2 = "Delete from player where first_name = 'Gollum' and last_name = 'Ring Stealer' "
    mycursor3.execute(sql) 

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