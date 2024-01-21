# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

dividendo = 0
divisor = 0
for student_height in student_heights:
  dividendo += student_height
  divisor += 1
  
media = round(dividendo/divisor)

print(f"total height = {dividendo}")
print(f"number of students = {divisor}")
print(f"average height = {media}")
