# 3x+1 aka *Collatz-Conjecture*

The Collatz-Conjecture is one of the most arduous unsolvable math problem in the world, One that young mathematicians are warned not to waste their time on.
This problem is also known as _Ulam conjecture,  Kakutani's problem, Thwaites conjecture, Hasse's algorithm, Syracuse problem_ or simply the _3n+1_. 

The sequence of numbers involved is sometimes referred to as the _Hailstone Sequence/Numbers/Numerals_ (because the values are usually subject to multiple descents and ascents like hailstones in a cloud), or as _Wondrous numbers_

**_"Mathematics is not yet ripe enough for such questions"_** - Paul Erdős
---
This is a simple conjecture yet it hasn't been solved by anyone in the world so far. Even then many are tempted to fall into this trap.

This problem is simply stated, easily understood, and all too inviting. Just pick a number, any number: If the number is even, cut it in half; if it’s odd, triple it and add 1. Take that new number and repeat the process, again and again. If you keep this up, you’ll eventually get stuck in a loop(...4,2,1). At least, that’s what we think will happen. 

Many might mistake the pattern to be of a fixed set for this infamous problem _3x+1_, Although it is not. Alex Kontorovich and Yakov Sinai had found out that there was an arbitary pattern to this problem. They researched, graphed and analyzed it.

Say, let us consider a sequence of large numer chosen at random, for instance(162,227,794). The graph peaks and drop so low that you cant really see what is happening at that scale. But if we took a log, we'd be able to find wiggle graph with a downward trend. And if we removed the linear trend, in the end we'd be able to get a _Geometric Brownian Motion_.

---
Here, I have made a simple python program which takes an input of your random number and eases your boiling brains from solving all by yourself.
Also I've visualized it in a 2D graph using matplotlib (yet to push) :) 
***
![Collatz_2880x1620_Lede](https://user-images.githubusercontent.com/79180908/231666072-3e87b0f2-aa2f-4d53-9f2d-372308b3767e.jpg)

