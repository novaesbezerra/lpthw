from sys import argv

script, filename = argv
#unpacking 2 parameter to variables script and filename in that order

txt = open(filename)
#atribuindo filename to txt dentro do script

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again: "
file_again = raw_input("> ")

txt_again = open(file_again)
#atribuindo a file again 
print txt_again.read()
