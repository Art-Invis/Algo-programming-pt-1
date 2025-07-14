s = input("Введіть послідовність літер: ")

if len(s) < 2:
    print("Немає пропущених букв або рядок занадто короткий.")
else:
    is_lower = s[0].islower()
    alphabet_low = "abcdefghijklmnopqrstuvwxyz"
    alphabet_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if is_lower:
        alphabet = alphabet_low
    else:
        alphabet = alphabet_up

    for i in range(len(s) - 1):
        num1 = alphabet.index(s[i])
        num2 = alphabet.index(s[i + 1])
        if num2 - num1 != 1:
            print(f"Пропущена буква: {alphabet[num1 + 1]}")
            break