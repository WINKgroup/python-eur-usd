import pandas as pd

def conversion(series):
	series = series.str.replace(',', '.')
	series = series.str.replace('%', '')
	series = series.astype('float', copy=False)
	return series

df = pd.read_csv('2001-2019.csv', index_col=0, infer_datetime_format=True)
df['Ultimo'] = conversion(df['Ultimo'])
df['Apertura'] = conversion(df['Apertura'])
df['Massimo'] = conversion(df['Massimo'])
df['Minimo'] = conversion(df['Minimo'])
df['Var. %'] = conversion(df['Var. %'])
df.index = pd.to_datetime(df.index, format='%d.%m.%Y')

weekly = df['Ultimo'].resample('W').mean()
monthly = df['Ultimo'].resample('M').mean()
yearly = df['Ultimo'].resample('A').mean()

monthlyInterpolated = yearly.resample('M').interpolate('linear')
diff = monthly - monthlyInterpolated
diff = diff.dropna()
diff.std()