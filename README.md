# python-infix-to-rpn
Infix to Reverse Polish Notation using Python.

## Usage
Each number and operator must be seperated by a space.

```py
from infixtorpn import InfixToRPN
print(InfixToRPN.run("3 + 4 * 2 / ( 1 − 5 ) ^ 2 ^ 3"))
>>> 3 4 2 * 1 5 − 2 3 ^ ^ / +	 
```
