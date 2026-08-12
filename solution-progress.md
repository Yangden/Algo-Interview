# progress
* Leetcode 80 : Notes in leetcode web page
* mark:Leetcode 30 : not totally clear: write it later focusing on sliding-window: adjustment
* cover all lcs problems: thinking-pattern:not repeat + right path + question descriptions + code logics organization
* thinking-pattern failed: leetcode 1769 optimization

# leetcode 355 
* concurrency : counter problem. then i record each tweet with a timestamp, and sort using timestamp. 
* if using a global counter : lockk. 

# Reconstruct Leetcode 819
**Logics**
```
HashMap count;
HashSet ban(banned);
parse(paragraph) -> list;
iterate - compute; 

// edge case analysis
/* Consider space ' ' and punctuation symbols*/
parse(paragraph) -> list
set delimiter as ' '
obtain each unit
remove punctuation symbols
transform to lower-case 
```
**C++ implmentation**

# Leetcode 218
**trace: input:[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]**
```
sort the right edge: arr:[[7, 1], [9, 0], [12, 2], [20, 3], [24, 4]];
set two pointers : pos1 : input. pos2: arr
max_heap: maintain the highest height :[height, index_of_building]. init: [[0, 0]]
pop_set(hash_set): record buildings already popped out(right_edge accessed)

while (pos1 < size1 || pos2 < size2) {
    // move the position on the smaller side, when hit the boundary, do not move

    // handle left edge
    push height to heap
    if (height > heap.top()) : emit result : [edge_val, height]

    // handle right edge 
}


1. smaller(2 < 7>) : left_edge-push [10, 0] to heap; pos1++; (10 > 0) : emit (2, 10)
2. (3 < 7>) : push [15, 1] to heap. emit (3, 15)
3 : 5 < 7 : push [12, 2]. 12 < 15: not emit result. 
4: 15 > 7: right_edge condition: should delete index_1 building. insert 1 to pop_set. 
    // record max_val
    max_val = heap.top()
    while (heap.top()->index in pop_set):
        pop out; 
    
    if (max_val > heap.top()) { // emit result
        [7, heap.top() - 12]

    }
5: 9 < 15:

6: 12 < 15
emit [12, 0]
heap: [10, 3]
7: 15 <20> : left edge
[15, 10]

8: heap : [8, 4]

9: exhaust left edges


```