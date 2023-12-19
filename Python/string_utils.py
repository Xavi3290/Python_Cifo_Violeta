def reverse_string(text):
    return text[::-1]

def is_palindrome(text):
    if text[::1] == text[::-1]:
        return True
    else:
        return False
    
def count_vowels(text):
    voc = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    voc_cont = 0
    for i in voc:
        for j in text:
            if i == j:
                voc_cont +=1
    return voc_cont
