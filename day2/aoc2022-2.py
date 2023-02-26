#A and X rock
#B and Y paper
#C and Z scissor
#Initiliaze variables and assigned values to each specific play and how the matches ends
rock = 1
paper = 2
scissor = 3
lose = 0
draw = 3
win = 6
score = 0

#Opens data file and stores it as a list which is split for each new line
my_file = open('./day2/aoc2022-2data.txt', 'r')
data = my_file.read()
data_list = data.split('\n')
my_file.close()

###Iterates through the data_list based on the conditions for the 9 possible options and assigns a point 
###value to it, which is then added into a score (sum)
for d in data_list:
    if d == 'A X':
        score += rock + draw
    elif d == 'A Y':
        score += paper + win
    elif d == 'A Z':
        score += scissor + lose
    elif d == 'B X':
        score += rock + lose
    elif d == 'B Y':
        score += paper + draw
    elif d == 'B Z':
        score += scissor + win
    elif d == 'C X':
        score += rock + win
    elif d == 'C Y':
        score += paper + lose
    elif d == 'C Z':
        score += scissor + draw
    else:
        raise Exception('invalid')
print(score)

#A rock     Y draw
#B paper    X lose
#C scissor  Z win
###Starts a new variable to hold the new sum
###Iterates through the list once again, but using the new set of conditionals giiven
score_new = 0
for d in data_list:
    if d == 'A X':
        score_new += scissor + lose
    elif d == 'A Y':
        score_new += rock + draw
    elif d == 'A Z':
        score_new += paper + win
    elif d == 'B X':
        score_new += rock + lose
    elif d == 'B Y':
        score_new += paper + draw
    elif d == 'B Z':
        score_new += scissor + win
    elif d == 'C X':
        score_new += paper + lose
    elif d == 'C Y':
        score_new += scissor + draw
    elif d == 'C Z':
        score_new += rock + win
    else:
        raise Exception('invalid')
print (score_new)