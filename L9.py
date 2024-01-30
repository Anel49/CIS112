# counts the first key found in 'xs' and adds to the counter if a duplicate is
# found afterwards
def counts(xs):

    xsd = {}

    for i in xs:
        if i in xsd:
            xsd[i] += 1
        else:
            xsd[i] = 1
    return xsd

# finds values in 'plants_d' equal to 'weekly' and returns their keys as a list
# in alphabetical order
def weeklies(plants_d):

    plants_list = []

    for i in sorted(plants_d):
        if plants_d[i] == 'weekly':
            plants_list.append(i)
    return plants_list

# calculates which dictionary entry of the correct location has the smallest
# distance from input 'here'
def closest(d, what, here):

    start = float()

    for i in d:
        if d[i] == what:
            if not start:
                start = ((i[0]-here[0])**2 + (i[1]-here[1])**2)**0.5
                nearest = i
            elif start:
                num = ((i[0]-here[0])**2 + (i[1]-here[1])**2)**0.5
                if num < start:
                    nearest = i

    if what not in d.values():
        return None
    return nearest

# sends a written file to function 'counts'
def file_counts(filename):

    with open(filename, "r") as f:
        nums = counts("".join(f).split("\n"))
        del nums[""]
        res = {}

        for i in nums:
            res[int(i)] = nums[i]
        return res