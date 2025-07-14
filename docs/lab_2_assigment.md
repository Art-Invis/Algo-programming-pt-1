# Lab Assignment 2: Function Tabulation in Python  
**Subject:** Algorithmization and Programming  
**Variant:** 5  
**Directory:** `src_code/lab_2/`

---

## 🎯 Objective  
Develop flowcharts and Python programs to tabulate functions using a defined interval `[a, b]` and step size `h`. This lab covers two tasks:  
- a) Tabulating a conditional function selected based on argument value (Table 1)  
- b) Tabulating a function defined as an infinite series with absolute error control (Table 2)

---

## 📂 File Structure  

| Filename                   | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| `task1.py`| Tabulates function values with dynamic selection based on argument conditions |
| `task2.py`     | Computes function values using series approximation and error estimation     |

> 📁 Files are stored in `src_code/lab_2/` and must match the naming conventions.

---

## ✅ Tasks  

### 🔸 Task A — Conditional Function Tabulation  
Tabulate function from **Table 1**:  
- Interval: `[0.1, 0.7]`  
- Step size: `h = 0.05`  
- Function selection based on argument conditions

#### 📈 Output Sample:  
```
0.1 | 1.0362045082160705  
0.15 | 1.0535452132544325  
0.2 | 0.2065203535384723  
...  
0.65 | -5.376425918153366  
Done
```

---

### 🔸 Task B — Tabulation via Series Approximation  
Tabulate function from **Table 2** using iterative summation:  
- Interval: `[1.1, 2.0]`  
- Step size: `h = 0.1`  
- Absolute error threshold: `d = 0.001`  
- Summation stops when current term < `d`

#### 📉 Output Sample:  
```
1.1 | sum = 0.351731239446971  
1.2 | sum = 0.3807357619877071  
...  
1.9 | sum = 0.5597103795285504
```

---

## 📚 Theoretical Highlights  

- Tabulation helps visualize function behavior across discrete values  
- Conditional logic applies different expressions within specific intervals  
- Series expansion uses successive terms with convergence control  
- Error estimation via modulus of current term ensures calculation precision  
- Python tools for tabulation include control flow (`while`, `if`), mathematical functions, and precision formatting
