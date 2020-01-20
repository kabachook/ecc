# Smart attack on anomalous curves

## Task

Given arbitary curve `E` over finite field of size `p` with `E.order == p` and some point `P = d*G`, find `d`.

## Solution

This is a general ECDLP problem, but it can be simplified using Smart's attack.

First, we generate `P'` and `G'` in `p`-adic field `Q_p` using [Hensel's lift](https://en.wikipedia.org/wiki/Hensel%27s_lemma)

Next, we reduce new curve `E_1(Q_p)` to new curve `E_2(Q_p)`.

Apply P-Adic Elliptic log to get final equation for `d`

## How to generate task

```bash
(ecgen  --anomalous --fp 521 | ./gen_task.py) > >(tee task.txt) 2> >(tee log.txt >&2)
```

You will get two files:
- `task.txt` — task itself
- `log.txt` — task generator log with answer

## Links

- https://wstein.org/edu/2010/414/projects/novotney.pdf