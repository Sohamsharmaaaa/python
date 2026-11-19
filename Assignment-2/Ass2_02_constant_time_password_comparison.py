# Write a constant time password verifier function to defend against timing attack. Use this function to safely compare user supplied API keys or passwords against stored ones.


def secure_compare(stored: str, userinput: str) -> bool:
    if len(stored) != len(userinput):
        target = stored
        len_result = 1
    else:
        target = userinput
        len_result = 0
    content_result = 0
    for ch1, ch2 in zip(stored, target):
        content_result |= ord(ch1) ^ ord(ch2)
    return (len_result | content_result) == 0


actual_hash = "Indira123"
input_hash = input("Enter the input password or ap key:: ")
print(secure_compare(actual_hash, input_hash))
