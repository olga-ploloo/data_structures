def check_brackets(string_):
    _list = []
    _dict = {')': '(', ']': '[', '}': '{'}
    _index = []
    for n, i in enumerate(string_):
        if i in _dict.values():
            _list.append(i)
            _index.append(n+1)
        elif i in _dict.keys():
            if not _list or _dict[i] != _list.pop():
                # if wrong give out index of mistake
                return n+1
            else:
                _index.pop()
    if _list:
        # if wrong give out index of mistake
        return _index[-1]
    else:
        return 'Success'


def main():
    string_ = input()
    print(check_brackets(string_))


if __name__ == "__main__":

    assert check_brackets("([](){([])})") == 'Success'
    assert check_brackets("()[]}") == 5
    assert check_brackets("{{[()]]") == 7
    assert check_brackets("{{{[][][]") == 3
    assert check_brackets("{*{{}") == 3
    assert check_brackets("[[*") == 2
    assert check_brackets("{*}") == 'Success'
    assert check_brackets("{{") == 2
    assert check_brackets("{}") == 'Success'
    assert check_brackets("") == 'Success'
    assert check_brackets("}") == 1
    assert check_brackets("*{}") == 'Success'
    assert check_brackets("{{{**[][][]") == 3
