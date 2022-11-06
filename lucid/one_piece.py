"""Incorrect"""
#a one piece reference :O
country_count = int(input())
pirates = []

for i in range(country_count):
    c_list = tuple(map(str, input().split(',')))
    for m in c_list:
        pirates.append(m)

most_wanted = []

for j in pirates:
    k = 0
    bounty_count = 0
    while k < len(pirates):
        if j == pirates[k]:
            bounty_count += 1
        k += 1
    if bounty_count == country_count:
        most_wanted.append(j)
    pirates.remove(j)

sort_list = sorted(most_wanted)

for pirate in sort_list:
    print(pirate)