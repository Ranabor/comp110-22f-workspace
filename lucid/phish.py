# """Unfinished"""
# num_employee = int(input())
# employees = []
# for i in range(num_employee):
#     employee = input()
#     employees.append((employee.lower().replace(" ", "")))

# num_tests = int(input())
# test_cases = []
# for i in range(num_tests):
#     test = input()
#     test_cases.append(test.lower().replace(" ", ""))

def check(employees_list, test_case):
    for i in employees_list:
        employee_mutable = i
        align = 0         
        for j in test_case:
            k = 0
            while k < len(employee_mutable):
                if j == k:
                    align += 1
                    employee_mutable = employee_mutable[:k] + employee_mutable[(k+1):]
            k += 1
            
        return align

print(check(["ascs", "asdwd"], "as"))
    #         if i[j] == test_case[j]:
    #             checking_bools.append(False)
    #         else:
    #             checking_bools.append(True)
    #         j += 1
    #     if sum(checking_bools) == 0:
    #         return "EMPLOYEE"
    #     elif sum(checking_bools) == 1:
    #         return "BOT"
    # return "CUSTOMER"
    

# for i in test_cases:
#     print(check(employees, i))
