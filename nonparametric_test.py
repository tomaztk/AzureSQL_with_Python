import scipy.stats


table = [[13,11],[12,1]]
odds_ratio, p_value=scipy.stats.fisher_exact(table) 
print(p_value)