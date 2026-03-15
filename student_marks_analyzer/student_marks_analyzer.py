
# Student Marks Analyzer
# This program analyzes student marks using arrays

marks = []

n = int(input("Enter number of students: "))

for i in range(n):
    m = int(input("Enter marks: "))
    marks.append(m)

average = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)

above_avg = 0
for m in marks:
    if m > average:
        above_avg += 1

print("\nResults:")
print("Marks:", marks)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Students above average:", above_avg)




