grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
avgGrades= {}
students2 = sorted(students)
for i in range(len(students2)):
    student = students2[i]
    studentGrades = grades[i]
    avgGrades[student] = sum(studentGrades) / len(studentGrades)
print(avgGrades)


