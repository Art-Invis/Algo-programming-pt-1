# Lab Assignment 1: Python Virtual Environment & Programming Basics  
**Subject:** Algorithmization and Programming  
**Variant:** 5  
**Directory:** `src_code/lab_1/`

---

## 🎯 Objective  
- Learn how to create and activate a virtual Python environment  
- Manage packages using `pip`  
- Execute HTTP requests using the `requests` library  
- Write and run basic Python scripts  
- Apply arithmetic, logical, and mathematical operations in Python  

---

## 📂 File Structure  
| Filename         | Purpose                                                                 |
|------------------|-------------------------------------------------------------------------|
| `task_1.py`     | Performing an HTTP GET request with `requests`                      |
| `task_2.py`    | Performing arithmetic and logical operations (Variant 5 - Table 1)  |
| `task_3.py`     | Calculating math expression with `math` module (Variant 5 - Table 2)|

> 📁 All files are saved in `code/lab_1/` and must follow the filenames exactly.

---

## ✅ Tasks  

### 📘 Part 1: Virtual Environment & HTTP  
1. Create environment using `python -m venv venv`  
2. Activate the environment (`venv\Scripts\activate` or `source venv/bin/activate`)  
3. Check installed packages with `pip list`  
4. Export packages: `pip freeze > requirements.txt`  
5. Write and run HTTP request script:

```python
import requests

url = "https://uakino.club/filmy/genre_drama/3-kryminalne-chtyvo.html"
response = requests.get(url)
print(response.text)
```

**Expected Output:**  
HTML document returned with 404 Not Found — indicates request was successful and URL does not exist.

---

### ⚙️ Part 2: Logical & Mathematical Programming  

#### 📐 Table 1 – Logic & Arithmetic (`variant_logic.py`)
```python
num1 = 31
num2 = 19
is_even = True
is_odd = False

print('Sum:', num1 + num2)
print('Difference:', num1 - num2)
print('Product:', num1 * num2)
print('Division:', num1 / num2)
print('AND:', is_even and is_odd)
print('OR:', is_even or is_odd)
```

**Output:**
```
Sum: 50
Difference: 12
Product: 589
Division: 1.631578947368421
AND: False
OR: True
```

---

#### 🧮 Table 2 – Math Expression (`variant_math.py`)
```python
import math

x = 2.735
z = 7.218

a = math.cos(x)
b = math.sin(x)
i = (z + x) / a
o = a * b
n = math.sqrt(abs(o))
r = 16 * z

result = (i + n) ** 2 + r
print(result)
```

**Output:**
```
220.21789218922078
```

---

## 📚 Theoretical Concepts  

- **Python** is a high-level interpreted language for diverse applications (web, AI, etc.)  
- Advantages: simple syntax, large community, cross-platform compatibility, rich libraries  
- Recommended version: **Python 3**, as Python 2 is deprecated  
- Virtual environments: isolated project-specific environments using tools like `venv`, `virtualenv`, `conda`  
- Variables: use descriptive `snake_case` names, assign with `=`, e.g. `total_sum = 42`  
- Data types: `int`, `float`, `str`, `bool`, `list`, `tuple`, `dict`  
- Operations:  
  - Arithmetic: `+`, `-`, `*`, `/`, `%`, `**`  
  - Logical: `and`, `or`, `not`  
  - Math functions: `sin()`, `cos()`, `sqrt()` from `math` module  

📎 *Covers Python scripting fundamentals, environment setup, HTTP interactions, and core logical/math operations through simple but instructive examples.*