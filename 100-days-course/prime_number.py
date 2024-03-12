# Write your code below this line 👇


def prime_checker(number):
  cousin = []
  for num in range(1,number):
    cous = number/num
    if cous.is_integer() is True:
      cousin.append(num)
    if 1 in cousin:
      cousin.pop(cousin.index(1))
  if len(cousin) > 0:
    print(f"It's not a prime number.")
  else:
    print(f"It's a prime number.")


# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)
