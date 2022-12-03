# day1 part 2

with open('data/day1.txt') as f:
    calories = 0
    sums = []
    for line in f.readlines():
        try:
            calories = calories + int(line)
        except:
            sums.append(calories)
            calories = 0

winners = sorted(sums, reverse=True)
print(f"The sum of the top 3 is {sum(winners[0:3])}")

