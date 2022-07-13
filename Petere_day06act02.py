winning = {10,11,8,1,5,20}
players = {
    "Jo":{1,8,10,27,12,15},
    "JoJo":{1,8,27,3,4,9},
    "Joe":{9,4,3,12,15,21},
    "Gemar":{10,11,1,8,5,20}
}

for x in list(players.keys()):
    toCount = winning.intersection(players[x])
    if len(toCount)*100 == 0:
        print('%s won nothing!'%(x))
    else:
        print('%s won %s pesos!'%(x,len(toCount)*100))
    
        