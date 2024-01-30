# assigns 'best_time,' 'mid_time,' and 'last_time' with the shortest to fastest
# times spent to finish the activity in relation to a, b, and c
def get_times(alice_time, bob_time, carol_time):

	if alice_time <= bob_time <= carol_time:
		best_time = alice_time
		mid_time = bob_time
		last_time = carol_time
		return (best_time, mid_time, last_time)

	elif alice_time <= carol_time <= bob_time:
		best_time = alice_time
		mid_time = carol_time
		last_time = bob_time
		return (best_time, mid_time, last_time)

	elif bob_time <= alice_time <= carol_time:
		best_time = bob_time
		mid_time = alice_time
		last_time = carol_time
		return (best_time, mid_time, last_time)

	elif bob_time <= carol_time <= alice_time:
		best_time = bob_time
		mid_time = carol_time
		last_time = alice_time
		return (best_time, mid_time, last_time)

	elif carol_time <= alice_time <= bob_time:
		best_time = carol_time
		mid_time = alice_time
		last_time = bob_time
		return (best_time, mid_time, last_time)

	elif carol_time <= bob_time <= alice_time:
		best_time = carol_time
		mid_time = bob_time
		last_time = alice_time
		return (best_time, mid_time, last_time)

# compares numbers and assigns the smallest (fastest_name), middle
# (middle_name), and largest (slow_name) numbers to the strings 'Alice,' 'Bob,'
# or 'Carol'
def get_names(alice_time, bob_time, carol_time):

	a = alice_time
	b = bob_time
	c = carol_time

	# if the tuple order must be ("Alice", "Bob", "Carol")
	if (a == b == c) or (a < b < c) or (a == b < c) or (a < b == c):
		fastest_name = 'Alice'
		middle_name = 'Bob'
		slow_name = 'Carol'
		return (fastest_name, middle_name, slow_name)

	# if the tuple order must be ("Bob", "Carol", "Alice")
	elif b == c < a:
		fastest_name = 'Bob'
		middle_name = 'Carol'
		slow_name = 'Alice'
		return (fastest_name, middle_name, slow_name)

	# if the tuple order must be ("Carol", "Alice", "Bob")
	elif (c < a == b) or (c < a < b):
		fastest_name = 'Carol'
		middle_name = 'Alice'
		slow_name = 'Bob'
		return (fastest_name, middle_name, slow_name)

	# if the tuple order must be ("Alice", "Carol", "Bob")
	elif (a == c < b) or (a < c < b):
		fastest_name = 'Alice'
		middle_name = 'Carol'
		slow_name = 'Bob'
		return (fastest_name, middle_name, slow_name)

	# if the tuple order must be ("Bob", "Alice", "Carol")
	elif (b < a < c) or (b < a == c):
		fastest_name = 'Bob'
		middle_name = 'Alice'
		slow_name = 'Carol'
		return (fastest_name, middle_name, slow_name)

	# if the tuple order must be ("Bob", "Carol", "Alice")
	elif b < c < a:
		fastest_name = 'Bob'
		middle_name = 'Carol'
		slow_name = 'Alice'
		return (fastest_name, middle_name, slow_name)

	# if the tuple order must be ("Carol", "Bob", "Alice")
	elif c < b < a:
		fastest_name = 'Carol'
		middle_name = 'Bob'
		slow_name = 'Alice'
		return (fastest_name, middle_name, slow_name)

# compares numbers and increments top_rank, mid_rank, and last_rank (seen below)
# by 0, 1, or 2
def get_ranks(alice_time, bob_time, carol_time):

	top_rank = 1
	mid_rank = 1
	last_rank = 1

	a = alice_time
	b = bob_time
	c = carol_time

	if a == b == c:
		return(top_rank, mid_rank, last_rank)

	elif (a < b < c) or (b < a < c) or (b < c < a) or (c < b < a) or \
	(a < c < b):
		mid_rank += 1
		last_rank += 2
		return(top_rank, mid_rank, last_rank)

	elif (a == b < c) or (a == c < b):
		last_rank += 2
		return(top_rank, mid_rank, last_rank)

	elif (a < b == c) or (b < a == c):
		mid_rank += 1
		last_rank += 1
		return(top_rank, mid_rank, last_rank)