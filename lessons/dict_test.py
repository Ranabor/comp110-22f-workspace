def filter_keys(keys: list[str], full: dict[str, int]) -> dict[str, int]:
    result: dict[str, int] = {}
    for item in keys:
        result[item] = 0
    for i in full:
        if i in result:
            result[i] = full[i]
    return result

print(filter_keys(["a", "b"], {"a": 0, "b": 1, "c": 4}))