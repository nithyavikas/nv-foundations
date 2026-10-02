print("---------Basics--------")
print("Hello World!!!!\a")  #\a Rings Bell
print("\\") #\
print("\'") #'
print("This is Alice\'s mother.")
print(r'This is Alice\'s mother.')
print(r'This is Alice\\\'s mother.')
print("\"") #"
print("\a") # Rings Bell
#print("Hello \fWorld") #form feed character
print("Hello \nWorld") #newline character
print("Hello \tWorld") #Prints a tab
print("\056") #octal value - \0
#print("\0x2a") #hex value - \0x


number = 42
print(oct(number))  # Output: '0o52'
print(hex(number))


print('''Dear Alice,

How are you!!

Thank you
Eve''')
#---------2. Raw String ==> format String Alignment
print("-----------------2. Raw String-------")
print(format('Hello', '>30'))   #right justified >
print(format('Hello', '<30'))   #left justified <
print(format('Hello', '^30'))   #Center justified ^

print('Hello', format('-','-<10'), 'World')
#---------3. Boolean variables
print("----------------3. Boolean--------")
var=True
print(var)
print(87<87.0)
print(87<=87.0)
