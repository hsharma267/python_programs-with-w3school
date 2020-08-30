import re
txt = "The rain in spain"
x = re.findall("^The.*spain$", txt)
if x:
    print("Yes,We have a match.")
else:
    print("No match")
