"""find the sum of all of the multiples of three and five up to some given number. Problem 1"""

def mult_3(num):
    if num %3 == 0:
        return True
    else:
        return False


def mult_5(num):
    if num %5 == 0:
        return True
    else:
        return False


def mult_3_or_5(num):
    mult_list = []
    for foo in range(0, num):
        if mult_3(foo) or mult_5(foo):
            mult_list.append(foo)
        else:
            pass

    prev = 0
    for foo in mult_list:
        bar = prev + foo
        prev = bar

    return prev


print("Sum of all multiples of 3 or 5 below 1000: " + str(mult_3_or_5(1000)))

def fibb_to(limit):
    """sums the even fibb numbers up to four million.
    needs an index limit to try out of laziness."""

    fibb_index = {1: 1, 2: 2}
    for k in range(3, limit):
        n = fibb_index[k-1] + fibb_index[k-2]
        fibb_index[k] = n

    summation = 0
    for foo in fibb_index.values():
        if foo % 2 == 0 and foo < 4000000:
            summation += foo
        elif foo > 4000000:
            print("limit reached!")
        else:
            pass

    return summation

print(fibb_to(400))


