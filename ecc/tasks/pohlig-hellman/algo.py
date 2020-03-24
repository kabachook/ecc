from sage.all import *

def pohlig_hellman(curve, G, H, verbose=False):
    def log(*args, **kwargs):
        if verbose:
            print(*args, **kwargs)

    n = curve.order()
    log(f"Order = {n}")
    factors = factor(n, verbose=1 if verbose else 0)
    log(f"Factorization: {factors}")
    v = []
    moduli = []

    # 1. Decompose one DLP to many DLPs
    for p_i, e_i in factors:
        log(f"{p_i}**{e_i}: ", end="")
        order = p_i ** e_i # Order of new group
        moduli.append(order)
        power = n // order # Power to make new generator and point
        G_i = G * power
        H_i = H * power

        x_i = G_i.discrete_log(H_i, order) # H_i = x_i*G_i mod p_i**e_i
        log(x_i)
        v.append(x_i)

    # 2. Use CRT to solve congruences x = x_i mod p_i**e_i
    x = CRT_list(v, moduli)

    return x % n
