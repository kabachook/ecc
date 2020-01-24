#!/usr/bin/env python3
from argparse import ArgumentParser
import sys
from sage.all import *


parser = ArgumentParser("Generate task on Pohlig-Hellman algo")
parser.add_argument("--p-start", type=int, default=2**128, help="min(p)")
parser.add_argument("--p-stop", type=int, default=2**256, help="max(p)")

if __name__ == "__main__":
    args = parser.parse_args()

    p = random_prime(args.p_stop, lbound=args.p_start)
    F = GF(p)
    E = None

    print(f"Finding curve with smooth order over field {F}", file=sys.stderr)
    while True:
        a, b = randint(1, p), randint(1, p)
        E_t = EllipticCurve(F, [a, b])
        print(E_t)
        order = E_t.order()
        print(f"Order = {order}")
        print(f"{order} = ", end="", file=sys.stderr)
        print(factor(order), file=sys.stderr)
        print("Countinue?[y]", file=sys.stderr)
        answer = input().lower()
        if "y" in answer:
            E = E_t
            E.set_order(order)
            break
    
    G = E.gens()[0]
    d = randint(E.order() // 10, E.order() - 1)
    P = d * G
    print(f"{P} = {d}*{G}", file=sys.stderr)
    print(f"{P} = d*{G}")
    print(f"d = ?")
    

