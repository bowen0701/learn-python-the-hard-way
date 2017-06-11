"""More Variables and Printing."""

his_name = 'Bowen Li'
his_age = 35  # Not a lie
his_height = 170  # cm
his_weight = 64  # KG
his_eyes = 'Brown'
his_teeth = 'White'
his_hair = 'Black'

print "Let's talk about %s." % his_name
print "I am %d cm tall." % his_height
print "I am %d KG heavy." % his_weight
print "Actually this is not too heavy."
print "I have got %s eyes and %s hair." % (his_eyes, his_hair)
print "his teeth are usually %s depending on the coffee." % his_teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
  his_age, his_height, his_weight, his_age + his_height + his_weight)

print "If I add %r, %r, and %r I get %r." % (
  his_age, his_height, his_weight, his_age + his_height + his_weight)