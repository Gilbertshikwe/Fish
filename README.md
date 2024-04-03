# Fish in the River

You are given two non-empty arrays A and B representing N voracious fish in a river, ordered from upstream to downstream. Array A contains the sizes of the fish, and array B contains the directions (0 for upstream, 1 for downstream) of the fish. If two fish move in opposite directions and there are no other (living) fish between them, they will eventually meet each other. Compute the number of fish that will stay alive.

## Function Signature:

``` python
def solution(A, B):
    pass
```
### Parameters:
A: A non-empty list of integers representing the sizes of the fish.
B: A non-empty list of integers representing the directions of the fish (0 for upstream, 1 for downstream).
### Returns:
An integer representing the number of fish that will stay alive.
Example:
A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]
print(solution(A, B)) 
### Constraints:
N is an integer within the range [1..100,000].
Each element of array A is an integer within the range [0..1,000,000,000].
Each element of array B is either 0 or 1, where 0 represents upstream and 1 represents downstream.

This README provides an overview of the problem statement, the function signature, parameters, return value, an example, and constraints of the problem. It helps users understand what the problem is about and how to use the provided function.


