#Assignments
# Calculator App (Function-Based)
def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operator"

print(calculator(10, 5, '+'))


#ATM Balance Checker (OOP + Functions)
class ATM:
    def __init__(self, balance=1000):
        self.balance = balance

    def check_balance(self):
        print("Current Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient funds.")

atm = ATM()
atm.check_balance()
atm.withdraw(200)
atm.check_balance()


#Contact Book (Dict + Function)
contacts = {}

def add_contact(name, number):
    contacts[name] = number

def search_contact(name):
    return contacts.get(name, "Not found")

add_contact("Alice", "12345")
add_contact("Bob", "67890")
print(search_contact("Alice"))


#Unique Words from Paragraph (Set)
def unique_words(text):
    words = text.lower().split()
    return set(words)

para = "Python is fun and Python is easy"
print("Unique words:", unique_words(para))


#Student Grades (List of Dicts + Function)
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 72}
]

def print_grades():
    for student in students:
        grade = "A" if student["marks"] >= 80 else "B"
        print(student["name"], "Grade:", grade)

print_grades()


#Product Inventory (Dict + Tuple + Function)
inventory = {
    "Laptop": (10, 800),  # (quantity, price)
    "Phone": (15, 500)
}

def display_inventory():
    for item, (qty, price) in inventory.items():
        print(f"{item}: {qty} units, ${price} each")

display_inventory()


#Rectangle Area and Perimeter (Class + Method)
class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

r = Rectangle(10, 5)
print("Area:", r.area())
print("Perimeter:", r.perimeter())


#Word Frequency Counter (Dict + Loop)
def word_count(text):
    words = text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

sentence = "apple orange apple banana orange"
print(word_count(sentence))


#Number Filter (List + Function + Loop)
def filter_even(nums):
    return [n for n in nums if n % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6]
print("Even numbers:", filter_even(numbers))


#Library System (Set + Class)
class Library:
    def __init__(self):
        self.books = set()

    def add_book(self, title):
        self.books.add(title)

    def remove_book(self, title):
        self.books.discard(title)

    def list_books(self):
        print("Books in library:", self.books)

lib = Library()
lib.add_book("Python 101")
lib.add_book("OOP Concepts")
lib.list_books()
lib.remove_book("Python 101")
lib.list_books()
