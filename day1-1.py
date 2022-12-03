# day1 part 1

with open('data/day1.txt') as f:
    winner = 0
    max = 0
    calories = 0
    elf = 1
    for line in f.readlines():
        try:
            calories = calories + int(line)
        except:
            if calories > max:
                max = calories
                winner = elf
            calories = 0
            elf = elf + 1

    print(f"Elf {winner} is carrying the heaviest load of {max}")