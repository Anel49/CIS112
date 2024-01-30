
def show_time(hour, min):

    times = [hour, min]
    times = list(map(int, times))
    hour = times[0]
    min = str(times[1])

    if 0 <= times[0] < 12:
        end = 'am'
    else:
        end = 'pm'

    if 12 < times[0] < 24:
        hour = times[0] - 12

    if times[0] == 0:
        hour = 12

    hour = str(hour)

    if 0 <= times[1] <= 9:
        min = '0' + min
        return('{}'':''{}{}'.format(hour, min, end))
    else:
        min = str(times[1])
        return('{}'':''{}{}'.format(hour, min, end))

# function to split a price evenly with the number of people involved
def split_up(funds, people):

    lst = [funds, people]
    shares = lst[0] / lst[1]
    return ('each person (of %d) gets $%.2f as their share' % (lst[1], shares))

# function to draw a box around the inputted text
def border_msg(msg):
    lst = msg
    lst = list(lst.split('\n'))
    maxi = len(lst[0])

    for i in lst:
        if len(i) > maxi:
            maxi = len(i)

    length = maxi
    lst2 = []

    for i in lst:
        lst2.append(f'| {i:^{length}} |')
    
    lst2.insert(0, '+-' + '-' * length + '-+')
    lst2.append('+-' + '-' * length + '-+\n')
    sep = '\n'
    lst2 = sep.join(lst2)
    return (lst2)
































