# Chain of fools/CurveBall attack

## Description

If the clinet/server does not check the certificate parameters with some fixed ones (e.g. secp521p), the certificate can be spoofed.

## Task

Given arbitary certificate, forge a new pair of private and public keys, create a new CA using new keys, sign a new certificate for TLS.

## Solution

See [`./poc/gen.sh`](./poc/gen.sh)

## Links

- https://blog.lessonslearned.org/chain-of-fools/
- https://research.kudelskisecurity.com/2020/01/15/cve-2020-0601-the-chainoffools-attack-explained-with-poc/