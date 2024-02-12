# Message Decoder - Pierre Kostantine - Jan 12, 2023

# You are sending a message to your friend.
# Instead of sending the actual message, you send a set of consecutive characters that represent the real letter.
# The number of consecutive characters determines the real letter.

# Prompt user to input the encoded message
encodedMessage = input("Enter the encoded message: ")

def decodeMessage(encodedMessage):
    decodedMessage = ""
    i = 0
    # Iterate through the encoded message
    while i < len(encodedMessage):
        count = 1
        # Count the number of consecutive characters for the current letter
        while i + count < len(encodedMessage) and encodedMessage[i] == encodedMessage[i + count]:
            count += 1
        # Determine the corresponding letter based on the number of consecutive characters
        decodedMessage += chr(ord('A') + count - 1)
        i += count
    return decodedMessage

# Decode the message
decodedMessage = decodeMessage(encodedMessage)
# Print the decoded message
print("Decoded message:", decodedMessage)
