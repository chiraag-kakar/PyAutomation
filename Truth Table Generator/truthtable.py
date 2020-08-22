# importing truth table generator module
import ttg
import pandas

print(ttg.Truths(['p', 'q', 'r']))
exp1 = 'p and q and r'
exp2 = 'p or q or r'
exp3 = '(p or (~q)) => r'

table1 = ttg.Truths(['p', 'q', 'r'], [exp1, exp2, exp3 ])
print(table1)
print(table1.as_prettytable())
print(table1.as_tabulate(index=False, table_format='latex'))
table1.as_pandas()
table1.as_pandas().style.set_properties(**{'text-align':'center'}).hide_index()
print(table1.as_tabulate())
print(table1.as_tabulate(index=False))
print(table1.valuation())
print(table1.valuation(4))

table2 = ttg.Truths(['p', 'q', 'r'], [exp1, exp2, exp3 ], ints=False)
print(table2)