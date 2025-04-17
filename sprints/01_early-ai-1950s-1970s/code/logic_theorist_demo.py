# logic_theorist_demo.py
from sympy import symbols, Implies, satisfiable

# Define propositions p and q
p, q = symbols('p q')

# Given (p -> q) and p, infer q
theorem = Implies(p, q) & p
model = satisfiable(theorem)
print('Satisfiable model:', model)
