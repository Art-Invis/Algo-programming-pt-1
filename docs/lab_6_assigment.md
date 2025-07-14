# Lab Assignment 6: Writing Tests with PyTest & Ensuring PEP8 Compliance  
**Subject:** Algorithmization and Programming  
**Variant:** 5  
**Directory:** `code/lab_6/`

---

## 🎯 Objective  
This lab focuses on:  
- Writing unit tests for Python classes using the `PyTest` framework  
- Understanding basic testing principles and covering all class methods  
- Applying the Python style guide (`PEP8`) in code formatting  
- Using `PyLint` to detect and fix stylistic and structural issues  
- Demonstrating technical correctness and adherence to professional development standards

---

## 📂 File Structure  

| Filename               | Description                                                               |
|------------------------|---------------------------------------------------------------------------|
| `code_of_lab6.py`            | Refactored Book and BookShop class from Lab 5 with PEP8-compliant docstrings and formatting |
| `test_for_lab6.py`       | PyTest unit tests covering all major class methods                        |

> ✅ Pylint rating: `10.00/10`  
> ✅ All PyTest cases passed successfully

---

## ✅ Tasks  
1. Refactor Lab 5 classes (`Book`, `BookShop`) to follow PEP8 coding standards  
2. Write descriptive docstrings for all classes, methods, and functions  
3. Cover every method of `BookShop` with separate PyTest functions  
4. Use fixtures to set up test environments  
5. Validate sorting methods and ensure dynamic add/remove logic works  
6. Verify code quality using `pylint`, and achieve a perfect score  
7. Demonstrate working tests and clean code to your instructor

---

## 📊 PyTest Coverage  

| Test Name                      | Description                                           | Status |
|-------------------------------|-------------------------------------------------------|--------|
| `test_add_book()`             | Checks if books are added correctly                  | ✅     |
| `test_remove_new_book()`      | Adds & removes a new book, confirms count            | ✅     |
| `test_remove_existing_book()` | Removes a known book, verifies new count             | ✅     |
| `test_remove_book_from_empty_shop()` | Validates behavior when shop is empty            | ✅     |
| `test_remove_non_existing_book()` | Tries to remove absent book, ensures no change   | ✅     |
| `test_top_books_by_price()`   | Verifies sorting by price works correctly            | ✅     |
| `test_top_books_by_sales()`   | Verifies sorting by sales works correctly            | ✅     |

---

## 📚 Theoretical Highlights  

- **PyTest** enables modular and readable testing with minimal boilerplate  
- **Fixtures** simplify object setup across multiple test cases  
- **PEP8** ensures consistency and readability in Python codebases  
- **PyLint** statically checks for code quality, naming, formatting, and possible bugs  
- Adhering to standards showcases good engineering practices alongside functional code  
- Automated tests ensure long-term maintainability and correctness of the project
