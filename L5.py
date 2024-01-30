
# searching for 'key' in the list 'xs'
def location(xs, key):

    for i in range(len(xs)):
        if xs[i] == key:
            return i
    return

# returns sum of fibonacci given the index 'n'
def fibonacci(n):

    fib = [1, 1]

    i = 0

    if n == 0 or n == 1:
        return fib[i]

    while i <= n:

        num = 0

        for i in range(n - 1):
            num = fib[i] + fib[i + 1]
            fib.append(num)
            i += 1
        return num

# returns the largest number for the squared input 'n' that doesn't exceed the
# following square root
def int_sqrt(n):

    for i in range(n + 1):
        if i * i == n:
            return i
        elif i * i > n:
            return (i - 1)

# adds even numbers in list xss' sub lists and returns the sum
def sum_evens_2d(xss):
    nums = []

    for i in xss:
        for j in i:
            if j % 2 == 0:
                nums.append(j)
    ans = 0

    for i in nums:
        ans += i

    return ans