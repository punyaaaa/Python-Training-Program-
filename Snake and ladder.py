
import random
snakes = {
    22: 6,
    45: 30,  
    96: 64
}
ladders = {
    7: 24,
    21: 77,
    42: 90,
    40: 60
}
player1 = 0
player2 = 0
while True:
    player = int(input("Enter player number (1 or 2): "))
    print(f"\nplayer 1: {player1}")
    print(f"player 2: {player2}")
    if player == 1:
        dice = random.randint(1, 6)
        print(f"dice score : {dice}")
        player1 += dice
        if player1 in ladders:
            print("ladder is climbed")
            player1 = ladders[player1]
        elif player1 in snakes:
            print("caught by the snake")
            player1 = snakes[player1]
        if player1 >= 100:
            print("player 1 is the winner")
            break

    elif player == 2:
        dice = random.randint(1, 6)
        print(f"dice score : {dice}")
        player2 += dice
        if player2 in ladders:
            print("ladder is climbed")
            player2 = ladders[player2]
        elif player2 in snakes:
            print("caught by the snake")
            player2 = snakes[player2]
        if player2 >= 100:
            print("player 2 is the winner")
            break
    else:
        print("invalid!!")