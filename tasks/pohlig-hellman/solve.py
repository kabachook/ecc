#!/usr/bin/env python3
from argparse import ArgumentParser
import sys
from sage.all import *
from algo import pohlig_hellman

parser = ArgumentParser("Solve task on Pohlig-Hellman algo")
parser.add_argument("--a", type=int, required=True)
parser.add_argument("--b", type=int, required=True)
parser.add_argument("--p", type=int, required=True)
parser.add_argument("--gx", type=int, required=True)
parser.add_argument("--gy", type=int, required=True)
parser.add_argument("--Px", type=int, required=True)
parser.add_argument("--Py", type=int, required=True)
parser.add_argument("--order", type=int, required=False)

if __name__ == "__main__":
    args = parser.parse_args()
    F = GF(args.p)
    E = EllipticCurve(F, [args.a, args.b])
    G = E(args.gx, args.gy)
    P = E(args.Px, args.Py)

    if args.order:
        E.set_order(args.order)

    d = pohlig_hellman(E, G, P, verbose=True)
    print(d)
    print(G.discrete_log(P))