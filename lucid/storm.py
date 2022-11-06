"""Correct"""

cond_1 = input()
cond_2 = input()
cond_3 = input()
cond_4 = input()

conds_list = [cond_1, cond_2, cond_3, cond_4]
conds_bool = []

def extract_bool(string_input):
    if "false" in string_input:
        return False
    else:
        return True

for i in conds_list:
    conds_bool.append(extract_bool(i))

print(sum(conds_bool))