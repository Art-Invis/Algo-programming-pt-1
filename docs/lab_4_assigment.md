# Lab Assignment 4: Class Structure and Visibility in Python  
**Subject:** Algorithmization and Programming  
**Variant:** 5  
**Directory:** `code/lab_4/`

---

## 🎯 Objective  
Understand Python class concepts including:  
- Class attributes and methods  
- Visibility modifiers (public, protected, private)  
- Accessor methods (getters)  
- Constructors (`__init__`) and destructors (`__del__`)  
- Overriding string representation methods (`__str__` and `__repr__`)  
- Creating multiple instances and managing data encapsulation

---

## 📂 File Structure  

| Filename        | Description                                                           |
|-----------------|-----------------------------------------------------------------------|
| `task.py`     | Defines the `Stadium` class with required fields, constructors, access methods, and destructors and contains the `main()` method, initializes 3 objects, prints all field values, and uses `__str__` / `__repr__` |

> 📁 All scripts must be stored in `code/lab_4/`.

---

## ✅ Tasks  
1. Learn about visibility modifiers, constructors, and destructors in Python  
2. Implement class `Stadium` with private fields:  
   - `spectators`  
   - `name`  
   - `lighting_power`  
3. Create public fields:  
   - one numeric  
   - one string  
4. Provide accessor methods for all private fields  
5. Override `__str__` and `__repr__` for formatted output  
6. Implement both default and parameterized constructors  
7. Add a custom destructor to show object deletion  
8. Write a `main()` method that:  
   - Instantiates 3 objects of `Stadium` class  
   - Outputs all field values  
   - Uses both `__str__()` and `__repr__()` for display  

---

## 🧾 Output Sample  
```
Stadium name: Арена, Spectators: 50000, Lighting power (lux): 5000  
Stadium name: Олімп, Spectators: 60000, Lighting power (lux): 6000  
Stadium name: Країна, Spectators: 70000, Lighting power (lux): 7000  

Stadium #1  
 Name: Арена, Spectators: 50000, Lighting: 5000  
Stadium #2  
 Name: Олімп, Spectators: 60000, Lighting: 6000  
Stadium #3  
 Name: Країна, Spectators: 70000, Lighting: 7000  

Method repr:  
Stadium : (50000, 'Арена', 5000)  
Stadium : (60000, 'Олімп', 6000)  
Stadium : (70000, 'Країна', 7000)  

Stadium Арена was demolished  
Stadium Олімп was demolished  
Stadium Країна was demolished
```

---

## 📚 Theoretical Overview  

- Python class fields default to public; protected use `_field`, private use `__field`  
- Constructors:  
  - `__init__()` defines initialization logic  
  - Can support default and parameterized values  
- Destructors:  
  - `__del__()` handles object cleanup  
- Accessor methods (getters) provide controlled data access  
- `__str__()` returns human-readable object representation  
- `__repr__()` returns system-friendly representation  
- Encapsulation improves data protection and modularity in OOP  