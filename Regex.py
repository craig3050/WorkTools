import re

test_string = "WSP-523-E-SW-XX-020"
input_string = "WSP-5..-E-SW"
regex = re.compile(input_string)
text_remove = re.search(regex, test_string)
print (text_remove)



