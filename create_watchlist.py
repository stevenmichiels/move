import os
import pandas as pd

# read /holdings/holdings_all.csv
holdings_all = os.path.join(os.path.dirname(__file__), 'holdings', 'holdings_all.csv')
holdings_all_df = pd.read_csv(holdings_all)
# tale holdings_all_df.Symbol and write them comma-separated to /holdings/holdings_all_symbols.txt
holdings_all_symbols = os.path.join(os.path.dirname(__file__), 'holdings', 'holdings_all_symbols.txt')


test = [num for num in holdings_all_df[(holdings_all_df.Weighting=='XLY')]['Symbol']]

test = [num for num in holdings_all_df[(holdings_all_df.Weighting=='SLX') |  (holdings_all_df.Weighting=='SLX')]['Symbol']]


# join with ','
test = ','.join(test)
# write test to 'holdings_all_symbols.txt')
with open(holdings_all_symbols, 'w') as f:
    f.write(test)
    f.close()

