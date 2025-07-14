def find_missing_letter(chars):
    # Ітеруємося через літери та їхні індекси у списку `chars`
    for i, char in enumerate(chars):
        # Перевіряємо, чи індекс `i` менший за останній індекс у списку
        if i < len(chars) - 1 and ord(chars[i + 1]) - ord(chars[i]) > 1:
            # Порівнюємо різницю ASCII кодів сусідніх літер
            # Якщо різниця більше за 1, то знаходимо пропущену літеру та повертаємо її
            return chr(ord(char) + 1)
            

print ('- Приклад використання функції наведенний у завданні:')
sequence1 = ["a", "b", "c", "d", "f"]
missing_letter1 = find_missing_letter(sequence1)
print(missing_letter1)  # Виведе "e"

sequence2 = ["O", "Q", "R", "S"]
missing_letter2 = find_missing_letter(sequence2)
print(missing_letter2)  # Виведе "P"

#-----------------------------------------------------------------------------------------------------------------------------------------------

print ('- Приклад використання функції при введені послідовності літер з клавіатури ->')
sequence = input("Для цього введіть послідовність літер: ")

chars = list(sequence)

missing_letter = find_missing_letter(chars)
print(f"Пропущена літера: {missing_letter}")


