
# finds all odd numbers in list 'xs', multiplies them together, and returns the
# product
def odd_product(xs):

    lst = []

    for i in xs:
        if i % 2 != 0:
            lst.append(i)

    prod = 1

    for i in lst:
        prod = prod * i

    return prod

# searches the list 'xs' for any duplicates without using the .count() function
# and returns a Boolean of True or False
def has_duplicates(xs):

    nums = []

    for i in xs:
        if i in nums:
            return True
        nums.append(i)

    return False

# returns the difference between the largest and smallest numbers in list 'nums'
# without using the min() or max() functions
def span(nums):
    if not nums:
        return 0

    maxi = nums[0]
    mini = nums[0]

    for i in range(len(nums)):
        if nums[i] > maxi:
            maxi = nums[i]
        elif nums[i] < mini:
            mini = nums[i]

    dist = maxi - mini
    return dist

# tests if a number is prime, removes the right digit through //, and returns
# Boolean True or False
def truncatable_prime(n):

        nc = n

        while nc:
            if nc == 1:
                return False
            for i in range(2, nc):
                if nc % i == 0:
                    return False
            nc = nc // 10
        return True

# removes duplicated elements of inputted list 'xs'
def remove_echo(xs):
    if not xs:
        return xs

    num = xs[0]
    xsc = []
    xsc.append(xs[0])

    for i in range(len(xs)):
        if xs[i] != num:
            xsc.append(xs[i])
            num = xs[i]

    return xsc

# function to return the second smallest number in the list without sorting with
# the .sort() method
def second_smallest(xs):

    xsc = xs[:]
    nums = []

    while xsc:
        mini = xsc[0]
        for i in xsc:
            if i < mini:
                mini = i
        
        nums.append(mini)
        xsc.remove(mini)

    return nums[1]