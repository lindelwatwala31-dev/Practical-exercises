def repeating(n):
  if n == 0 or n == 1:
    return
  if n % 4 == 0:
    print("Ping", end=" ")
    repeating(n - 1)
  elif n % 2 == 0:
    print("Pong", end=" ")
    repeating(n - 2)
  elif n % 3 == 0:
    print("King", end=" ")
    repeating(n - 3)
  elif n % 5 == 0:
    print("Donkey", end=" ")
    repeating(n - 5)
  else:
    print("Kong", end=" ")
    repeating(n - 4)

#Question 1.4

def is_even(n):
    return n % 2 == 0    
print(is_even(4))  # True
print(is_even(5))  # False

#Question 1.5

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True