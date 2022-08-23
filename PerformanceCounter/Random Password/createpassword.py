import random
import string
import time

print("Welcome to the PyPassword generator")
Q_Letters = int(input("How many letters would you like in your password?\n"))
Q_numbers = int(input("How mnay numbers would you like?\n"))
Q_symbols = int(input("How many symbols would you like?\n"))

# Performance count start here
start = time.perf_counter()
password = random.choices(string.ascii_letters, k=Q_Letters) + \
             random.choices(string.digits, k=Q_numbers) + \
             random.choices(string.punctuation, k=Q_symbols)
random.shuffle(password)
end = time.perf_counter()
# Performance count ends here
print(f"{end - start:.8f} seconds")
print(f"Your password is: {''.join(password)}")
