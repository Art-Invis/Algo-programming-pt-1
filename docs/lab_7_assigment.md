# Lab Assignment 7: Custom Exceptions & Decorators with Logging in Python  
**Subject:** Algorithmization and Programming  
**Variant:** 5  
**Directory:** `code/lab_7/`

---

## 🎯 Objective  
This lab focuses on extending Lab 5 by applying advanced Python techniques, including:  
- Creating custom exception classes  
- Implementing a parameterized decorator `logged()` for logging exceptions  
- Understanding Python logging functionality in both console and file modes  
- Applying PEP8 standards and validating code using `PyLint`  
- Enhancing flexibility and robustness of class methods through exception handling  

---

## 📂 File Structure  

| Filename             | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `task.py`          | Updated `Book` and `BookShop` classes with custom exceptions and logging and Contains the `logged()` decorator and `BookNotFoundException` implementation and Main execution script demonstrating exception raising and logging behavior  |
| `error_log.txt`      | Generated during file-mode logging to capture exception details              |

> ✅ PyLint Score: `10.00/10`  
> ✅ Exception handling and decorator logic tested successfully

---

## ✅ Tasks  
1. Define at least one custom exception (`BookNotFoundException`)  
2. Implement a parameterized decorator `logged(exception, mode)` that logs errors  
   - `mode = "console"`: logs to terminal  
   - `mode = "file"`: appends errors to a log file  
3. Decorate a method in the `BookShop` class (e.g. `remove_book`)  
4. Trigger and log multiple exceptions during `main()` execution  
5. Ensure code meets PEP8 styling with no PyLint warnings  
6. Demonstrate both console and file logging modes

---

## 📊 Output Sample

```
Initial Book Inventory:
"Притулок", "Учень убивці", "Машина"

Removing books...

[Console Mode]
Book 'Притулок' was removed.
ERROR:root:BookNotFoundException: Book titled 'Код да Вінчі' not found.
Book 'Машина' was removed.
ERROR:root:BookNotFoundException: Book titled 'Емоційний шантаж' not found.

[File Mode]
Logged error: Book titled 'Код да Вінчі' not found.
Logged error: Book titled 'Емоційний шантаж' not found.
```

---

## 📚 Theoretical Highlights  

- **Exceptions** enable structured error handling and improve code readability  
- **Custom Exceptions** like `BookNotFoundException` allow descriptive, domain-specific error feedback  
- **Decorators** enhance function behavior dynamically without modifying core logic  
- **Parameterized Decorators** offer configurable behavior (e.g. logging mode control)  
- **Python Logging** is a powerful built-in tool for monitoring, debugging, and auditing runtime events  
- **PEP8 Compliance** ensures code consistency and maintainability across large codebases  
- **PyLint** assists in enforcing style rules and detecting common mistakes
