"""Prompting and Passing."""

from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I would like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "Do you think I am smart?"
smart = raw_input(prompt)

print """
All right, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
Finally, you think %r about I am smart. Thanks!
""" % (likes, lives, computer, smart)