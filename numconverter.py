import pandas as pd

def conversion(series):
	series = series.str.replace(',', '.')
	series = series.astype('float', copy=False)
	return series


df = pd.read_csv('2017small.csv')
df['Ultimo'] = conversion(df['Ultimo'])
df['Apertura'] = conversion(df['Apertura'])
df['Massimo'] = conversion(df['Massimo'])
df['Minimo'] = conversion(df['Minimo'])
df['Var. %'] = conversion(df['Var. %'])

df[['Ultimo','Apertura','Massimo','Minimo','Var. %']].to_csv('2017small-numbers.csv', header=False, index=False)