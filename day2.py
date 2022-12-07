# day2 parts 1 and 2

from functools import reduce

# Map instructions to values of rock, paper, scissors
value_map = {
    'A': 1, 'X': 1,
    'B': 2, 'Y': 2,
    'C': 3, 'Z': 3,
    }

# Define winning games based on values played by opponent, me
my_wins = set([(1, 2), (2, 3), (3, 1)])

def is_my_win(*pair):
    return pair in my_wins

def score(opponent_move, my_move):
    """Score a game with play values"""
    if opponent_move == my_move:
        outcome = 3
    elif is_my_win(opponent_move,  my_move):
        outcome = 6
    else:
        outcome = 0
    return outcome + my_move

def solve(strategy):
    """
    Run through the input move instructions and sum scores
    using the given strategy
    """
    total = 0
    with open('data/day2.txt') as f:
        for line in f.readlines():
            moves = strategy(*line.split())
            total = total + score(*moves)
    return total


# Create a map to find my move value given opponent move and advice
# X means lose, Y means draw, Z means win
my_moves = {
    'A': {'X': 3, 'Y': 1, 'Z': 2},
    'B': {'X': 1, 'Y': 2, 'Z': 3},
    'C': {'X': 2, 'Y': 3, 'Z': 1},
}


if __name__ == "__main__":
    print(f"Part 1: {solve(lambda c1, c2: (value_map[c1], value_map[c2]))}")
    print(f"Part 2: {solve(lambda c1, c2: (value_map[c1], my_moves[c1][c2]))}")
