可以参考 [写树算法的套路框架](https://leetcode-cn.com/problems/same-tree/solution/xie-shu-suan-fa-de-tao-lu-kuang-jia-by-wei-lai-bu-/)

要判断两棵树是否相同，就是判断对应节点是否相同。

则有三种情况：
1. 节点p和q都为空，True
2. 节点p和q一个位空一个不为空，False
3. 节点p和q都不为空，但是存储的值不一样，False

最后，再递归调用函数`isSameTree()`，传入当前判断的两棵树相同位置的节点p和q对应的左子节点、右子节点