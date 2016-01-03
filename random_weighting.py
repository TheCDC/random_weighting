# Hurr durr import random.
import random
import matplotlib.pyplot as plt

# Let's figure out how to do this thing!
def research():
	print("Let's do research!")
	# Make a list from 1 (inclusive) to n (inclusive)
	n = 10
	whatever_items = [i for i in range (1,n + 1)]
	print("Items: {}".format(whatever_items))
	# Make the weights simply a function of the indices of the whatever_items.
	# In this case f(i)=(i+1)^2.
	# This kind of a function should make it easier to see if we are correct.
	# Start at 1 because we don't want to first item having a probablility of 0.
	# That would be lame.
	def f(i):
		x = i + 1
		return x**2

	myweights = list(map(f,range(len(whatever_items))))
	print("Weights: {}".format(myweights))

	# Think of what we are doing as making a line,
	# each item will have its own length along the line.
	# All we have to do is pick one place along that line, 
	# that place corresponds to an item.
	# The length of that line is simply the sum of the weights.
	range_max = sum(myweights)
	print("Max of range (sum of weights): {}".format(range_max))

	# Get a random float from [0.0 1.0].
	the_number = random.random()

	# make a selection along the line of items
	cursor = the_number * range_max

	# Now get the item that is under the "cursor."
	selected = 0
	mysum = 0
	for i in range(len(myweights)):
		# This part is tricky.
		# All you have to do is check if the cursor is within the range of one item.
		# Slice the weights properly.
		if cursor >= sum(myweights[0:i]) and cursor < sum(myweights[0:i+1]):
			selected = whatever_items[i]
		else:
			mysum += myweights[i]
	print("Selected: {}".format(selected))

# Now to make it a function that accepts arbitrary items and weights.
# This function is the primary goal of this program.
def weighted_random(things, weights):
	# The list of items and list of weights must be the same. Hurr durr.
	assert len(things) == len(weights)
	range_max = sum(weights)
	the_number = random.random()
	cursor = the_number * range_max
	for i in range(len(weights)):
		if cursor >= sum(weights[0:i]) and cursor < sum(weights[0:i+1]):
			return things[i]
	else:
		# Raise an error something if no match is found.
		# I don't know why that would happen.
		raise ValueError

# Self explanatory name.
def do_tests():
	# Redefine items and weights.
	n = 10
	whatever_items = [i for i in range (1,n + 1)]
	# Let's try a rising sawtooth shaped distribution.
	myweights = [1,2,1,3,1,4,1,5,1,6]
	
	# Let's run it a bunch of times. How about n*x times?
	# x should be big (>100ish)to ensure an approximnately correct distribution.
	x = 100
	test_output = sorted([weighted_random(whatever_items, myweights) \
	 for i in range(len(whatever_items)*x)])
	print("Given the following items and weights:\n{},"
		.format('\n'.join(str(i) for i in zip(whatever_items,myweights))))
	print("{num_items} items were selected as follows:"
		.format(num_items=len(test_output)))

	xs = whatever_items[:]
	# The occurence counts.
	ys = [test_output.count(i) for i in whatever_items]
	print('\n'.join([str(i) for i in zip(xs,ys)]))

	# Maybe we could even plot it!
	plt.figure()
	plt.plot(xs,ys)
	plt.show()

def main():
	research()
	print("Now to do it for real.")
	do_tests()

if __name__ == '__main__':
	main()
