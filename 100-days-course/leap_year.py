# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
leap_f = year % 4
leap_s = year % 100
leap_t = year % 400

if leap_f == 0 and leap_t == 0 and leap_t == 0:
  print("Leap year")
elif leap_f == 0 and leap_s != 0:
  print("Leap year")
else:
    print("Not leap year")
