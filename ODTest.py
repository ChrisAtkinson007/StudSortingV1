Students={'Greg':24,'John':22,'Andy':21,'Jim':23,'Phil':22,'Bob':23,'Chip':23,'Tim':24}

print(Students)

StudSorted={ke: val for ke, val in sorted(Students.items(), key=lambda x: x[1])}
print(StudSorted)