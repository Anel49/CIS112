# creates a dictionary with years as the keys and lists as the values containing
# tuples detailing storms and their data for that year
def read_file(filename):

    storm_dict = {}
    data = []

    with open(filename, "r") as f:
        for line in f:
            data.append(line.strip())

    for i in data[1:]:
        # assigns variables for the list items split by ","
        y, n, mp, g, c, d, dm = i.split(",")

        # converts YEAR, CATEGORY, deaths, and DamageMillions to integers
        y, c, d, dm = int(y), int(c), int(d), int(dm)

        # if the year is already a key in the dictionary, append tuple to year's
        # list value, else add the year as a dictionary key followed by a list
        # as the value containing the storm tuple
        if y in storm_dict:
            storm_dict[y].append((n, c, d, dm))
        else:
            storm_dict[y] = [(n, c, d, dm)]

    return storm_dict

# adds or updates storm data
def add_storm(db, y, n, c, d, dm):

    # if the year is already a key in the dictionary, append tuple to year's
    # list value, else add the year as a dictionary key followed by a list
    # as the value containing the storm tuple
    if y in db:
        db[y].append((n, c, d, dm))
    else:
        db[y] = [(n, c, d, dm)]

# merges storm dictionaries into one and alphabetically and chronologically
# sorts the list tuples and year keys
def merge_databases(db1, db2):

    # if year i in 'db2' is found in 'db1', append tuple to key's list items,
    # else update 'db1' with 'db2'
    for y in db2:
        if y in db1:
            for j in db2[y]:
                db1[y].append(j)
        else:
            db1.update(db2)

    for val in db1:
        db1[val].sort()

    sorted_db1 = {}

    for y in sorted(db1):
        sorted_db1.update({y: db1[y]})

    return sorted_db1

# returns the key, value pair of the storm in 'db' that matches 'name'
def storms_by_name(db, name):

    named_db = {}

    # searches "db's" years for the inputted 'name' and, if found, updates
    # 'named_db' with the year as the key and the tuple in a list as the value
    for y in db:
        for t in db[y]:
            if name in t:
                named_db.update({y: [(t)]})

    return named_db

# returns all storms from 'db' matching 'years'
def storms_by_years(db, years):

    temp = {}
    storm_years = {}

    # iterates through the input 'years', checking if i == years and, if so,
    # updates 'temp' with db's key and values
    for year in years:
        for y in db:
            if year == y:
                temp.update({y: db[y]})
    # updates and returns 'storm_years' in the format of a sorted 'db', in case
    # the years inputted were out of chronological order
    for y in sorted(temp):
        storm_years.update({y: db[y]})

    return storm_years

# returns all storms from 'db' matching 'categories'
def storms_by_categories(db, categories):

    temp = {}
    sorted_storms = {}

    # for all categories in the 'categories' list, by year in 'db', find tuple's
    # index 1 (category) and check if it's equal to 'categories'; if it is,
    # check if 'temp' has the year already in it; if it does, append it to
    # "temp's" year list as a tuple, else create the key and value with the
    # tuple inside a list
    for c in categories:
        for y in db:
            for t in db[y]:
                if c == t[1]:
                    if y in temp:
                        temp[y].append(t)
                    else:
                        temp.update({y: [t]})

    # for loops first sort the tuples alphabetically and then updates
    # 'sorted_storms' with a sorted 'temp'
    for t in temp:
        temp[t].sort()
    for y in sorted(temp):
        sorted_storms.update({y: temp[y]})

    return sorted_storms

# returns the costliest storm in 'db'
def costliest_storm(db):

    max = 0

    # for year in 'db', if tuple index 3 (damage in millions) is bigger than
    # 'max', set 'max' to index 3 and assign 'costliest' to the year and tuple
    # of current iteration
    for y in db:
        for t in db[y]:
            if t[3] > max:
                max = t[3]
                costliest = (y, (t))

    return costliest

# returns the deadliest storm in 'db'
def deadliest_storm(db):

    max = 0

    # for year in 'db', if tuple index 2 (deaths) is bigger than 'max', set
    # 'max' to index 2 and assign 'deadliest' to the year and tuple of current
    # iteration
    for y in db:
        for t in db[y]:
            if t[2] > max:
                max = t[2]
                deadliest = (y, (t))

    return deadliest

# calculates and returns the costliest year in 'db'
def costliest_year(db):

    hold = {}
    
    # for each year's tuple in 'db', add index 3 (damage in millions) to the
    # last
    for y in db:
        num = 0
        for t in db[y]:
            num += t[3]
        # update 'hold' with year and sum of the damage in millions numbers
        hold.update({y: num})

    # resets num for next loop
    num = 0

    # for each year, if the year's value is larger than 'num', assign
    # 'costliest_y' to the year and 'num' to the year's value
    for year in hold:
        if hold[year] > num:
            costliest_y = year
            num = hold[year]

    return costliest_y

# calculates and returns the deadliest year in 'db'
def deadliest_year(db):

    hold = {}

    # for each year's tuple in 'db', add index 2 (deaths) to the
    # last
    for y in db:
        num = 0
        for t in db[y]:
            num += t[2]

        hold.update({y: num})

    # resets num for next loop
    num = 0

    # for each year, if the year's value is larger than 'num', assign
    # 'deadliest_y' to the year and 'num' to the year's value
    for year in hold:
        if hold[year] > num:
            deadliest_y = year
            num = hold[year]

    return deadliest_y

# returns the deadliest storm of 'db' in the inputted category
def deadliest_in_category(db, category):

    max = 0

    # for year in 'db', if category equals tuple index 1 (category), and if tuple
    # index 2 is bigger than max, assign 'max' to tuple index 2 (deaths) and
    # 'deadliest_cat' to the year and tuple of current iteration
    for y in db:
        for t in db[y]:
            if category == t[1]:
                if t[2] > max:
                    max = t[2]
                    deadliest_cat = (y, t)

    return deadliest_cat

# returns the costliest storm of 'db' in the inputted category
def costliest_in_category(db, category):

    max = 0

    # for year in 'db', if category equals tuple index 1 (category), and if tuple
    # index 3 is bigger than max, assign 'max' to tuple index 3 (damage in
    # millions) and 'costliest_cat' to the year and tuple of current iteration
    for y in db:
        for t in db[y]:
            if category == t[1]:
                if t[3] > max:
                    max = t[3]
                    costliest_cat = (y, t)

    return costliest_cat

# calculates and orders years in 'db' by most deaths and outputs the years in
# descending (highest to lowest deaths) in order
def years_by_deadliness(db):

    nums = []
    year_data = []
    desc_deadliness = []
    
    # sets sum to 0 and resets for each 'y' in 'db', adds index 2 (deaths) of t
    # to the variable 'sum' for each iteration, after which 'sum' is appended to
    # 'nums' and the year and corresponding 'sum' are appended to 'year_data'
    for y in db:
        sum = 0
        for t in db[y]:
            sum += t[2]
        nums.append(sum)
        year_data.append((y, sum))

    # sorts 'nums' in reverse, as specified in the instructions
    nums.sort(reverse = True)

    # compares the numbers in 'nums' with index 1 of 'year_data' and, if it
    # equals index 1, and the year is not found in 'desc_deadliness', appends
    # the year to 'desc_deadliness'
    for n in nums:
        for y in year_data:
            if n == y[1]:
                if y[0] not in desc_deadliness:
                    desc_deadliness.append(y[0])

    return desc_deadliness