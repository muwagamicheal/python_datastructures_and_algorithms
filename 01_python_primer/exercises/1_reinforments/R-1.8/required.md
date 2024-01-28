## Assignment
Python allows negative integers to be used as indices into a sequence,such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references the same element?

## Solution(s)
### 1. Indexing
The above assignment requires us to have an understanding of indexing in python. The expresssion −n ≤ k < 0 is used to denote negative indexing, here elements are accessed from the last backwards to the first in the squence. The expression j ≥ 0 denotes "postive indexing" elements are accesed from the start of the squence towards the end.
To convert a negative index k to its equvalent postive index j, you simply add the length of the sequence n to it.
Consider the string n = Hello with lenght of 5.

| Postive index  | Character  |Negative index |Equivalent postive index |
| :------------- | :----------| --------------| ------------------------|
| 0              | H          |-5             |0+5=5                    |
| 1              | e          |-4             |1+5=6                    |
| 2              | l          |-3             |2+5=7                    |
| 3              | l          |-2             |3+5=8                    |
| 4              | o          |-1             |4+5=9                    |
