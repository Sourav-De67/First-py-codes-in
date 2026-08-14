'''Sure! Here is a simple solution **without using `set()`**.

```python id="r9h8wg"
a = [1, 2, 3, 2, 4, 5, 1, 6, 3]

for i in range(len(a)):
    count = 0

    for j in range(len(a)):
        if a[i] == a[j]:
            count += 1

    if count > 1:
        duplicate = False

        for k in range(i):
            if a[k] == a[i]:
                duplicate = True

        if not duplicate:
            print(a[i])
```

### Output

```text id="am56cs"
1
2
3
```

---

## Easy Explanation

### First loop

```python id="vlrzg6"
for i in range(len(a)):
```

Take one element at a time.

Example:

```text id="pkmxwi"
1, 2, 3, 2, 4, 5, ...
```

---

### Second loop

```python id="8d0c6h"
for j in range(len(a)):
```

Count how many times that element appears.

Example:

```text id="blf7v3"
1 appears 2 times
2 appears 2 times
3 appears 2 times
```

---

### Third loop

This checks whether we have already printed that number.

Without this loop, output would be:

```text id="b1yxhh"
1
2
3
2
1
3
```

The third loop avoids repeated printing.

---

## Much Easier Method (Using `set()`)

After learning sets, you can write:

```python id="0l1i4v"
a = [1, 2, 3, 2, 4, 5, 1, 6, 3]

for i in set(a):
    if a.count(i) > 1:
        print(i)
```

This is shorter, but the first method is better for learning loops and list logic.

---

## 🟢 Next Question

Remove duplicate elements from a list.

Example:

```python id="7z3r91"
a = [1, 2, 3, 2, 4, 5, 1, 6, 3]
```

Output:

```text id="9vwehn"
[1, 2, 3, 4, 5, 6]
```

Would you like to try it yourself or see the solution directly?'''
a = [1, 2, 3, 2, 4, 5, 1, 6, 3]

for i in range(len(a)):
    count = 0

    for j in range(len(a)):
        if a[i] == a[j]:
            count += 1

    if count > 1:
        duplicate = False

        for k in range(i):
            if a[k] == a[i]:
                duplicate = True

        if not duplicate:
            print(a[i])
