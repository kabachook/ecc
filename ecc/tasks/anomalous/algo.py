#!/usr/bin/env python3
"""
Smart attack implementation. Taken from https://wstein.org/edu/2010/414/projects/novotney.pdf and slightly modified
Paper Copyright Peter Novotey 2014
"""
from typing import Union
from sage.all import *
from sage.schemes.elliptic_curves.ell_point import *


def hensel_lift(P: EllipticCurvePoint, p: Integer, prec: Union[None, Integer]) -> EllipticCurvePoint:
    E = P.curve()
    Eq = E.change_ring(QQ)
    Ep = Eq.change_ring(Qp(p,prec))
    x_P,y_P = P.xy()
    x_lift = ZZ(x_P)
    y_lift = ZZ(y_P)

    # x, y, a1, a2, a3, a4, a6 = var('x,y,a1,a2,a3,a4,a6')
    # f(a1,a2,a3,a4,a6,x,y) = y^2 + a1*x*y + a3*y - x^3 - a2*x^2 - a4*x - a6
    # g(y) = f(ZZ(Eq.a1()),ZZ(Eq.a2()),ZZ(Eq.a3()),ZZ(Eq.a4()),ZZ(Eq.a6()),ZZ(x_P),y)
    # gDiff = g.diff(y)

    y = var('y')
    a1, a2, a3, a4, a6, x = ZZ(Eq.a1()), ZZ(Eq.a2()), ZZ(Eq.a3()), ZZ(Eq.a4()), ZZ(Eq.a6()), ZZ(x_P)
    g = y**2 + a1*x*y + a3*y - x**3 - a2*x**2 - a4*x - a6
    gDiff = g.diff()
    
    for i in range(1,prec):
        uInv = ZZ(gDiff(y=y_lift))
        u = uInv.inverse_mod(p^i)
        y_lift = y_lift - u*g(y_lift)
        y_lift = ZZ(Mod(y_lift,p^(i+1)))
    y_lift = y_lift+O(p^prec)
    return Ep([x_lift,y_lift])

def smart_attack(P: EllipticCurvePoint, Q: EllipticCurvePoint,  p: Integer, prec: Union[None, Integer]) -> Integer:
    E = P.curve()
    Eqq = E.change_ring(QQ)
    Eqp = Eqq.change_ring(Qp(p,prec))

    P_Qp = hensel_lift(P,p,prec)
    Q_Qp = hensel_lift(Q,p,prec)

    p_times_P = p*P_Qp
    p_times_Q=p*Q_Qp

    x_P,y_P = p_times_P.xy()
    x_Q,y_Q = p_times_Q.xy()

    phi_P = -(x_P/y_P)
    phi_Q = -(x_Q/y_Q)
    k = phi_Q/phi_P
    k = Mod(k,p)
    return k


