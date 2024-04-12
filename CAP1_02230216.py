###############################
# Kunzang Lhamo
# your section
# 02230216
###############################
# References
#
# How to handle file
# https://www.dataquest.io/blog/read-file-python/#:~:text=Python%20provides%20a%20built%2Din,we%20can%20manipulate%20its%20content
# https://www.w3schools.com/python/python_file_open.asp
#
# Defining a function
# https://www.geeksforgeeks.org/python-functions/
#
###############################
# Solution
# Solution score:
# 50223
##############################
# Read the input_6_cap1.txt file
def read_input():
    # file should be closed after opening. So 'with' context manager ensure it closes the file.
    with open('input_6_cap1.txt', 'r') as f: 
        line = f.readline()#readline read the content of a text file one line at a time
        #while loop to read entire content line by line
        rounds = []
        while line:
            # Split the line into two parts and append them as a tuple to the rounds list
            rounds.append((line.split()[0], line.split()[1]))
            # Read the next line
            line = f.readline()
        return rounds    

# solution
def calculate_score(rounds):
    weapons = {'A': 1, 'B': 2, 'C': 3} # dictionary to store key value pairs
    round_result = {'X': 0, 'Y': 3, 'Z': 6} # dictionary to store key value pairs
    total_score = 0 # initialize total score
    # iterating through input_6_cap1.txt file
    for i in rounds:
        #assigning value for opponent value and result
        opponent_move, result = i
        #conditions for calculating the total score 
        if opponent_move == 'A' and result == 'X':
            your_move = 'C'
        elif opponent_move == 'A' and result == 'Y':
            your_move = 'A'
        elif opponent_move == 'A' and result == 'Z':
            your_move = 'B'
        elif opponent_move == 'B' and result == 'X':
            your_move = 'A'
        elif opponent_move == 'B' and result == 'Y':
            your_move = 'B'
        elif opponent_move == 'B' and result == 'Z':
            your_move = 'C'
        elif opponent_move == 'C' and result == 'X':
            your_move = 'B'
        elif opponent_move == 'C' and result == 'Y':
            your_move = 'C'
        elif opponent_move == 'C' and result == 'Z':
            your_move = 'A'  
        else:
            print('Word out of range')
        total_score += weapons[your_move] + round_result[result]
    return total_score

# call the function
rounds = read_input()
print(f"The total score is: {calculate_score(rounds)}")