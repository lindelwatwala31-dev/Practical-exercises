# Procedural Programming
#sum the numbers in a list
nums = [1,2,3,4,5]
total = 0
for num in nums:
    total + num
print("Result:" + str (total))

# Object-oriented programming
# sum the numbers in a list
class SumNum:
    def __init__(self):
        self.total = 0
    def sum(self, numbers):
        self.total = 0
        for n in numbers:
            self.total = self.total + n
        return self.total
sum_object = SumNum()
print(sum_object.sum([1,2,3,4,5])) 

# Functional programming
nums = [1,2,3,4,5]
result = sum(nums)
print("Result: " + str(result))
