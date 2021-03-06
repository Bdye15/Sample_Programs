# calculator.py

# can perform the four basic operations, plus differentiation, definite, and
# indefinite integration

import sympy

x, y, z = sympy.symbols("x y z")


def find_suffix(num):  # attaches the correct suffix to the "nth" derivative
    if num % 10 == 1:
        return "st"
    elif num % 10 == 2:
        return "nd"
    elif num % 10 == 3:
        return "rd"
    else:
        return "th"


def basic():  # simple addition, subtraction, multiplication, or division
    a = sympy.sympify(input("\nEnter your operation:\n"))
    print(f"\n{a}\n")


def differentiate():  # derivatives
    print("\nNote: Use '**' to represent exponents.\n\t'2x', must be '2*x', "
          "etc.\n\tSquare roots must be 'sqrt()'\n\tInverse trig must be "
          "'acos', etc.")  # tells the user how to correctly format their input
    f = sympy.sympify(input("\nEnter your function:\n"))
    n = int(input("\nWhich derivative do you want?\n"))

    suffix = find_suffix(n)

    f_prime = sympy.simplify(sympy.diff(f, x, n))

    print(f"\nThe {n}{suffix} derivative of {f} is {f_prime}\n")


def indef_integrate():  # indefinite integrals
    print("\nNote: Use '**' to represent exponents.\n\t'2x', must be '2*x', "
          "etc.\n\tSquare roots must be 'sqrt()'\n\tInverse trig must be "
          "'acos', etc.")  # tells the user how to correctly format their input
    f = sympy.sympify(input("\nEnter your function:\n"))
    F = sympy.simplify(sympy.integrate(f, x))

    print(f"\nThe integral of {f} is {F}\n")


def def_integrate():  # definite integrals
    print("\nNote: Use '**' to represent exponents.\n\t'2x', must be '2*x', "
          "etc.\n\tSquare roots must be 'sqrt()'\n\tInverse trig must be "
          "'acos', etc.")  # tells the user how to correctly format their input
    f = sympy.sympify(input("\nEnter your function:\n"))
    a = sympy.sympify(input("\nEnter your lower bound:\n"))
    b = sympy.sympify(input("\nEnter your upper bound:\n"))
    F = sympy.simplify(sympy.integrate(f, (x, a, b)))

    print(f"\nThe integral of {f} on the interval {a} to {b} is {F}\n")


while True:
    operation = input("\nWhich operation would you like to perform?\n"
                      "1. Addition, Subtraction, Multiplication, or Division\n"
                      "2. Differentiation\n3. Integration\n")

    if operation == "1":
        basic()

    if operation == "2":
        differentiate()

    if operation == "3":
        def_indef = input("\nWould you like to take the definite or "
                          "indefinite integral?\n1. Indefinite\n2. Definite\n")

        if def_indef == "1":
            indef_integrate()

        if def_indef == "2":
            def_integrate()

    print("Press 'x' to exit, or press enter to try another operation.")
    if input() == "x":
        break
