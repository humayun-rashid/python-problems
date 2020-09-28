"""
Task 4.
When sending data, for example online, we can only send 1 and 0. This means electricity on or
electricity off. We could also send data in same way by flashing a flashlight between buildings
(though morse-code might be more relevant in that case).
For the purposes of this task, we represent the sent data as a string, like ”0101110011”.
In error correction methods, one simple way is to add a parity bit in the end. If the sent data
has an even number on 1’s, we add another to the end. If the data has an odd number of 1’s, we
add a 0. The purpose is that when the data is received, we can check how many 1’s there are. If
there is an even number of 1’s, we know an error must have happened (maybe someone walked
between the buildings and 1 turned into 0 as we could not see the light).
Write a programthat asks a bit-sequence from the user and adds a paritybit.
Example run 1:
Give a bit pattern: 01101
Parity bit added: 011010
Example run 2:
Give a bit pattern: 11001100
Parity bit added: 110011001
Note: This would be quite inefficient error detection system. There exist a lot better error
detection and correction algorithms, but that is out of our scope.
"""