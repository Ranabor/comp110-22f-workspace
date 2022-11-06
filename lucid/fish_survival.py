"""Correct"""
num_input = input()
fish_events_pop = tuple(map(int, num_input.split(' ')))

fish_pop = int(fish_events_pop[0])
fish_events = int(fish_events_pop[1])

def event_fish(t, num):
    global fish_pop
    num_int = int(num)
    if t == "G":
        fish_pop += num_int
    elif t == "P":
        fish_pop -= (fish_pop%num_int)



for i in range(fish_events):
    event = input()
    mapping = tuple(map(str, event.split(' ')))
    event_fish(mapping[0], mapping[1])

print(fish_pop)