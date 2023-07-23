##Author: Paul Lorenz III
##Date: 7-15-2023
##Description: Creating tables into the pysports database.  

SELECT team_id, team_name, mascot FROM team;

drop database if exists pysports;
create database pysports; 
use pysports;

CREATE TABLE `team` (
  `team_id` int NOT NULL,
  `team_name` varchar(45) DEFAULT NULL,
  `mascot` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`team_id`)
) ;

CREATE TABLE `player` (
  `player_id` int NOT NULL,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `teamID` int NOT NULL,
  PRIMARY KEY (`player_id`),
  CONSTRAINT `Fk_team_player` FOREIGN KEY (`teamID`) REFERENCES `team` (`team_id`)
) ;

print("-- DISPLAYING TEAM RECORDS --")
cursor = db.cursor()

cursor.execute("SELECT team_id, team_name, mascot FROM team")

teams = cursor.fetchall()

for team in teams:
    print("Team Name: {}".format(team[1]))

print("-- DISPLAYING PLAYER RECORDS --")

input("press any key to continue...")