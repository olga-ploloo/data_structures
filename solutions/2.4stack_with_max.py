def stack_with_max(_list):
    stack_ = []
    for i in _list:
        if len(i) > 3:
            val = int(i[5:])
            if stack_:
                stack_.append((val, max(val, stack_[-1][1])))
            else:
                stack_.append((val, val))
        elif i == 'pop':
            stack_.pop()
        elif i == 'max':
            print(stack_[-1][1])


def main():
    _list = []
    n = int(input())
    for i in range(n):
        _list.append(input())
    stack_with_max(_list)


if __name__ == "__main__":
    main()
