The initial homework just required the students to write 8 functions:
down_up(n): return a list that counts down from n to 1 and back up to n.
filter(pred, xs): returns a list of all the elements in the list xs that satisfy the predicate pred.
make_even(xs): Take a list xs and modify it in-place so that all odd items become even (rounding down); returns nothing.
char_count(s): returns a dictionary mapping all the characters in string s to their frequency (count) in s.
counts(n, xs): returns a list of length n indicating how many elements in xs are equal to 0, exactly 1, ... till n-1.
primes_list(n): returns a list of the first n primes.
has_duplicates(xs): returns True iff the list xs contains one or more duplicate items.
inverse(d): takes a dictionary d and returns a dictionary where the values of d are the keys, and the values of the returned dictionary are lists of all the keys of d that pointed to that original value:



The first part of the challenge is just to solve these correctly. Put all your functions in one file.

The second part, where the real challenge lies, is to play "Python golf": write a file with all 8 functions in as few bytes as a possible. The solutions can be horribly inefficient and use any trick in the Python language.
