# Task - Maths with dictionary elements

dict1 = {
  'a': 4,
  'b': 16,
  'c': 3
}

dict2 = {
  'a': 8,
  'b': 2,
  'c': 3
}

sum_value = 0

for i in dict2:
    sum_value += (dict1[i]*dict2[i])
    
print(sum_value)
    