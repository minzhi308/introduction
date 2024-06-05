thief = 1
while thief <= 4:
    count_true = 0  # Counter for true statements
    # Check each suspect's statement
    if thief != 1:  # Suspect 1 said he is not the thief
        count_true += 1
    if thief == 3:  # Suspect 2 said 3 is the thief
        count_true += 1
    if thief == 4:  # Suspect 3 said 4 is the thief
        count_true += 1
    if thief != 4:  # Suspect 4 said 3 is a liar
        count_true += 1

    # Check if exactly three statements are true
    if count_true == 3:
        print('The true thief is', thief)
        break
    
    thief += 1

#會計系 H14126173 賈閔之
