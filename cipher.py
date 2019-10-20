"""Cipher Module"""

def caesar(message, key, direction):
    """
    Use the key and symbolset to perform caesar encoding of message. A direction (1 or -1) can be specify.
    
    Return the encoded message.
    """
    symbolset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    newMessage = ''
    length = len(message)
    for i in range(0, length):
        if message[i] in symbolset:
            originalIndex = symbolset.index(message[i])
            newIndex = (originalIndex + key * direction) % len(symbolset)
            newMessage += symbolset[newIndex]
        else:
            newMessage += message[i]
    return newMessage
