```{python}
import pandas as pd
import numpy as np
house_df = pd.read_csv("./house_price/train.csv")
house_df.shape
```

```{python}
price_mean = house_df["SalePrice"].mean()
price_mean
```

sub_df에 있는 SalePrice값 다 평균으로 바꾸기 
```{python}
sub_df = pd.read_csv("./house_price/sample_submission.csv")
sub_df['SalePrice'] = price_mean
sub_df
```

기존 csv에 바뀐 csv로 바꿔치기 
```{python}
sub_df.to_csv("./house_price/sample_submission.csv", index = False)
```


```{python}

```

