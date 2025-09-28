#plaintext = "ThieuPhuongLinh", k = 31

def en(text, k):
    k = k % 26  
    result = ""
    for ch in text:
        if ch.isalpha():  
            if ch.isupper():
                base = ord('A')
                result += chr((ord(ch) - base + k) % 26 + base)
            else:
                base = ord('a')
                result += chr((ord(ch) - base + k) % 26 + base)
        else:
            result += ch
    return result

def de(text, k):
    return en(text, -k)

#test
P = "ThieuPhuongLinh"
k = 31
C = en(P, k)

print("Plaintext:", P)
print("Key k =", k, "(mod 26 =", k % 26,")")
print("Ciphertext:", C)
