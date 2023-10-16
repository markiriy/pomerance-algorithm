# The algorithm of Pomerance et al . Calculations of spsp numbers.
https://kpfu.ru//staff_files/F406287292/_tom1_nom1.pdf  &lt; p. 67.

**The algorithm consists of three stages. 
At the first stage, the sieve of Eratosthenes is performed on an interval bounded by a certain number B, and all primes are eliminated.
At the second stage, the numbers that do not satisfy the propositions 1 and 2 formulated above are eliminated for a=2 and small primes p. For example, since l_2(p) = 4, psp class 15 (mod 20) cannot contain psp(2) numbers. Similarly, the second sentence weeds out multiples of squares 9, 25, 49, etc. Fulfilling these conditions requires the same or less amount of time and does not increase the time complexity and memory requirements.
At the third stage, the remaining numbers are tested for the fulfillment of conditions (5) directly by definition, and this part is the most time-consuming."**

This code calculates pseudo-simple numbers for different limits on the bases (2;3) and then builds a graph showing the dependence of the execution time on the limit of numbers. 
Uses the matplotlib library for visualization.
