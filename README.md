# python-infix-to-rpn
Infix to Reverse Polish Notation (Postfix) using Python.

## Usage
Each number and operator must be seperated by a space.

```py
import infixtorpn
print(infixtorpn.convert("3 + 4 * 2 / ( 1 − 5 ) ^ 2 ^ 3"))
>>> 3 4 2 * 1 5 − 2 3 ^ ^ / +	 
```
