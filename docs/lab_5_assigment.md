# Lab Assignment 5: Object-Oriented Programming & Book Management in Python  
**Subject:** Algorithmization and Programming  
**Variant:** 5  
**Directory:** `code/lab_5/`

---

## 🎯 Objective  
Implement Python classes based on OOP principles to model books and a bookshop system.  
The goal is to:  
- Practice working with constructors, destructors, visibility modifiers, and access methods  
- Add and remove objects dynamically from a collection  
- Output structured information and compute top books based on price and sales

---

## 📂 File Structure  

| Filename        | Description                                                         |
|-----------------|---------------------------------------------------------------------|
| `task_1.py`     | Defines the `Book` class with required fields and display methods   and Implements the `BookShop` class with methods for managing books  and Main execution logic for initializing and displaying book data   |
| `task_2.py`     |  Second variant   of programm  |

> 📁 All files are stored in `code/lab_5/`. They must follow consistent naming and encapsulation practices.

---

## ✅ Tasks  
1. Create a `Book` class with fields:  
   - `price`, `numberOfPages`, `author`, `quantity`, `numberOfSales`  
2. Create a `BookShop` class to store multiple `Book` objects  
3. Implement constructors and destructors  
4. Add accessor and display methods for all fields  
5. Provide functionality to:  
   - Add books to shop  
   - Remove books by title  
   - Display top books by price and sales  
6. Use the `main()` method to:  
   - Initialize multiple books  
   - Add them to the shop  
   - Demonstrate sorting and removal operations  

---

## 📊 Output Sample

```
Initial Book Inventory:

Title: Притулок
Price: 350 грн
Pages: 300
Author: Меделін Ру
In stock: 50
Sales: 100

Title: Учень убивці
Price: 200 грн
Pages: 250
Author: Робін Гобб
In stock: 30
Sales: 80

Title: Машина
Price: 500 грн
Pages: 400
Author: Дарія Піскозуб
In stock: 40
Sales: 120

Top-3 Books by Price:
1. Машина – 500 грн  
2. Притулок – 350 грн  
3. Учень убивці – 200 грн

Top-3 Books by Sales:
1. Машина – 120 sales  
2. Притулок – 100 sales  
3. Учень убивці – 80 sales

Book Притулок was removed from inventory.  
Book Код да Вінчі not found in inventory.

Updated Book Inventory:
- Учень убивці  
- Машина
```

---

## 📚 Theoretical Highlights  

- Python classes can encapsulate data using public, protected, and private attributes  
- Constructors (`__init__`) initialize fields, destructors (`__del__`) manage cleanup  
- Getters provide controlled access to private data  
- Custom display via `__str__()` and `__repr__()` improves readability and object tracking  
- Sorting and filtering are performed using custom logic within class methods  
- Main functions integrate all components to simulate real-world system behavior
