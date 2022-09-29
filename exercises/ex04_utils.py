"""EX 4 List Utils."""

__author__: str = "730575704"


def all(int_list: list[int], chosen: int) -> bool:
    """Takes list and int and if all of list values are equal to int, returns True."""
    i = 0
    if len(int_list) == 0:  # Ensures if list is empty returns false
        return False
    while i < len(int_list):  # Loops through list, if nested condition is not met then false. If loop ends then true
        if int_list[i] == chosen:  # Checking int vs list item
            i += 1
        else:
            return False
    return True


def max(int_list: list[int]) -> int:
    """Finds the highest value in a list."""
    if len(int_list) == 0:  # Raises error for empty list
        raise ValueError("max() arg is an empty List")
    i = 0
    highest = int_list[0]  # Sets variable to track the largest item
    while i < len(int_list):  # Loops through list
        if highest < int_list[i]:  # If item that is found is greater than current value of variable, reassigns
            highest = int_list[i]
        i += 1
    return highest  # Outputs highest assigned value as it will be the current value of highest variable


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns True if both lists are deeply equal."""
    i = 0
    if len(list1) != len(list2):  # If length not equal, gives false
        return False
    while i < len(list1):  # Loops through one list
        if list1[i] != list2[i]:  # If value at same index in both lists is not the same then lists are not deeply equal
            return False
        else:
            i += 1
    return True

print(is_equal([], []))
