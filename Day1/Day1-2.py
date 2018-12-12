import os
os.chdir('Day1')
checklist = []
for s in open('input.txt'):
    if s not in checklist:
        checklist.append(s)
    else:
        print(s)
        break
        