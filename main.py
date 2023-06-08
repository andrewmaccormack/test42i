# Assumption: we're dealing with ints, not floats (or a combo)
# Assumption: it is OK to remove all duplicates, not just 4
# Assumption: by reading numbers, we're going to read them 1 by 1 from console,
#             but could come from csv, api parameter, etc.
# Assumption: we'll output list using builtin python string representation
# Assumption: 1 to 100 is inclusive, for allowable numbers

def remove_duplicates(my_list):
    """
    Remove duplicated items from a list
    :param my_list: list of items of same type
    :return: de-duplicated list
    """
    return list(set(my_list))


def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 3, 3, 4, 4]) == [1, 2, 3, 4]
    assert remove_duplicates([1, 1, 1, 1, 1]) == [1]
    assert remove_duplicates([9, 9, 11, 11, 11]) == [9, 11]


class Input:
    def __init__(self, test_data=None):
        self.test_data = test_data

    def input(self, prompt):
        if self.test_data:
            return self.test_data.pop(0)
        else:
            return input(prompt)


def read_numbers(count, min_int, max_int, input_class):
    """ 
    :param count: how many numbers to read
    :param min_int: minimum allowed number
    :param max_int: maximum allowed number
    :param input_class: class that provides input method
    :return: list of <count> integers
    """
    numbers = []
    while len(numbers) < count:
        try:
            number = int(input_class.input('Enter a number: '))
            if min_int <= number <= max_int:
                numbers.append(number)
            else:
                print(f'Numbers must be between {min_int} and {max_int}, please')
        except ValueError:
            print('Numbers must be valid integers, please')
    return numbers


def test_read_numbers():
    input_list = ["4", "4", "44", "444", "-44", "7", "33", "fish", "100", "1", "0", "8", "1", "100"]
    expected_output = [100, 44, 33, 8, 7, 4, 1]
    assert read_numbers(10, 1, 100, Input(input_list)) == expected_output


if __name__ == '__main__':
    # Assignment: read list fo 10 numbers ranging between 1 to 100
    # Assuming there are 4 duplicates in the list of numbers,
    # output should remove the duplicates and sort teh remaining numbers
    # in descending order
    orig_numbers = read_numbers(10, 1, 100, Input())
    dedup_numbers = remove_duplicates(orig_numbers)
    print(f"Output: {sorted(dedup_numbers, reverse=True)}")
