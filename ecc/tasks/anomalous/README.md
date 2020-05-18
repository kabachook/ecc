# Smart attack on anomalous curves

## Description

If a curve E defined over finite field of size $p$, has a subproup with order of $p$, then ECDLP problem can be solved in $O(1)$ time. 

## Task

Given arbitary curve $E$ over finite field of size $p$ ($\mathbb{F}_{p}$) with $E.order == p$ and some point $P = d*G$, find $d$.

## Solution

This is a general ECDLP problem, but it can be simplified using Smart's attack.

First, we generate $P'$ and $G'$ in $p$-adic field $Q_{p}$ using [Hensel's lift](https://en.wikipedia.org/wiki/Hensel%27s_lemma)

Next, we reduce new curve $E_{1}(Q_p)$ to new curve $E_{2}(Q_p)$.

Apply P-Adic Elliptic log to get final equation for $d$

## How to generate task

- Install [ecgen](https://github.com/J08nY/ecgen)

- Generate task:

```bash
(ecgen  --anomalous --fp 521 | ./gen_task.py) > >(tee task.txt) 2> >(tee log.txt >&2)
```

You will get two files:

- `task.txt` — task itself
- `log.txt` — task generator log with answer

## Other tasks

- PoliCTF 2012 Crypto 200. [Writeup by MSLC](http://mslc.ctf.su/wp/polictf-2012-crypto-500/)
- SharifCTF 2016 Crypto 350 — British Elevator. [Writeup 1 by hxp team](https://hxp.io/blog/25/SharifCTF-2016-crypto350-British-Elevator-writeup/). [Writeup 2 by Shiho Midorikawa](https://gist.github.com/elliptic-shiho/e76e7c2a2aff228d7807)
- DEFCON Quals 2020 - nottobefooled. [Writeup by Ariana1729](https://github.com/Ariana1729/CTF-Writeups/tree/master/2020/DEFCON/notbefoooled) (interesting thing here is that we need to do the opposite - generate an anamolous curve which is not affected by Smart attack)

## Links

- https://wstein.org/edu/2010/414/projects/novotney.pdf

!!! note
    There is a problem when an anomalous curve is isomorphic to its lifted curve over Q_p.  
    Then we randomize the lift to some curve $y^2 = x^3 + (p+a')*x + (b + p*b')$  
    More info [here](https://crypto.stackexchange.com/questions/70454/why-smarts-attack-doesnt-work-on-this-ecdlp)
