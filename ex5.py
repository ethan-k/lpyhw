# -- coding: utf-8

my_name = "Zed A. Shaw Kang king"
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

# 1 inch = 2.54 cm
my_height_cm = my_height * 2.54

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy" % my_weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair" % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee" % my_teeth


# this line is tricky, try to get it exactyl right
print "If I add %d, %d, and %d I get %d" % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

print "I LOVE %r %r" % ("Hayley", "Griffiths")
print "My height in cm is %d" % my_height_cm
print "Round : %d" % round(1.5555)
