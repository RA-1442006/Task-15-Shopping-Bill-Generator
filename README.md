# Task 15: Shopping Bill Generator

A simple and user-friendly Python console application that accepts product details (item name, quantity, and unit price) and generates a neatly formatted, itemized shopping invoice with subtotal, discount, GST tax, and the final payable amount.

---

## What the Program Does

1. Lets the user input products one by one (name, quantity, and price per unit).
2. Stores each product as a dictionary with keys `name`, `quantity`, and `price`, keeping all products inside a list.
3. Automatically validates input data using `try/except` and conditional checks:
   - Rejects empty product names.
   - Rejects non-numeric, zero, or negative quantities.
   - Rejects non-numeric or negative prices.
   - Displays clear error messages and prompts the user again without crashing.
4. Allows the user to type `done` when finished adding items.
5. Calculates:
   - **Subtotal**: Sum of `quantity * price` across all items.
   - **Discount**: 10% discount if the subtotal is Rs. 1000.00 or more; otherwise 0.
   - **Tax (GST)**: 18% GST applied strictly to the amount after discount.
   - **Final Amount**: Discounted subtotal + GST.
6. Prints a clean, column-aligned invoice with currency values formatted to 2 decimal places using `Rs.` for Windows terminal compatibility.

---

## How to Run It

1. Make sure Python 3 is installed:
   ```bash
   python --version
   ```

2. Navigate to the project directory:
   ```bash
   cd "C:\Users\realc\Documents\task-15-shopping-bill-generator"
   ```

3. Run the program:
   ```bash
   python shopping_bill.py
   ```

4. Enter product details when prompted. Type `done` when you finish adding all items.

---

## How the Calculation Works

The bill calculations follow a step-by-step sequence:

1. **Subtotal**:
   $$\text{Subtotal} = \sum (\text{Quantity} \times \text{Price})$$

2. **Discount Rule**:
   - If $\text{Subtotal} \ge 1000.00$: $\text{Discount} = 10\% \text{ of Subtotal} = \text{Subtotal} \times 0.10$
   - If $\text{Subtotal} < 1000.00$: $\text{Discount} = \text{Rs. } 0.00$

3. **Taxable Amount**:
   $$\text{Taxable Amount} = \text{Subtotal} - \text{Discount}$$

4. **Tax Rule (18% GST)**:
   $$\text{Tax} = \text{Taxable Amount} \times 0.18$$

5. **Final Amount**:
   $$\text{Final Amount} = \text{Taxable Amount} + \text{Tax}$$

---

## Sample Output

The following are real outputs from testing `shopping_bill.py`.

### 1. Normal Bill Without Discount (Subtotal < Rs. 1000)

```
=== Shopping Bill Generator ===
Enter product name (or 'done' to finish): Notebook
Enter quantity: 3
Enter price per unit: 60
Added 'Notebook' to cart.

Enter product name (or 'done' to finish): Pen
Enter quantity: 5
Enter price per unit: 20
Added 'Pen' to cart.

Enter product name (or 'done' to finish): Pencil Box
Enter quantity: 2
Enter price per unit: 150
Added 'Pencil Box' to cart.

Enter product name (or 'done' to finish): done

====================================================
                   SHOPPING BILL                    
====================================================
Item                  Qty   Price       Total       
----------------------------------------------------
Notebook              3     Rs. 60.00   Rs. 180.00  
Pen                   5     Rs. 20.00   Rs. 100.00  
Pencil Box            2     Rs. 150.00  Rs. 300.00  
----------------------------------------------------
Subtotal:                                 Rs. 580.00
Discount:                                   Rs. 0.00
Tax (18% GST):                            Rs. 104.40
====================================================
Final Amount:                             Rs. 684.40
====================================================
```

### 2. Bill With Discount Applied (Subtotal >= Rs. 1000)

