numbers=list(map(int,input("Enter numbers separated by space: ").split()))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
squares = list(map(lambda x: x ** 2, even_numbers))
print("Squares of even numbers:", squares)