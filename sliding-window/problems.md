# Leetcode 209
* key : sub-array
* analysis : the key point is how to move the window. 一个困扰方面是如果left超过right怎么办。在这种情况下直接increment right.

# Leetcode 395
* key : 先以the number of unique chars为锚点让sliding windows有移动的依据。在此基础上track 相关状态，确定满足条件

# Leetcode 30
* 结合leetcode explore card: 彻底清晰一些基本原则
* 加快思考连续性和速度
- [X] Approach inspiration: Sliding-Window
* 细节推理的完整性
* 基于上一点叠加
* result: why cannot pass some test cases 
## Progress Conclusion 
* original questions: how to rely on table to track states
* 细节处理： 考虑到over-used words.也就是说点要全部考虑到。
* 对应how to apply sliding-windows: 首先是基本原理，其次是探索正确的思考步骤。<br>
比如这个问题情景： <br>
1. each word check  : hash-table condition 
2. check if valid substring: window expand 
## Reorganize thinking
1. how to check whether a substring is valid - purpose: 切入正确的思考路径和状态

## bug reports and progress conclusion
* 已经理清楚几个要点了，接下来直接去应用
* 状态变化： 循环中状态切换
### c++ size_t type computation
* 基础保持：signed integer and unsigned integer 


 
