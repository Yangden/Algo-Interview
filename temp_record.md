# Leetcode 31
* how to from **next** permutation(naive and brute-force)

# Leetcode 2405 review 
* what can i do : partition strings into substring(unque characters - constraint)
* optimize: minimum number of partition

* brute-force: It is feasible to consider recursion 

* feasible

# Leetcde 285
* stack-based tree traversal(in-order)
## How stack is applied 
* init: node = root;
while (node->left) {
    push(node->left)
    node = node->left
}
pop
right - push. 
node - node->right 
* cutting point: break; 
* if - right: push to stack
* while node->left, push(node->left)
* pop. if -> right : push. 
* while (!st.empty()) {
    wh
}

## Implementation:  
p->val : pop

# Leetcode 529
* Topic : DFS 
* recursion : 
- reveal Mine: game over
- Empty sqaure - iterate through all adjascent 

# Leetcode 743
* idea: BFS -> Dijstraka algorithm 
* from the source node in the set
* all neighbors accessed : update distance(not in set )
* minheap - <distance, point> : pop 
* add to set : Then update all affected neighbors (those not in set)
* 如何做到一步犹豫。 
* 行动开始 
* if : distance array : 
* heap - pop : update 
* if separate : 

* Implementation
 - while loop(error) :  
  - min distance - Add to set : 
  + not in the set: (All in the set or INT_MAX remain )
  - update: excet those not in set : update 
  - cnt -> detect all nodes? 
## Improvements

# Leetcode 749 
* constraint : wall & 
* day counter : dynamic change - install wall around one region 
* target: return the number of walls
* Tranalate the problem and how to think : 
- regions 
- each day, if not contaimented grwo
- region decide the number of walls

## Solution
- use search to decide the region
- decide the number of walls 
- how to decide grow : same thing 
- store positions : vector<vector<int>> : track the number of cells 

- tack the number of contempted region 
the number of walls 

- for each day
check if fully  spread: break; - return the number of walls
block _mask
consider what to block : 
after block 

How to grow: for each : blank : spread : increase the number of affected regions 
* what if each time select to contain the regio with most affected : 

- each iteration is one day:
for each day : blocked : 
breakl 
： select which to blocl
after selection: iterate through : edge cells found : accessed_set : add wall number - use hash set 
: grow (on infected_set) : add number 

if number - full break; 

* continue: [[0,1,0,0,0,0,0,1],[0,1,0,1,0,0,0,1],[0,0,0,0,0,0,0,1]]
[0, 1, 0, 0, 0, 0, 0, 1]
[0, 1, 0, 1, 0, 0, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 1]

5 + 4 + 

[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,0,0],
[1,0,0,0,0,0,0,0,0,0],
[0,0,1,0,0,0,1,0,0,0],
[0,0,0,0,0,0,1,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,0],
[0,0,0,0,1,0,1,0,0,0],
[0,0,0,0,0,0,0,0,0,0]]



# leetcode 2405 
* bit approach
* flag ? 
* bitmask : how to set ? 


