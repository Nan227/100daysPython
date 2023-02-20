# count 1-100
# if the number %3 and %5 == 0 then print FizzBuzz

# if the number %3 == 0 then print Fizz
# if the number %5 ==0 then print Buzz
for n in range(1, 101):
  if n %3 == 0 and n %5 ==0:
    print("FizzBuzz")
  elif n%3 == 0:
    print("Fizz")
  elif n%5 == 0:
    print("Buzz")
  else:
    print(n)
