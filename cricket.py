# Write a code that prints out individual scores of two players in a game of cricket where score is given as runs per ball in an array. In a game of cricket a person changes strike if he scores an odd number, and keeps strike with him if he scores an even number. No need to consider changing strike after every 6 balls or an over.
# Sample Input1: [1,2]
# Output1: p1: 1, p2: 2
# Sample Input2: [1,2,3,2,1]
# Output2: p1: 4, p2: 5

# Code>>>

def cricket(runs_arr):
    player_scores = {True:0, False:0}    # True for p1, False for p2. Boolean is apt because there are two players
    strike = True
    for runs in runs_arr:
        player_scores[strike]+=runs
        if runs%2!=0:
            strike = not strike     # change strike
    print('p1',player_scores, 'p2',player_scores)
    return {'p1':player_scores[True], 'p2':player_scores[False]}

test1=cricket([1,2])
test2=cricket([1,2,3,2,1])