# return index of input 'index' from list 'xs'; if not found, return 'response'
def get(xs, index, response=None):
    # try returning the 'index' of list xs
    try:
        return xs[index]
    # if an error occurs, return response
    except:
        return response

# classifies the inputted string into two separate lists of ints and strings
def classify(input_string):

    nums = []
    words = []

    if input_string:

        input_list = input_string.split(" ")

        for i in input_list.copy():
            try:
                nums.append(int(i))
            except:
                if i == "":
                    input_list.remove(i)
                else:
                    words.append(i)
    input_tuple = (nums, words)
    return input_tuple

# updates product inventory but returns a ValueError if the product's value goes
# below 0
def shelve(inventory, product_list):

    for i in product_list:
        if i[0] in inventory:
            val_sum = i[1] + inventory[i[0]]
            inventory.update({i[0]: val_sum})
        elif i[0] not in inventory:
            inventory.update({i})

    for i in inventory:
        if inventory[i] < 0:
            raise ValueError("negative amount for {}".format(i))