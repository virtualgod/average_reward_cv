import pandas as pd

exp = 1554001706
path = 'Experiments/lambda_cv_prediction/{}/results.csv'.format(exp)
df = pd.read_csv(path)
df_sorted = df.sort_values('rmse')