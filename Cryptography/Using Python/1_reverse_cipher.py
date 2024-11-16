#Reverse Cipher
msg = input("Enter your message: ")
n = len(msg)
rev = " "
i = n - 1
while(i>=0):
    rev = rev + msg[i]
    i = i - 1
print("Reverse of msg is: ", rev)