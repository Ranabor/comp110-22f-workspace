# def love(subject: str) -> str:
#     """Given...."""
#     return f"f*** {subject}"

# print(love("you"))

def mystery(n):
    i = 0
    while i < n:
        print(i)
        if i % 2 == 1:
            return "oo"
        i += 1
        print(i)
    return "aa"

print(mystery(4))