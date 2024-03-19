# string indexes and slicing
# find() method
# replace() method
#isalpha() method

# string indexes
# get individual characters from a string by using indexes

title = 'Duncan is great'
print(title[4]) 

# string slice notation

title = 'Duncan is great'
print(title[-5:])
print(title[0:6])

# find() method
# search for substrings in a string using the find() method. It returns the index of the first occurrence of the substring

email = 'bing@outlook.com'
domain_index = email.find('outlook.com')
print(domain_index)
 
# replace() method
# replace one substring with another, 1st argument is substring you want replaced, 2nd argument is substring you want to replace the 1st with

email = 'bing@outlook.com'
gmail = email.replace('outlook.com', 'gmail.com')
print(gmail)
 
# isalpha() method
# check if a string contains only letters 

a = "abcd"
b = " "
c = "12fad"
d = "apple orange"

print(a.isalpha())
print(b.isalpha())
print(c.isalpha())
print(d.isalpha())
