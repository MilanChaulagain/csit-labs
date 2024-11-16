alpha ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Lenght of alpha: {}".format(len(alpha)))

 # input in capitalize
str_in = input("Enter a word, like HELLO:")
print("str_in = ", str_in)
 
msg_cipher = " "
n = len(str_in)
print("n =", n)
 
for i in range(n):
    c = str_in[i]
    loc = alpha.find(c)
    print(i , c, loc) #This line can be omitted, used only to see
    #intermediate result
    newloc = (loc+3)% 26
    msg_cipher += alpha[newloc]
 
print("Plain text: ", str_in)
print("Cipher text: ", msg_cipher)
