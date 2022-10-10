"""EX07 Dictionary Utils."""

__author__ = "730575704"


def invert(dict_i: dict[str, str]) -> dict[str, str]:
    """Function to invert a dictionary's keys and values."""
    keys: list[str] = []
    values: list[str] = []
    for i in dict_i:
        keys.append(i)
        values.append(dict_i[i])
    j: int = 0
    while j < len(values):
        k: int = j + 1
        while k < len(values):
            if values[j] == values[k]:
                raise KeyError("Cannot have duplicate values.")
            k += 1
        j += 1
    result: dict[str, str] = {}
    counter: int = 0
    for val in values:
        result[val] = keys[counter]
        counter += 1
    return result


def favorite_color(dict_c: dict[str, str]) -> str:
    """Returns most common favorite color. First color if tie."""
    if dict_c == {}:
        return ""
    colors_dict: dict[str, int] = {}
    colors_dict_keys: list[str] = []
    for i in dict_c:
        colors_dict_keys.append(dict_c[i])
    for j in colors_dict_keys:
        if j in colors_dict:
            colors_dict[j] += 1
        else:
            colors_dict[j] = 1
    max_value: str = colors_dict_keys[0]
    for i in colors_dict:
        if colors_dict[i] > colors_dict[max_value]:
            max_value = i
    print(max_value)
    return max_value


def count(list_to_count: list[str]) -> dict[str, int]:
    """Counts unique values in list and makes a dict of them."""
    results: dict[str, int] = {}
    for i in list_to_count:
        if i in results:
            results[i] += 1
        else:
            results[i] = 1
    return results