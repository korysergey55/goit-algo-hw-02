
from collections import deque

def is_palindrome(string):
    # Видаляємо пробіли та перетворюємо рядок у нижній регістр
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    
    # Створюємо двосторонню чергу (deque)
    char_deque = deque(cleaned_string)
    
    # Порівнюємо символи з обох кінців deque
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            print('This text is not polindrom')
            return False  # Якщо символи не збігаються, це не паліндром
    print('This text is polindrom')
    return True  # Якщо всі символи збігаються, це паліндром


is_palindrome("A man a plan a canal Panama")
