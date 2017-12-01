### 题目：
给定一个数组，返回数组中两个元素相加后，结果为目标值target的下标数组；假定，只有一个结果，即不会出现数组中有两种方案使得他们相加都能得到target,并且同一个元素只能使用一次；

```
Input: nums=[2, 7, 11, 15]， target = 9
Output: [0,1]
```

### 分析：
首先，最能想到的思路就是，两层循环遍历：对于每一个nums[i],遍历i+1 -> len(nums)-1,如果有符合条件的则返回，但是这样的话时间复杂度较高为O(n^2)；
因此，采用增加空间复杂度，减少时间复杂度的方法：首先用字典存储，键为nums,值为nums[i]对应的index,这样就能根据nums[i]得到 索引值i；对于每一个nums[i],用target-nums[i]得到差值，再判断差值是否在字典中的键集合，如果在，则将[i, dict.get(d_value)]返回
还有就是通过`if len(set(result)) == 1:`判断是否出现了[i,i]的情况，如果是的话`continue`进入下一次循环

### 总结：
一开始想到的是第一种方法，后来发现可以免去里层循环；

### 文件说明：
`readme.md`</br>
`TwoSumSolution.py`    **Solution**  </br>
`test.py`    **本地测试的可执行文件**