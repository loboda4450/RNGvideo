# RNGvideo
Implementation of DOI: [10.23956/ijarcsse/SV7I5/0327](http://ijarcsse.com/Before_August_2017/docs/papers/Volume_7/5_May2017/SV7I5-0327.pdf) article in Python 3.8, uses PIL, time, numpy and math libs. Now it generates random values based on video instead of screenshot. 

Implementation could be better (just use Sieve of Eratosthenes to generate primes, not this shit I wrote) - still tho it's quite fast (generates 100k 8bit random numbers in about 3 seconds). ~~It's not the perfect one, but good tradeoff in terms of time complexity and results (You should not use this one to protect your data, cuz it takes a screenshot after executing XD)~~ No, now it's so fckin hardware bloating. It consumes as much RAM, as you give'em. Tbh I recommend not to use more than 8 threads if u have 16GB of RAM, cuz u won't even notice when your PC will use swap XD.

But there's **ONE** good thing - generating histogram is now perfectly economical (probably can't be better).

##### Executing:

```python rng.py --single [range of random numbers]```

```python rng.py [size of sequence] [range of random numbers] [threads amount you want to use]```
