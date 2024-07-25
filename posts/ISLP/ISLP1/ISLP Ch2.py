---
title: "EasyPython Practice Ch8"
author: Ahyeong Jeong
date: "2024-07-25"
categories: [ISLP]
---

Concatenation 
```{python}
x = [3, 4, 5]
y = [4, 9, 7]
x + y
```
```{python}
import numpy as np
x = np.array([3, 4, 5])
y = np.array([4, 9, 7])
x + y
```

```{python}
x = np.array([[1, 2], [3, 4]])
x
x.ndim
x.dtype
```

```{python}
np.array([[1, 2], [3.0, 4]]).dtype
 #dtype float로 설정 
np.array([[1, 2], [3, 4]], float).dtype
x.shape
```

```{python}
x = np.array([1, 2, 3, 4])
x.sum()
x = np.array([1, 2, 3, 4])
np.sum(x)
```

```{python}
x = np.array([1, 2, 3, 4, 5, 6])
print('beginning x:\n', x)
x_reshape = x.reshape((2, 3))
print('reshaped x:\n', x_reshape)
x_reshape[0, 0]
x_reshape[1, 2]
```

```{python}
print('x before we modify x_reshape :\n', x)
print('x_reshpae before we modify x_reshape:\n', x_reshape)
x_reshape[0, 0] = 5
print('x_reshape after we modify its top left element:\n', x_reshape)
print('x after we modify top left element of x_reshape:\n', x)
```

(a)
```{python}
import pandas as pd 
college = pd.read_csv("College.csv")
```

(b)
```{python}
college2 = pd.read_csv('College.csv', index_col = 0)
college3 = college.rename({'Unnamed: 0': 'College'},
                            axis = 1 )
college3 = college3.set_index('college')
```
