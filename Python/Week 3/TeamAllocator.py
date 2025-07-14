import random 

players=["walter", "Max","braylen"
         "ollie","xavier", "Avery"
         "Carl", "Darren","EJ","no'home"
         "Marshawn","Ja'den","Isaiah"
         "Kenlon","Nishad","Kauri",
         "Joseph","Semaj","Tay",
         "Jefferey","Joaquin","Devon"
         "bobs", "dad", "mom"]

def PickTeams(players):
    random.shuffle(players)
team1 = players[:len(players) // 2]
teamCaptin1 = team1[random.randrange(0, 12)] 
    
    
print("TEAM 1")
print("Team 1 Captin: " + teamCaptin1)
print(team1)

PickTeams(players)
for player in team1:
    print(player)

    team2 = players[:len(players) // 2]
    teamCaptin2 = team2[random.randrange(0,12)]
    
    print("Team 2:")
    print("Team 2 captin"+ teamCaptin2)
    for player in team2:
        print(player)

    PickTeams(players)    




