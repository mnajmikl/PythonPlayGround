import random
import string
import time

#print("Welcome to the PyPassword generator v1")
#Q_Letters = int(input("How many letters would you like in your password?\n"))
#Q_numbers = int(input("How many numbers would you like?\n"))
#Q_symbols = int(input("How many symbols would you like?\n"))

# Performance count start here
start = time.perf_counter()
password = random.choices(string.ascii_letters, k=8) + \
             random.choices(string.digits, k=2) + \
             random.choices(string.punctuation, k=2)
random.shuffle(password)
end = time.perf_counter()
# Performance count ends here
print(f"{end - start:.12f}")
#print(f"Your password is: {''.join(password)}")
