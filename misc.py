encode_dict = [
    {'Муж': 0, 'Жен': 1},
    {'Да': 0, 'Нет': 1},
    {1: 1, 2: 2, 3: 0},
    {'Cherbourg': 1, 'Queenstown': 2, 'Southampton': 0}]


def encode(gender, with_family, pclass, embarked):
    return encode_dict[0][gender], encode_dict[1][with_family], encode_dict[2][pclass], encode_dict[3][embarked]
