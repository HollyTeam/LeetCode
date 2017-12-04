### 题目：
判断是否为回文数字

### 分析：
这里我用了python的语法糖，将该数字转成string，然后对该string取逆，判断二者是否相等：```str(x) == str(x)[::-1]```
今天看了下discussion以及Soolutions里的讨论，发现了这么一段话
```
VinzDude commented last week
Extra space is a consideration for people who want to convert number to String and then solve it. If you go that route, you violate extra space constraint.
```
也就是题目的 额外空间，可能是不想要玩家使用int转str的方法来解题；
</br>
以下是`solution`：
如果x＜0或者x==10那么就直接返回，这两种都不是回文数；
如果用变量reverse_number存储数字右半边的逆， 每次都让reverse_number为reverse_number * 10 + x % 10</br>
让x成为左半边，x = x // 10，让x减少一位，而当x<=reverse_number的时候即可退出循环；</br>
最后返回x与reverse_number的关系至于return那里，有两种情况，一种是回文数位数为偶数的情况，一种是为奇数的情况 
比如： x = 12321
reverse_number = 0 
x > reverse_number:
    reverse_number = reverse_number * 10 + x % 10   `1`
    x = x // 10   `1232`

x > reverse_number:
    reverse_number = reverse_number * 10 + x % 10   `12`
    x = x // 10   `123`

x > reverse_number:
    reverse_number = reverse_number * 10 + x % 10   `123`
    x = x // 10   `12`
退出循环
此时x == reverse_number // 10 为True