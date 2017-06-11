"""Reading Files.

### Usage
    
```shell
python ex15.py ex15_sample.txt
```
"""

# Import argv (argument variable) module from sys
from sys import argv

# Input script and filename by argv
script, filename = argv

# Open filename and set it as txt variable
txt = open(filename)

# Print "Here is your file" and filename
print "Here is your file %r" % filename
# Pring content of txt
print txt.read()

txt.close()

# Print "Type the file name again:"
print "Type the file name again:"
# Input filename by raw_input
file_again = raw_input("> ")

# Open filename and set it as txt_again
txt_again = open(file_again)

# Print content of txt_again
print txt_again.read()

txt_again.close()
