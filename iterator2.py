class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.new_lst_cursor = -1
        self.new_lst = []
        return self

    def __next__(self):
        if len(self.list_of_list) == 0:
            raise StopIteration

        self.new_lst_cursor += 1
        while True:
            i = self.list_of_list.pop(0)
            if isinstance(i, list):
                lst = []
                self.list_of_list = lst.extend(i) + self.list_of_list
            else:
                self.new_lst[self.new_lst_cursor] = i
                break


        return self.new_lst[self.new_lst_cursor]


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()