import time
from random import randint
from dataclasses import dataclass, asdict, astuple
from itertools import groupby, chain, count, takewhile, dropwhile
from collections import namedtuple, Counter

@dataclass
class Comment:
    id: str
    text: str
    likes: int
    status: bool

Comment1 = Comment("12", "comment text", 4, True)
# Comment2 = Comment("24", "commm", 42, False)

# c = asdict(Comment1)
# c1 = astuple(Comment1)
# print(f"{c} \n{c1}")


# emojis = ['\U0001F600', '\U0001F605', '\U0001F60D']
# start = time.time()
# for i in range(10):
#     print(emojis[randint(0, len(emojis) + -1)])
#     time.sleep(1)
# end = time.time()
# print(end - start)


# inputArray = [3, 6, -2, -5, 7, 3]
# l = []
# for i in range(len(inputArray)-1):
#     x = inputArray[i] * inputArray[i+1]
#     l.append(x)
# print(max(l))

# def dropwhile1(n):
#     return n

# x = ['ali', 'toshmat', 'azim']
# x1 = [2, 4, 5, 7, 8, 9]

# print(list(chain.from_iterable(x)))

# print(list(dropwhile1(dropwhile(lambda r: r > 5, x1))))



# def func():
#     i = 1

#     while True:
#         yield i * i
#         i += 1

# for s in func():
#     if s > 200:
#         break
#     print(s)



# s = ['odam', 'moshina', 'dasturchi']
# s1 = list(chain.from_iterable(s))
# print(s1)

# s2 = Counter(s1)
# print(s2.most_common(2))

