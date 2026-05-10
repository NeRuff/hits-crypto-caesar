def solve():
    # Зашифрованный текст из task.txt
    ciphertext = "p3nfne_zrrgf_k0e_4aq_a0obql_q1rq"
    
    # Расшифровка ROT13 (сдвиг 13)
    result = ""
    for char in ciphertext:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') - 13) % 26 + ord('a'))
        else:
            result += char
            
    print(f"Decoded: {result}")
    print(f"Final Flag: HITS{{{result}}}")

if __name__ == "__main__":
    solve()
