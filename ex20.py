"""Functions and Files."""

# From sys import agrv
from sys import argv

# Input ex20.py, ex20.txt as argv
script, input_file = argv

# Define a function: read and then print file
def print_all(f):
	print f.read()

# Since we cannot read file twice, rewind the file to the origin
def rewind(f):
	f.seek(0)

# Pring line id and its content
def print_a_line(line_count, f):
	print line_count, f.readline()

# Re-open file (thus we need to rewind it)
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kine of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(1, current_file)

#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)



