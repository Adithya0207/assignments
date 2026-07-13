
products = ["Laptop", "Mouse", "Keyboard"]
print("Initial List:", products)

products.append("Printer")
print("After append:", products)

products.insert(3, "Monitor")
print("After insert:", products)

new_products = ["Tablet", "Webcam"]
products.extend(new_products)
print("After extend:", products)

products.remove("Mouse")
print("After remove:", products)


shipped = products.pop()
print("Shipped Product:", shipped)
print("After pop:", products)

count = products.count("Laptop")
print("Laptop appears:", count, "time(s)")

position = products.index("Monitor")
print("Monitor is at index:", position)

products.sort()
print("Sorted List:", products)

products.reverse()
print("Reversed List:", products)


backup = products.copy()
print("Backup Copy:", backup)


products.clear()
print("After clear:", products)
print("Backup remains:", backup)