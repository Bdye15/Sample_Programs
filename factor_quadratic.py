#!/usr/bin/env python3
# factor_quadratic.py

# factors any quadratic where all coefficients are positive

print("\nNote: This program does not work if negative terms are input.")
while True:
    J = int(input("\nThe coefficient of the x^2 term:\n"))
    if J > 0:
        break
    if J < 0:
        print("\nI'm sorry, I can't factor if terms are negative.")
    if J == 0:
        print("\nThere's no point in factoring if there's no x^2 term!")

while True:
    K = int(input("\nThe coefficient of the x term:\n"))
    if K > 0:
        break
    if K < 0:
        print("\nI'm sorry, I can't factor if terms are negative.")
    if K == 0:
        print("\nThere's no point in factoring if there's no x term!")

while True:
    L = int(input("\nThe constant term:\n"))
    if L > 0:
        break
    if L < 0:
        print("\nI'm sorry, I can't factor if terms are negative.")
    if L == 0:
        print("\nThere's no point in factoring if there's no constant!")

print("\nGiven the quadratic:")
if J == 1 and K == 1:
    print(f" \nx^2 + x + {L} = 0")
elif J == 1:
    print(f" \nx^2 + {K}x + {L} = 0")
elif K == 1:
    print(f" \n{J}x^2 + x + {L} = 0")
else:
    print(f" \n{J}x^2 + {K}x + {L} = 0")


def gcd_calc(a, b):  # calculates the greatest common divisor of a and b
    if b > a:
        a, b = b, a
    c = a - b
    while c > 0:
        if b > c:
            a = b
            b = c
        else:
            a = c
        c = a - b
    return b


def show_answer(gcd, e, f, g, h):  # prints the factored form and removes
    print("\nIn factored form:")  # unnecessary 1's
    if gcd != 1:
        if e == g and f == h:  # perfect square special case
            if e == 1:  # removes coefficient of 1
                print(f"\n{gcd}(x + {f})^2\n")
            else:
                print(f"\n{gcd}({e}x + {f})^2\n")
        elif e == 1 and g == 1:  # removes coefficients of 1
            print(f"\n{gcd}(x + {f})(x + {h})\n")

        elif e == 1:
            print(f"\n{gcd}(x + {f})({g}x + {h})\n")

        elif g == 1:
            print(f"\n{gcd}({e}x + {f})(x + {h})\n")

        else:
            print(f"\n{gcd}({e}x + {f})({g}x + {h})\n")

    if gcd == 1:  # so that a 1 is not printed as gcf
        if e == g and f == h:  # perfect square special case
            if e == 1:  # removes coefficient of 1
                print(f"\n(x + {f})^2\n")
            else:
                print(f"\n({e}x + {f})^2\n")
        elif e == 1 and g == 1:  # removes coefficients of 1
            print(f"\n(x + {f})(x + {h})\n")

        elif e == 1:
            print(f"\n(x + {f})({g}x + {h})\n")

        elif g == 1:
            print(f"\n({e}x + {f})(x + {h})\n")

        else:
            print(f"\n({e}x + {f})({g}x + {h})\n")


gcd1 = gcd_calc(J, K)
gcd2 = gcd_calc(gcd1, L)

J = J // gcd2
K = K // gcd2
L = L // gcd2

not_factored = True  # to check if the quadratic has been factored
a_save = 0  # stores the a value to exclude printing conjugate solutions

for a in range(1, J + 1):
    if J % a == 0:
        c = J // a

        for b in range(1, L + 1):
            if L % b == 0:
                d = L // b

                if a*d + b*c == K:
                    if a_save != c:
                        # compares the previous solution's a value to the new
                        # solution's c value, these will be the same
                        # if conjugates
                        show_answer(gcd2, a, b, c, d)
                        a_save = a
                        not_factored = False

if not_factored and gcd2 != 1:  # for when gcf is the furthest simplification
    print("In factored form:")
    print(f"\n{gcd2}({J}x^2 + {K}x + {L})\n")

if not_factored and gcd2 == 1:
    # if it's not factored with a gcf of 1, it's prime
    print("\nThis quadratic is prime.\n")
