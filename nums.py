input = input('enter a number between 0-9999: ')


one_words = [
    'one', 'two', 'three',
    'four', 'five', 'six',
    'seven', 'eight', 'nine'
]

ten_words = [
    'ten', 'twenty ', 'thirty ',
    'fourty ', 'fifty ', 'sixty ',
    'seventy ', 'eighty ', 'ninety '
]

teen_words = [
    'ten', 'eleven', 'twelve',
    'thirteen', 'fourteen', 'fifteen',
    'sixteen', 'seventeen', 'eighteen', 'nineteen'
]

one_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
one_nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
one_nums3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

my_list = []

#-------- NUMBERS 1-9 ---------#


def ones(num_1):
    if num_1 == 0:
        return 'zero'
    if num_1 > 0:
        for num in one_nums:
            if num_1 == num:
                return one_words[num - 1]

#-------- NUMBERS 10-99 ---------#


def tens(num_1, num_2):
    if num_1 == 1 and num_2 <= 9:
        for num in one_nums3:
            if num_2 == num:
                x = teen_words[num]
                my_list.append(x)

    if num_1 > 1:
        for num in one_nums:
            if num_1 == num:
                x = ten_words[num - 1]
                my_list.append(x)

    if num_1 > 1 and num_2 != 0:
        for num in one_nums2:
            if num_2 == num:
                y = one_words[num - 1]
                my_list.append(y)
                return ''.join(my_list)

    else:
        return ''.join(my_list)

#-------- NUMBERS 100-999 ---------#


def hundreds(num_1, num_2, num_3):
    if num_2 == 0 and num_3 == 0:
        result = ones(num_1)
        return f'{result} hundred'

    if num_2 == 0:
        result = ones(num_1)
        result_2 = ones(num_3)
        return f'{result} hundred {result_2}'

    if num_2 > 0 and num_2 <= 9:
        result = ones(num_1)
        result_2 = tens(num_2, num_3)
        return f'{result} hundred {result_2}'


#--------- NUMBERS 1000-9999 ----------#
def thousands(num_1, num_2, num_3, num_4):
    if num_2 == 0 and num_3 == 0 and num_4 == 0:
        result = ones(num_1)
        return f'{result} thousand'

    if num_2 == 0 and num_3 == 0 and num_4 > 0:
        result = ones(num_1)
        result_2 = ones(num_4)
        return f'{result} thousand {result_2}'

    if num_2 == 0 and num_3 > 0 and num_4 >= 0:
        result = ones(num_1)
        result_2 = tens(num_3, num_4)
        return f'{result} thousand {result_2}'

    if num_2 >= 0 and num_3 >= 0 and num_4 >= 0:
        result = ones(num_1)
        result_2 = hundreds(num_2, num_3, num_4)
        return f'{result} thousand {result_2}'


if len(input) == 1:
    print(ones(int(input)))

if len(input) == 2:
    a = int(input[0])
    b = int(input[1])
    print(tens(a, b))

if len(input) == 3:
    a = int(input[0])
    b = int(input[1])
    c = int(input[2])
    print(hundreds(a, b, c))

if len(input) == 4:
    a = int(input[0])
    b = int(input[1])
    c = int(input[2])
    d = int(input[3])
    print(thousands(a, b, c, d))
