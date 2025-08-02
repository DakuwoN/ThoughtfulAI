# 📦 Package Sorting Function — Thoughtful Support Engineering Challenge

This project implements a Python function that determines how robotic arms in Thoughtful's automation factory should dispatch packages based on their **size** and **weight**.

[Run it on Replit](https://replit.com/new/python3)

---

## 🧠 Objective

Sort each package into one of three stacks based on its **volume** and **mass**:

### Rules:

- A package is **bulky** if:
  - Its volume (width × height × length) is **≥ 1,000,000 cm³**, **or**
  - **Any one** of its dimensions is **≥ 150 cm**
- A package is **heavy** if:
  - Its mass is **≥ 20 kg**

### Stack Labels:

| Stack      | Conditions                                                 |
| ---------- | ---------------------------------------------------------- |
| `REJECTED` | If the package is **both bulky and heavy**                 |
| `SPECIAL`  | If the package is **either bulky or heavy** (but not both) |
| `STANDARD` | If the package is **neither bulky nor heavy**              |

---

## 🛠️ Function Signature

```python
def sort(width: int, height: int, length: int, mass: int) -> str:
```

## 🧪 Test Coverage

This solution includes test cases for:
Packages that are neither bulky nor heavy
Packages that are only bulky
Packages that are only heavy
Packages that are both bulky and heavy
Threshold edge cases (exactly 150 cm or 20 kg)
