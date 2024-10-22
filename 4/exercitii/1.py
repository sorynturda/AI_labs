l = [["Sorin", 12], ["Simba", 11], ["Marcel", 6], ["John", 7], ["Juan", 11], ["Pablo", 7]]
l = sorted(l, key=lambda x: x[1])
lowestGrade = l[0][1]
print(lowestGrade)
for it in l:
    if it[1] == lowestGrade:
        l.remove(it)
lowestGrade = l[0][1]
for it in l:
    if it[1] == lowestGrade:
        print(it)