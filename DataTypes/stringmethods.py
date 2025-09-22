course = 'Python for Beginners'

print(len(course)) #len() is a built-in function

print(course.upper()) #upper() is a method

#upper() method returns a new string. It does not change the original string
print(course)

#upper() is a method but not a function because it associated with a string object
#whereas  len() and print() are functions because they are not associated with any object and used independently/generally

print(course.lower()) #lower() method returns a new string in lowercase

print(course.find('P')) #Output: 0 (index of first occurrence of 'P')
print(course.find('z')) #Output: -1 (not found)
print(course.find('n')) #Output: 5 (index of first occurrence of 'n')
print(course.find('for')) #Output: 7 (index of first occurrence of substring 'for')
print(course.find('For')) #Output: -1 (case-sensitive, not found)
print(course.replace('Beginners', 'Absolute Beginners'))
print(course.replace('beginners', 'Absolute Beginners')) #case-sensitive, no change

print('Python' in course) #Output: True
print('p' in course) #Output: False (case-sensitive)

#find returns the index of first occurrence of substring
#in returns a boolean value indicating presence or absence of substring

print(course.title()) #capitalizes the first letter of each word in the string
print(course) #original string remains unchanged