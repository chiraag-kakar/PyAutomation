# Truth Table Generator
Truth Table Generator is a tool that allows to generate a truth table with the help of ttg module.

## Installing Dependency
To install the ttg module, we can use pip command. Run the below pip command to
download the PyPDF2 module:

```python3
pip install truth-table-generator
```

## Dependency Expalined
* A truth table has one column for each input variable and one final column showing all of the possible results of the logical operation that the table represents. 
* If the input has only one list of strings, each string is considered an input variable.
* A second list of strings can be passed with propositional expressions created with logical operators.

## Operator Notations
* negation: 'not', '-', '~'
* logical disjunction: 'or'
* logical nor: 'nor'
* exclusive disjunction: 'xor', '!='
* logical conjunction: 'and'
* logical NAND: 'nand'
* material implication: '=>', 'implies'
* logical biconditional: '='
---
Note: Use Parenthesis in boolean expressions to avoid precedence errors.


## Running the Code Snippet Locally
To run the project locally :
* Clone the git repo.
* Then from the terminal/ command prompt navigate to the pdf2text directory of the cloned repo.
* Run the *truthtable.py* file using the following command:
```
python truthtable.py
```
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
