import random

print("Pacanele Time 7️⃣  7️⃣  7️⃣  7️⃣  7️⃣")
print("---------------------------")
print()

pacanea = ["7  ", "🍉", "🍋", "🍇", "🍒", "⭐", "🟣", "🍊"]

hand = []

cards = {"Rosie": ["♥️", "♦️"], "Neagra": ["♠️", "♣️"]}
cardsDealt = []

def prettyPrint():
    print("--------------------------------------")
    for index in range(5):
            print(f"{hand[index]:^5}", end ="|")
    print()
    print("--------------------------------------")
    for index in range(5, 10):
            print(f"{hand[index]:^5}", end ="|")
    print()
    print("--------------------------------------")
    for index in range(10, 15):
            print(f"{hand[index]:^5}", end ="|")
    print()
    print("--------------------------------------")

budget = int(input("Insert Budget\n> "))
bet = int(input("Choose your bet\n> "))

while True:
    hand = []
    prizeCollected = False

    for i in range (0, 15):
        i = random.randint(0, len(pacanea) - 1)
        hand.append(pacanea[i])
        i += 1
        
    start = input("Press SPACE to start\n> ")
    budget -= bet
    randomChoice = ""
    prettyPrint()

    print(f"Remaining budget: {budget}")
    print(f"Bet: {bet}")
    print()

    winningHandx2 = False
    winningHandx3 = False
    winningHandx4 = False
    winningHandx5 = False
    winningHandx10 = False
    
    if hand[0] == hand[1] == hand[2] == hand[3] == hand[4] or hand[5] == hand[6] == hand[7] == hand[8] == hand[9] or hand[10] == hand[11] == hand[12] == hand[13] == hand[14] or hand[0] == hand[6] == hand[12] == hand[8] == hand[4] or hand[10] == hand[6] == hand[2] == hand[8] == hand[14]:
        winningHandx10 = True

    elif hand[0] == hand[1] == hand[2] == hand[3] or hand[5] == hand[6] == hand[7] == hand[8] or hand[10] == hand[11] == hand[12] == hand[13] or hand[0] == hand[6] == hand[12] == hand[8] or hand[10] == hand[6] == hand[2] == hand[8]:
        winningHandx5 = True

    elif hand[0] == hand[1] == hand[2] or hand[5] == hand[6] == hand[7] or hand[10] == hand[11] == hand[12] or hand[0] == hand[6] == hand[12] or hand[10] == hand[6] == hand[2]:
        winningHandx3 = True

    elif (hand[0] == hand[1] and hand[0] == "🍒") or (hand[5] == hand[6] and hand[5] == "🍒") or (hand[10] == hand[11] and hand[10] == "🍒") or (hand[0] == hand[6] and hand[0] == "🍒") or (hand[10] == hand[6] and hand[10] == "🍒"):
        winningHandx2 = True

    elif hand.count("⭐") == 3:
        winningHandx3 = True
    
    elif hand.count("⭐") == 4:
        winningHandx4 = True

    elif hand.count("⭐") == 5:
        winningHandx5 = True

    #
    if winningHandx2:
        print("x2")
        doubleDown = input("D. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            should_break = False
            prize = bet * 2
            while True:
                index = 1
                print(f"Moara {index}")
                if len(cardsDealt) >= 5:
                    print(f"Previous Cards: {cardsDealt[-5]}  {cardsDealt[-4]}  {cardsDealt[-3]}  {cardsDealt[-2]}  {cardsDealt[-1]}")
                elif len(cardsDealt) >= 4:
                    print(f"Previous Cards: {cardsDealt[-4]}  {cardsDealt[-3]}  {cardsDealt[-2]}  {cardsDealt[-1]}")
                elif len(cardsDealt) >= 3:
                    print(f"Previous Cards: {cardsDealt[-3]}  {cardsDealt[-2]}  {cardsDealt[-1]}")
                elif len(cardsDealt) == 2:
                    print(f"Previous Cards: {cardsDealt[-2]}  {cardsDealt[-1]}")
                elif len(cardsDealt) == 1:
                    print(f"Previous Cards: {cardsDealt[-1]}")
                else:
                    print("No cards have been picked")
                rosieNeagra = input("R. Rosie\nN. Neagra\nC. Collect Prize\n> ")
                if rosieNeagra.lower() == 'r':
                    randomChoice = "Rosie"
                elif rosieNeagra.lower() == 'n':
                    randomChoice = "Neagra"
                else:
                    budget += prize
                    print(f"Prize of {prize}$ has been collected!")
                    prizeCollected = True
                    index = 1
                    should_break = True
                    break
                randomKey = random.choice(list(cards.keys()))
                randomCard = random.choice(cards[randomKey])
                print(randomCard)
                cardsDealt.append(randomCard)
                if randomChoice == randomKey:
                    prize *= 2
                    index += 1
                    if index > 5:
                        budget += prize 
                        print(f"Maximum rounds reached! Prize of {prize}$ collected!")
                        prizeCollected = True 
                        index = 1
                        should_break = True
                        break
                else:
                    prize = 0
                    print("Prize lost")
                    index = 1
                    should_break = True
                    break

            if should_break:
                pass

        else:
            if not prizeCollected:
                prize = bet * 2
                budget += prize
                print(f"Collected {prize}")
    #

    #
    if winningHandx3:
        print("x3")
        doubleDown = input("D. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            should_break = False
            prize = bet * 3
            while True:
                index = 1
                print(f"Moara {index}")
                if len(cardsDealt) >= 5:
                    print(f"Previous Cards: {cardsDealt[-5]}  {cardsDealt[-4]}  {cardsDealt[-3]}  {cardsDealt[-2]}  {cardsDealt[-1]}")
                elif len(cardsDealt) >= 4:
                    print(f"Previous Cards: {cardsDealt[-4]}  {cardsDealt[-3]}  {cardsDealt[-2]}  {cardsDealt[-1]}")
                elif len(cardsDealt) >= 3:
                    print(f"Previous Cards: {cardsDealt[-3]}  {cardsDealt[-2]}  {cardsDealt[-1]}")
                elif len(cardsDealt) == 2:
                    print(f"Previous Cards: {cardsDealt[-2]}  {cardsDealt[-1]}")
                elif len(cardsDealt) == 1:
                    print(f"Previous Cards: {cardsDealt[-1]}")
                else:
                    print("No cards have been picked")
                rosieNeagra = input("R. Rosie\nN. Neagra\nC. Collect Prize\n> ")
                if rosieNeagra.lower() == 'r':
                    randomChoice = "Rosie"
                elif rosieNeagra.lower() == 'n':
                    randomChoice = "Neagra"
                else:
                    budget += prize
                    print(f"Prize of {prize}$ has been collected!")
                    prizeCollected = True
                    index = 1
                    should_break = True
                    break
                randomKey = random.choice(list(cards.keys()))
                randomCard = random.choice(cards[randomKey])
                print(randomCard)
                cardsDealt.append(randomCard)
                if randomChoice == randomKey:
                    prize *= 2
                    index += 1
                    if index > 5:
                        budget += prize 
                        print(f"Maximum rounds reached! Prize of {prize}$ collected!")
                        prizeCollected = True 
                        index = 1
                        should_break = True
                        break
                else:
                    prize = 0
                    print("Prize lost")
                    index = 1
                    should_break = True
                    break

            if should_break:
                pass

        else:
            if not prizeCollected:
                prize = bet * 3
                budget += prize
                print(f"Collected {prize}")
    #

    #
    if winningHandx4:
        print("x4")
        doubleDown = input("D. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            should_break = False
            prize = bet * 4
            while True:
                index = 1
                print(f"Moara {index}")
                if len(cardsDealt) >= 5:
                    print(f"Previous Cards: {cardsDealt[-5]}  {cardsDealt[-4]}  {cardsDealt[-3]}  {cardsDealt[-2]}  {cardsDealt[-1]}")
                elif len(cardsDealt) >= 4:
                    print(f"Previous Cards: {cardsDealt[-4]}  {cardsDealt[-3]}  {cardsDealt[-2]}  {cardsDealt[-1]}")
                elif len(cardsDealt) >= 3:
                    print(f"Previous Cards: {cardsDealt[-3]}  {cardsDealt[-2]}  {cardsDealt[-1]}")
                elif len(cardsDealt) == 2:
                    print(f"Previous Cards: {cardsDealt[-2]}  {cardsDealt[-1]}")
                elif len(cardsDealt) == 1:
                    print(f"Previous Cards: {cardsDealt[-1]}")
                else:
                    print("No cards have been picked")
                rosieNeagra = input("R. Rosie\nN. Neagra\nC. Collect Prize\n> ")
                if rosieNeagra.lower() == 'r':
                    randomChoice = "Rosie"
                elif rosieNeagra.lower() == 'n':
                    randomChoice = "Neagra"
                else:
                    budget += prize
                    print(f"Prize of {prize}$ has been collected!")
                    prizeCollected = True
                    index = 1
                    should_break = True
                    break
                randomKey = random.choice(list(cards.keys()))
                randomCard = random.choice(cards[randomKey])
                print(randomCard)
                cardsDealt.append(randomCard)
                if randomChoice == randomKey:
                    prize *= 2
                    index += 1
                    if index > 5:
                        budget += prize 
                        print(f"Maximum rounds reached! Prize of {prize}$ collected!")
                        prizeCollected = True 
                        index = 1
                        should_break = True
                        break
                else:
                    prize = 0
                    print("Prize lost")
                    index = 1
                    should_break = True
                    break

            if should_break:
                pass

        else:
            if not prizeCollected:
                prize = bet * 4
                budget += prize
                print(f"Collected {prize}")
    #

    #
    if winningHandx5:
        print("x5")
        doubleDown = input("D. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            should_break = False
            prize = bet * 5 
            while True:
                index = 1
                print(f"Moara {index}")
                if len(cardsDealt) >= 5:
                    print(f"Previous Cards: {cardsDealt[-5]}  {cardsDealt[-4]}  {cardsDealt[-3]}  {cardsDealt[-2]}  {cardsDealt[-1]}")
                elif len(cardsDealt) >= 4:
                    print(f"Previous Cards: {cardsDealt[-4]}  {cardsDealt[-3]}  {cardsDealt[-2]}  {cardsDealt[-1]}")
                elif len(cardsDealt) >= 3:
                    print(f"Previous Cards: {cardsDealt[-3]}  {cardsDealt[-2]}  {cardsDealt[-1]}")
                elif len(cardsDealt) == 2:
                    print(f"Previous Cards: {cardsDealt[-2]}  {cardsDealt[-1]}")
                elif len(cardsDealt) == 1:
                    print(f"Previous Cards: {cardsDealt[-1]}")
                else:
                    print("No cards have been picked")
                rosieNeagra = input("R. Rosie\nN. Neagra\nC. Collect Prize\n> ")
                if rosieNeagra.lower() == 'r':
                    randomChoice = "Rosie"
                elif rosieNeagra.lower() == 'n':
                    randomChoice = "Neagra"
                else:
                    budget += prize
                    print(f"Prize of {prize}$ has been collected!")
                    prizeCollected = True
                    index = 1
                    should_break = True
                    break
                randomKey = random.choice(list(cards.keys()))
                randomCard = random.choice(cards[randomKey])
                print(randomCard)
                cardsDealt.append(randomCard)
                if randomChoice == randomKey:
                    prize *= 2
                    index += 1
                    if index > 5:
                        budget += prize 
                        print(f"Maximum rounds reached! Prize of {prize}$ collected!")
                        prizeCollected = True 
                        index = 1
                        should_break = True
                        break
                else:
                    prize = 0
                    print("Prize lost")
                    index = 1
                    should_break = True
                    break

            if should_break:
                pass

        else:
            if not prizeCollected:
                prize = bet * 5
                budget += prize
                print(f"Collected {prize}") 
    #

    #
    if winningHandx10:
        print("x10")
        doubleDown = input("D. Double down\nC. Collect prize\n> ")
        if doubleDown.lower() == "d":
            should_break = False
            prize = bet * 10
            while True:
                index = 1
                print(f"Moara {index}")
                if len(cardsDealt) >= 5:
                    print(f"Previous Cards: {cardsDealt[-5]}  {cardsDealt[-4]}  {cardsDealt[-3]}  {cardsDealt[-2]}  {cardsDealt[-1]}")
                elif len(cardsDealt) >= 4:
                    print(f"Previous Cards: {cardsDealt[-4]}  {cardsDealt[-3]}  {cardsDealt[-2]}  {cardsDealt[-1]}")
                elif len(cardsDealt) >= 3:
                    print(f"Previous Cards: {cardsDealt[-3]}  {cardsDealt[-2]}  {cardsDealt[-1]}")
                elif len(cardsDealt) == 2:
                    print(f"Previous Cards: {cardsDealt[-2]}  {cardsDealt[-1]}")
                elif len(cardsDealt) == 1:
                    print(f"Previous Cards: {cardsDealt[-1]}")
                else:
                    print("No cards have been picked")
                rosieNeagra = input("R. Rosie\nN. Neagra\nC. Collect Prize\n> ")
                if rosieNeagra.lower() == 'r':
                    randomChoice = "Rosie"
                elif rosieNeagra.lower() == 'n':
                    randomChoice = "Neagra"
                else:
                    budget += prize
                    print(f"Prize of {prize}$ has been collected!")
                    prizeCollected = True
                    index = 1
                    should_break = True
                    break
                randomKey = random.choice(list(cards.keys()))
                randomCard = random.choice(cards[randomKey])
                print(randomCard)
                cardsDealt.append(randomCard)
                if randomChoice == randomKey:
                    prize *= 2
                    index += 1
                    if index > 5:
                        budget += prize 
                        print(f"Maximum rounds reached! Prize of {prize}$ collected!")
                        prizeCollected = True 
                        index = 1
                        should_break = True
                        break
                else:
                    prize = 0
                    print("Prize lost")
                    index = 1
                    should_break = True
                    break

            if should_break:
                pass

        else:
            if not prizeCollected:
                prize = bet * 10
                budget += prize
                print(f"Collected {prize}")
    #

    if budget <= 0:
        print("You ran out of money")
        addMore = input("1. Reinsert budget\n2. Exit completely\n> ")
        if addMore == "1":
            print("New Game!")
            cardsDealt = []
            budget = int(input("Reinsert Budget\n> "))
            bet = int(input("Choose your bet\n> ")) 
        else:
            print("Thanks for your time and money :)))))")
            exit()
    

    


