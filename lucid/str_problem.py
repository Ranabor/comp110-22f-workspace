"""Correct"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
entry = input()
score = 0

def find_AB(entry_str) -> str:
    new_str = entry_str
    i = 0
    while i < len(new_str):
        if new_str[i] == "A":
            if i == (len(new_str) - 1):
                return new_str
            if new_str[i + 1] == "B":
                new_str = new_str[:i] + "D" + new_str[i+2:]  
        i += 1
    return new_str

def find_C(entry_str_mod1):
    global score
    d_count = 0
    for i in entry_str_mod1:
        if i == "D":
            d_count += 1
    for i in entry_str_mod1:
        if i == "C":
            score -= (d_count ** 2)

def score_calc(entry_str_mod2):
    global score
    for i in entry_str_mod2:
        if i == "A":
            score += 1
        if i == "B":
            score += 2
        if i == "D":
            score += 4

result_str = str(find_AB(entry))
find_C(result_str)
score_calc(result_str)

print(score)