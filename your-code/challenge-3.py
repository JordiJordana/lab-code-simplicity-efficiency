"""The solution in this case is about using list comprehensions to make the code
more efficient and simple"""


X = int(input("What is the maximal length of the triangle side? Enter a number: "))

solutions = [[x, y, z] for x in range(5, X) for y in range(4, X) for z in range(3, X) if (x*x==y*y+z*z)]

maximum = 0
maximum = max([max(solution) for solution in solutions if maximum < max(solution)])

print(f"The longest side possible is {maximum}")