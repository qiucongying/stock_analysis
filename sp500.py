import pandas as pd

companies_data = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
table = companies_data[0]
table.head()
