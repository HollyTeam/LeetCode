### 题目：
有两个分别代表两个非负整数的非空链表，每一位以倒叙的形式存放在链表的结点中，将这两个数相加并返回结果链表；假设这两个数开头不会为0，即不会有012(2->1->0)这种形式，除了0本身；

```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
```

### 分析：
首先，链表l1和l2分别代表两个非负整数，并且存储的形式已经是倒过来的：比如 `123 + 45`就是 `3->2->1  +  5->4` `3+5,  2+4 , 1`, 因此，这道题中运算已经对齐，就不需要考虑对齐的问题；如果是正序存储，则可以使用倒序存储的方法达到运算时对齐的目的；
其次，首先要考虑的就是进位的问题，在这里我使用了一个进位标志（用于指示下一次运算是否需要进位）以及让进位的大小为1；
还有需要考虑的问题是，当链表l1和l2长度不同时的处理；
最后还需要考虑的是当两个链表都加完了，是否还有需要进位的情况，比如：`5->6->7  +  3->2->8` 运算完结果应该是 `8->8->5->1`而不是`8->8->5`;

### 输出：
leetcode 上测试通过；同时发现有时候提交上去的代码，运行的时间每次都不太一样；

### 总结：
我这里不是最优的算法，空间复杂度上，我是新创建了`temp_node`作为结果链表，从而增加了空间复杂度，其实可以直接在l1和l2中，较长的链表上进行操作；时间复杂度为`O(max{m, n})`，其中，m和n分别为链表l1和l2的长度

### 文件说明：
`readme.md`
`add-two-numbers.py`    **Solution** 
`test.py`    **本地测试的可执行文件，内含 结点类，创建链表的函数，链表相加函数**

