import re

readPath = 'Dataset_AllCompletePolicies_Exercise.txt'
writePath = 'Dataset_AllCompletePolicies_New.txt'

# Read all lines from the file
with open(readPath, 'r') as file:
    lines = file.readlines()

# Replace "Word" with "Lord" in each line
updated_lines = [line.replace('Unspecified', 'Research').replace('Analytics/Research', 'Analytics') for line in lines]


# Write the updated lines back to the file
with open(writePath, 'w') as file:
    file.writelines(updated_lines)

    


