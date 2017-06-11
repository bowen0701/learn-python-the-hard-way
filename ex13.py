"""Parameters, Unpacking, Variables."""

from sys import argv

# Run scripts with 4 variables.
script, first, second, third, last = argv

last_last = raw_input("Your one more variable is:")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your last variable is:", last

print "Your one more variable is:", last_last
