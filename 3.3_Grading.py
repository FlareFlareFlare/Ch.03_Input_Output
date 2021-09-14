'''
Grading PROGRAM
---------------
Create a program that asks the user for their semester grade, final exam grade, 
and final exam worth and then calculates the overall final grade. 
Ask your instructor if you don't know how to calculate weighted averages.
You don't have to print out the letter grade. We will do that in the next chapter.

Test with the following:

Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6
'''
sem = int(input("What is your semester grade?"))
final = int(input("What is your final exam grade?"))
worth = int(input("What is the exam worth?"))
second_worth = 100 - worth
worth2 = worth * .01
second_worth2 = second_worth * .01
final_grade = (second_worth2*sem) + (worth2*final)
print(final_grade)

