class Stack(object):
    __slots__ = ('__items')

    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def size(self):
        return len(self.__items)

    def peek(self):
        return self.__items[len(self.__items)-1]

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()


if __name__ == '__main__':
    words = Stack()
    print(words.is_empty())
    words.push("fuck")
    print(words.size())
    words.push("world")
    print(words.size())
    print(words.peek())
    print(words.pop())
    print(words.peek())
