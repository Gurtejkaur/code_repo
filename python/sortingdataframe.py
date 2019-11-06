import numpy as np
import pandas as pd

from pandas import Series, DataFrame
DF_obj = pd.DataFrame(np.arange(36).reshape(6,6))
DF_sorted = DF_obj.sort_values(by=[5], ascending=[False])
print(DF_sorted)
