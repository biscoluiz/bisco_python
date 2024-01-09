print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

# Getting Size price

size_price = 0 

if size == 'S':
  size_price = 15
elif size == 'M':
  size_price = 20
else:
  size_price = 25

# Getting peppe addition

pep_add = 0

if add_pepperoni == 'Y':
  if size == 'S':
    pep_add = 2
  else:
    pep_add = 3
else:
  pep_add = 0

# Getting cheese add

chs_add = 0

if extra_cheese == 'Y':
  chs_add = 1
else:
  chs_add = 0

bill =  str(size_price + pep_add + chs_add)

print(f"Your final bill is: ${bill}.")
