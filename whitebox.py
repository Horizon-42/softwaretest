from stack import Stack


def compute_rp(rp, values):
    op1 = {'~': lambda x: -x}
    op2 = {'+': lambda y, x: x + y, '-': lambda y, x: x - y,
           '/': lambda y, x: x/y, '*': lambda y, x: x*y}
    res = Stack()
    for char in rp:
        if char in op1:
            assert not res.is_empty()
            res.push(op1[char](res.pop()))
        elif char in op2:
            assert not res.is_empty()
            res.push(op2[char](res.pop(), res.pop()))
        else:
            assert char.is_digit()
            res.push(values[char])
    assert res.size() == 1
    return res.pop()


def test():
    pass


if __name__ == '__main__':
    test()
