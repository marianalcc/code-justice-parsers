# This is a practice parser
# It pulls out the case name and date from some fake text

example_text = """
Case: Lubanga v. ICC
Date: March 14, 2012
Violation: Child Soldiers
"""

lines = example_text.strip().split("\n")
for line in lines:
    if "Case:" in line:
        print("Case Name:", line.split(":")[1].strip())
    if "Date:" in line:
        print("Date:", line.split(":")[1].strip())
