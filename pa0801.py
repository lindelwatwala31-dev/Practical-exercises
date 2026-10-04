# Question 1.1
import numbers


def round_to_ten(numbers):
    i = 0
    while i < len(numbers):
        numbers[i] = round(numbers[i], -1)
        i += 1
    return numbers

print(round_to_ten([12, 15, 17, 19, 22, 25, 28, 30]))


# Question 1.2
def increment_and_count(numbers):
    i = 0
    while i < len(numbers):
        if numbers[i] < 40:
            numbers[i] += 2

    count = 0
    j = 0
    while j < len(numbers):
       if numbers[j] < 50:
            count += 1
       j += 1

    return (numbers, count)

result = increment_and_count([35, 38, 42, 45, 48, 50])
print(result)