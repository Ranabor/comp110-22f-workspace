"""EX 5 Utils."""

__author__: str = "730575704"


def only_evens(all_list: list[int]) -> list[int]:
    """Taking a list, returns a list of all the even values."""
    i: int = 0
    even_list: list[int] = []
    while i < len(all_list):
        if all_list[i] % 2 == 0:
            even_list.append(all_list[i])
        i += 1
    return even_list


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Taking 2 lists, returns a list that concatenates them."""
    i: int = 0
    j: int = 0
    both_list: list[int] = []
    while i < len(list1):
        both_list.append(list1[i])
        i += 1
    while j < len(list2):
        both_list.append(list2[j])
        j += 1
    return both_list


def sub(given_list: list[int], start: int, end: int) -> list[int]:
    """Given a list and start and end, returns a sublist with of those indices."""
    sub_list: list[int] = []
    if start < 0:  # Testing for and correcting argument values of start and end
        start = 0
    if end >= len(given_list):
        end = len(given_list)
    if end <= 0:  # Returning prematurely with specified arguments
        return []
    if start >= len(given_list):
        return []
    if len(given_list) == 0:
        return []
    while start < end:  # Appending based on range given in arguments
        sub_list.append(given_list[start])
        start += 1
    return sub_list