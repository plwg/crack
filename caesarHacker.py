from cipher import caesar

cipherText = input("What is the encrypted message you want to crack?")

attemptKey = int(input("What is the number of key you want to attempt?"))

for i in range(1, attemptKey + 1):
    print("Key " + str(i)  + ": " + caesar(cipherText, i, 1))
