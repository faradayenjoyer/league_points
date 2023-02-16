def abc():
    num = input("Tell me the wins, and draws seperate with commas (in that order, wins -> draws), no spaces. ").split(",")
    num = list(map(int, num))
    wins = num[0]
    draws = num[1]
    wins *= 2
    draws *= 1
    total = wins + draws
    print(total)
abc()
