# Question 1 - Discount Calculator

org_price = float(input("Enter the original price of the item: R"))
discount_perc = float(input("Enter the discount percentage: "))
discount_amount = (discount_perc / 100) * org_price
final_price = org_price - discount_amount
print("")
print("Discount amount is: R", discount_amount)
print("Final price after discount is: R", final_price)


# Question 2 - Marks and Grade

marks_obtained = float(input("Enter the marks obtained: "))
total_marks = float(input("Enter the total marks: "))
grade_percentage = (marks_obtained / total_marks) * 100
if grade_percentage >= 75:
    print("Grade: Distinction")
elif grade_percentage <= 74 and grade_percentage >= 60:
    print("Grade: Merit")
elif grade_percentage <= 59 and grade_percentage >= 50:
    print("Grade: Pass")   
else:
    print("Grade: Fail")


#Question 3 - Salary increase

current_salary = float(input("Enter the current salary: R"))
percentage_increase = float(input("Enter the percentage increase: "))
increase_amount = (current_salary * percentage_increase) / 100
new_salary = current_salary + increase_amount
print("Current salary is: R", current_salary)
print("New salary is: R", new_salary)


#Question 4 - Profit percentage

cost_price = float(input("Enter the cost price of the item: R"))
selling_price = float(input("Enter the selling price of the item: R"))
profit_or_loss = selling_price - cost_price
if profit_or_loss > 0:
    profit_percentage = (profit_or_loss / cost_price) * 100
    print("")
    print("You made a profit of R", profit_or_loss)
    print("Profit percentage is: ", profit_percentage, "%")

elif profit_or_loss < 0:
    loss = abs(profit_or_loss)
    loss_percentage = (loss / cost_price) * 100
    print("")
    print("You made a loss of R", loss)
    print("Loss percentage is: ", loss_percentage, "%") 

    



