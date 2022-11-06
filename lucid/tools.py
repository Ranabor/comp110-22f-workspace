"""Correct"""
tools = tuple(map(str, input().split(', ')))
tool_count = tuple(map(int, input().split(', ')))
tool_dict = {}

j = 0
for i in tools:
    tool_dict[i] = tool_count[j]
    j += 1

jobs_available_count = int(input())
jobs_available = {}

for i in range(jobs_available_count):
    job_name = input()
    jobs_tools = tuple(map(str, input().split(', ')))
    job_tool_count = tuple(map(int, input().split(', ')))
    job_tools_dict = {}
    k = 0
    for l in jobs_tools:
        job_tools_dict[l] = job_tool_count[k]
        k += 1
    jobs_available[job_name] = job_tools_dict

jobs_doable = []

def possible(tools_on_hand, tools_needed):
    for i in tools_needed:
        if i not in tools_on_hand:
            return False
        else:
            if tools_needed[i] > tools_on_hand[i]:
                return False
    return True

for m in jobs_available:
    can_do = possible(tool_dict, jobs_available[m])
    if can_do == True:
        jobs_doable.append(m)

alpha_jobs_doable = sorted(jobs_doable)

for job in alpha_jobs_doable:
    print(job)