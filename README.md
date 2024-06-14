### Python Algebra Equation Solver

This function `solve_equation` solves a simple algebraic equation in the form of a string. It extracts numeric values from the string, performs arithmetic operations, and prints the result.

**Function Signature:**
```python
def solve_equation(insert: str):
```

**Parameters:**
- `insert`: A string representing an equation in the format `"num1 + num2 = num3"`.

**Example Usage:**
```python
solve_equation("3 + 7 = 30")
```

**Function Explanation:**
1. **Parsing the Input:**
   - Extracts `num1`, `num2`, and `num3` from the input string.
   - Converts these extracted substrings into integers.

2. **Calculating the Solution:**
   - Computes `num3 - num2`.
   - Divides the result by `num1` to find the value of `x` in the equation.

3. **Output:**
   - Prints the computed value of `x`.

**Example Output:**
```
First Extract 7 from 30 then you have 23 then divide 23 from 3 and you have
x : 7.666666666666667
```

### Python Matrix Add Function

This function `plus_matrix` adds two 3x3 matrices and prints the resulting matrix.

**Function Signature:**
```python
def plus_matrix(matrix0, matrix1):
```

**Parameters:**
- `matrix0`, `matrix1`: Lists representing 3x3 matrices in row-major order (flattened form).

**Example Usage:**
```python
matrix_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
matrix_b = [9, 8, 7, 6, 5, 4, 3, 2, 1]
plus_matrix(matrix_a, matrix_b)
```

**Function Explanation:**
1. **Matrix Representation:**
   - `matrix0` and `matrix1` are flattened lists representing 3x3 matrices.
   - Each matrix is represented by 9 elements in a row-major order.

2. **Adding Matrices:**
   - Adds corresponding elements of `matrix0` and `matrix1` to form a new matrix `plus`.

3. **Output:**
   - Prints the resulting matrix `plus` row by row.

**Example Output:**
```
[10, 10, 10]
[10, 10, 10]
[10, 10, 10]
```

**Note:** Ensure that the input matrices (`matrix0` and `matrix1`) are provided correctly as lists of 9 integers each, representing the elements of a 3x3 matrix in row-major order.

These functions are designed to perform specific tasks related to algebraic equations and matrix operations and provide direct outputs based on their respective functionalities.
