# Jessie Conn - CIT 120 Final Project: Bookstore Discount Manager

# Simple Python Program that reads a list of book titles from input file books.txt,
# then prompts user to enter original prices and discount percentages, validates inputs,
# then calculates the discounted prices, and then displays a neatly formatted summary.

# Declare constants
MAX_BOOKS = 5
INPUT_FILE = "books.txt"

# Declare variables
i = 0
price = 0.0
discount = 0.0
final_price = 0.0
price_valid = False
discount_valid = False

# Initialize arrays
BookTitles = []
OriginalPrices = []
DiscountRates = []
DiscountedPrices = []

# Open and read file
try:
    file = open(INPUT_FILE, "r")
    for i in range(MAX_BOOKS):
        title = file.readline().strip()
        if title != "":
            BookTitles.append(title)
    file.close()
except FileNotFoundError:
    print(f"Error: '{INPUT_FILE}' not found.")
    exit()

# Get prices and discounts
for i in range(len(BookTitles)):
    print("\nBook:", BookTitles[i])

# Get original price
    price_valid = False
    while price_valid == False:
        try:
            price = float(input("Enter original price: $"))
            price_valid = True
        except ValueError:
            print("Invalid input. Please enter a number.")

# Get discount percentage
    discount_valid = False
    while discount_valid == False:
        try:
            discount = float(input("Enter the discount % (e.g., 20 for 20%): "))
            if 0 <= discount <= 100:
                discount_valid = True
            else:
                print("Enter a value between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

# Store data and calculate final price
    OriginalPrices.append(price)
    DiscountRates.append(discount)
    final_price = price * (1 - discount / 100)
    DiscountedPrices.append(final_price)

# Display results
print("\n--- Book Discount Summary ---")
for i in range(len(BookTitles)):
    print(f"{BookTitles[i]}")
    print(f"  Original Price: ${OriginalPrices[i]:.2f}")
    print(f"  Discount: {DiscountRates[i]}%")
    print(f"  Final Price: ${DiscountedPrices[i]:.2f}\n")
