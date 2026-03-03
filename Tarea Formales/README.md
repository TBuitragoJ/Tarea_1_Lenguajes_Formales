# Failure Function (KMP Prefix Function)

## Environment

| Item               | Version              |
|--------------------|----------------------|
| Operating System   | Windows 11           |
| Programming Language | Python 3.14.3      |
| Tools              | Terminal / Command Prompt |

## How to Run

1. Make sure Python 3 is installed on your system. You can verify by running:
   ```
   python --version
   ```
2. Open a terminal in the project folder and run:
   ```
   python tarea.py
   ```
3. The program will print the failure function array for the string `"abac"`. To test with a different string, edit the `print(compute_failure("your_string"))` call at the bottom of `tarea.py`.

## Algorithm Explanation

The program implements the **failure function** (also called the **prefix function**) used in the **Knuth-Morris-Pratt (KMP)** string-matching algorithm.

Given a pattern string `b` of length `n`, the failure function `f` is an array of size `n + 1` where `f[s]` stores the length of the longest proper prefix of `b[0..s-1]` that is also a suffix of that same substring.

### How it works

1. Initialize the array `f` with zeros and a variable `t = 0` that tracks the current matching prefix length.
2. Iterate through each position `s` from `1` to `n - 1`:
   - If the current character `b[s]` does not match `b[t]`, fall back using the failure function (`t = f[t]`) until a match is found or `t` reaches `0`.
   - If `b[s] == b[t]`, increment `t` and record `f[s + 1] = t`.
   - Otherwise, set `f[s + 1] = 0`.
3. Return the failure array `f`.

### Example

For the input `"abac"`, the output is:

```
[0, 0, 0, 1, 0]
```

This means:
- `f[0] = 0` (base case)
- `f[1] = 0` (`"a"` has no proper prefix that is also a suffix)
- `f[2] = 0` (`"ab"` — no match)
- `f[3] = 1` (`"aba"` — `"a"` is both a prefix and suffix)
- `f[4] = 0` (`"abac"` — no match)

### Time Complexity

The algorithm runs in **O(n)** time, where `n` is the length of the input string, making it efficient for preprocessing patterns in the KMP search algorithm.
