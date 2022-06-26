import yfinance as yf


def get_factor_adj(column, column_close_adj):
    return column_close_adj / column


def set_price_with_factor_adj(column, factor_adj):
    return column * factor_adj


df = yf.download("PETR4.SA", start="2022-05-01", end="2022-05-31")
df['factor_adj'] = df.apply(lambda x: get_factor_adj(column=x['Close'], column_close_adj=x['Adj Close']), axis=1)

df['Adj Open'] = df.apply(lambda x: set_price_with_factor_adj(column=x['Open'], factor_adj=x['factor_adj']), axis=1)
df['Adj High'] = df.apply(lambda x: set_price_with_factor_adj(column=x['High'], factor_adj=x['factor_adj']), axis=1)
df['Adj Low'] = df.apply(lambda x: set_price_with_factor_adj(column=x['Low'], factor_adj=x['factor_adj']), axis=1)

df = df.drop(columns=['Open', 'High', 'Low', 'Close', 'factor_adj'])
df.rename(columns={'Adj Open': 'Open', 'Adj High': 'High', 'Adj Low': 'Low', 'Adj Close': 'Close'}, inplace=True)
print(df)