```
=== Shopping Bill Generator ===
Enter product name (or 'done' to finish): Backpack
Enter quantity: 1
Enter price per unit: 1200
Added 'Backpack' to cart.

Enter product name (or 'done' to finish): Water Bottle
Enter quantity: 2
Enter price per unit: 250
Added 'Water Bottle' to cart.

Enter product name (or 'done' to finish): done

====================================================
                   SHOPPING BILL                    
====================================================
Item                  Qty   Price       Total       
----------------------------------------------------
Backpack              1     Rs. 1200.00 Rs. 1200.00 
Water Bottle          2     Rs. 250.00  Rs. 500.00  
----------------------------------------------------
Subtotal:                                Rs. 1700.00
Discount:                                 Rs. 170.00
Tax (18% GST):                            Rs. 275.40
====================================================
Final Amount:                            Rs. 1805.40
====================================================
```

### 3. Invalid Input Handling (Error Recovery)

```
=== Shopping Bill Generator ===
Enter product name (or 'done' to finish): 
Product name cannot be empty. Please try again.
Enter product name (or 'done' to finish): Notebook
Enter quantity: abc
Invalid quantity. Please enter a valid whole number.
Enter quantity: 0
Quantity must be greater than zero. Please try again.
Enter quantity: -2
Quantity must be greater than zero. Please try again.
Enter quantity: 2
Enter price per unit: xyz
Invalid price. Please enter a valid number.
Enter price per unit: -50
Price cannot be negative. Please try again.
Enter price per unit: 75
Added 'Notebook' to cart.

Enter product name (or 'done' to finish): done

====================================================
                   SHOPPING BILL                    
====================================================
Item                  Qty   Price       Total       
----------------------------------------------------
Notebook              2     Rs. 75.00   Rs. 150.00  
----------------------------------------------------
Subtotal:                                 Rs. 150.00
Discount:                                   Rs. 0.00
Tax (18% GST):                             Rs. 27.00
====================================================
Final Amount:                             Rs. 177.00
====================================================
```

### 4. Empty Cart (Typing "done" Immediately)

```
=== Shopping Bill Generator ===
Enter product name (or 'done' to finish): done

No items were added. No bill to generate.
```

---

## Interview Questions & Answers

### 1. Which data structure would you use for product records?
I would use a **dictionary** for each individual product record (e.g., `{"name": "Notebook", "quantity": 3, "price": 60.0}`) and store them in a **list** (`items = [...]`).
- **Why dictionary for records**: Dictionaries store values using descriptive key-value pairs (`name`, `quantity`, `price`), which makes the code readable and self-documenting. If we used plain lists or tuples (`[name, qty, price]`), we would have to access fields using numeric indices (`item[0]`, `item[1]`), making the code error-prone and harder to maintain.
- **Why list for the collection**: A list preserves insertion order, allows dynamic sizing as the user adds products, and can easily be looped through or checked with `len()`.

### 2. Why should calculations be separated into functions?
Separating calculations into distinct functions (`calculate_subtotal`, `calculate_discount`, `calculate_tax`) provides several key benefits:
- **Single Responsibility Principle**: Each function does one job well. The function calculating discount doesn't need to know how tax is computed or how input was received.
- **Maintainability & Reusability**: Business rules change often. If the discount percentage changes from 10% to 15% or GST changes from 18% to 12%, we only modify that single function without touching the input loop or printing logic.
- **Testability**: Independent functions are easy to unit test. We can pass mock numbers directly (e.g., `calculate_discount(1500)`) and assert the returned value without simulating terminal user input.

### 3. How would you handle invalid quantities?
To handle invalid quantities robustly without crashing:
1. Wrap user input inside a `while True` loop so the program repeatedly asks until valid input is given.
2. Use a `try...except ValueError` block when converting the string input to an integer via `int()`. If the user inputs letters or symbols (like `"abc"` or `"$"`), the `ValueError` is caught and a helpful message is displayed.
3. Add a logical validation check `if qty <= 0` because a shopping quantity must be a positive whole number. If the user enters `0` or negative values (e.g., `-2`), warn them and continue the loop.
4. Only `break` the loop once an integer strictly greater than zero is received.
