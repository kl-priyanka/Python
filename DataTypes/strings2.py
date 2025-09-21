course = "Python for 'Beginners'"

print(course[0])  # Output: P
print(course[-1]) # Output: s
print(course[0:3]) # Output: Python
print(course[0:])  # Output: Python for 'Beginners'
print(course[:])   # Output: Python for 'Beginners'
print(course[7:10]) # Output: for
print(course[11:])  # Output: 'Beginners'
print(course[:11])  # Output: Python for

numbers = "0123456789"
print(numbers[::2])  # Output: 02468 (every second character)