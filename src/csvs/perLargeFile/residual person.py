import numpy as np
import statsmodels.api as sm

# Tabela grande
L = np.array([[3018, 1661, 1389], [10505, 11862, 12134]])
table_large = sm.stats.Table(L)
resid_pearson_large = table_large.resid_pearson
standardized_resids_large = table_large.standardized_resids

# Tabela pequena
T = np.array([[3361, 2931, 2411], [19377, 19807, 20327]])
table_tiny = sm.stats.Table(T)
resid_pearson_tiny = table_tiny.resid_pearson
standardized_resids_tiny = table_tiny.standardized_resids

print("Resid Pearson 199 Large File->")
print(resid_pearson_large)
print("Resid Pearson 199 Tiny File->")
print(resid_pearson_tiny)
