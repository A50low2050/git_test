from typing import List

data = 'ab fabc def ac abd'

def func(s1: str, prefix: str) -> List[str]:
    words = s1.split()
    result = [word for word in words if len(word) >= 2 and prefix in word]

    return result

f = func(data, "ab")
print(f)
#____________________________________________

data_2 = 'ab fabc def ac abd'

def func_2(s1: str, prefix: str) -> List[str]:
    words = s1.split()

    result = [word for word in words if len(word) >= 2 and word.find(prefix) != -1]
    return result

f2 = func_2(data_2, "ab")
print(f2)
