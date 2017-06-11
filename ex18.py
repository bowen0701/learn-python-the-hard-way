"""Names, Variables, Code, Functions."""

# This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# OK, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# This just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# This takes no arguments
def print_none():
    print "I got nothin'."

print_two("Bowen", "Li")
print_two_again("Bowen", "Li")
print_one("Bowen")
print_none()
