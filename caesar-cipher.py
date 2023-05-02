# Python3.6  
# Coding: utf-8 
# Program to implement a caesar cipher encryption


# Takes a string argument and concatenates it with itself
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
    

# Asks user for message to encrypt
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
    
    
# Asks user to provide key that will be used to encrypt the earlier message
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount
    

# Encrypting the message
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    
    
    # The for loop iterates over each letter in the message
    for currentCharacter in uppercaseMessage:
        # For a specific letter, determine the new position given the cipher key.
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        
        
        # If current letter is in the alphabet, append the new letter to the 
        # encrypted message.
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
            
            
        # If current letter is not in the alphabet, append the current letter.
        else:
            encryptedMessage = encryptedMessage + currentCharacter
            
            
    return encryptedMessage
    
    
# Decrypting the encrypted message
def decryptMessage(message, cipherKey, alphabet):
    
    # Simply shift the letters to their original positions
    decryptKey = -1 * int(cipherKey) 
    return encryptMessage(message, decryptKey, alphabet)
    
    
    
# Driver code
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    
    myMessage = getMessage()
    print(myMessage)
    
    myCipherKey = getCipherKey()
    print(myCipherKey)
    
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')
    

runCaesarCipherProgram()