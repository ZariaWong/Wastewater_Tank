# Wastewater_Tank

Consider N wastewater tanks numbered sequentially from 0 to N-1 (N is at most 100). Each tank has at most one overflow pipes connects to another tank so the overflow wastewater can flow to another tank.  Note that the pipe has a valve so that if Tank A has a pipe connects to Tank B, wastewater can only flow from A to B through that pipe but not from B to A.
User can start filling wastewater into any tank, we call that starting tank.

E.g., Starting tank = 1 will have a capacity of 2 tanks until it is full because overflow wastewater will go to Tank 0.

E.g., Starting tank = 2 will have a capacity of 3 tanks until it is full because overflow wastewater will go in this sequence: Tank 2 -> Tank 5 -> Tank 4 -> Tank 5. Note that there is a cycle.


# Input specification

The first line contains a single integer, N, which is the total number of water tanks.

The second line contains N integers separated by spaces. The first integer defines the overflow tank for tank 0, the second for tank 1, and so on. A value of -1 denotes no overflow pipe from that tank.

The third line contains a single integer, E, and is the starting tank to fill in wastewater.

# Output specification

A single integer representing the amount of wastewater (in terms of number of tanks) that user can fil in from the starting tank.
