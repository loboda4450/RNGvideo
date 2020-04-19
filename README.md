# RNGvideo
Implementation of DOI: [10.23956/ijarcsse/SV7I5/0327](http://ijarcsse.com/Before_August_2017/docs/papers/Volume_7/5_May2017/SV7I5-0327.pdf) article in Python 3.8, uses PIL, time, numpy and math libs. Now it generates random values based on video instead of screenshot. 

Implementation could be better (just use Sieve of Eratosthenes to generate primes, not this shit I wrote) - still tho it's quite fast (generates 100k 8bit random numbers in about 7 seconds (using 16 workers, wth 1 it takes 3secs)). Generating histogram is now perfectly economical (probably can't be better). __No more left to say now, everything is fixed I guess XD__

##### Executing:

```python rng.py --single [range of random numbers]```

```python rng.py [size of sequence] [range of random numbers] [threads amount you want to use]```
