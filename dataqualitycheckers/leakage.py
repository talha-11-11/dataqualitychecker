def check_data_leakage(df, target, threshold=0.95):
    correlations = df.corr()[target].drop(target)
    return correlations[abs(correlations) > threshold]
