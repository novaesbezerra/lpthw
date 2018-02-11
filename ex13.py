from sys import argv
#import from the sys module

'''
the argv is the "argument variable". esta variavel holds 
the arguments you pass to your script when you run items
'''

script, first, second, third = argv
#unpack whatever is in argv to the variables

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "Your third variable is: ", third
