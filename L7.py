# returns the passed arguments in ascending or descending order depending on the
# boolean provided
def rank3(x, y, z, ascending=True):

    temp = []
    temp.extend((x, y, z))

    if ascending == True:
        temp.sort()
    elif ascending == False:
        temp.sort(reverse=True)
    else:
        temp.sort()
    tup = tuple(temp)
    return tup

# removes ('limit') multiples of val from xs
def remove(val, xs, limit=None):

    xsc = xs[:]

    if limit == 0:
        xs = xs
    elif limit == None:
      for i in xsc:
        if val in xs:
          xs.remove(val)
    else:
        for i in range(limit):
            if val in xs:
                xs.remove(val)

# adds the same characters from 'keeps' found in 'msg' to a new string, unless
# keeps=None in which it will add only the alpha characters from 'msg'
def filter_chars(msg, keeps=None):

    mystr = ''

    if keeps != None:
        for i in msg:
            for j in keeps:
                if j in i:
                    mystr += j
                    break
    elif keeps == None:
        for i in msg:
            if i.isalpha():
                mystr += i
    return mystr

# relocates evens to new list
def relocate_evens(data, new_home=None):

    lst = data[:]

    if new_home == None:
        new_home = []

    for i in lst:
        if i % 2 == 0:
            data.remove(i)
            new_home.append(i)
    return new_home