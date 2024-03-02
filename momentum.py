import momentum_data
import momentum_posis
import pickle
import pandas as pd
import os

def main():
   momentum_data.main()
   momentum_posis.main()

if __name__ == "__main__":
   main()


picklefile = os.path.join(os.getcwd(),'tmp','tickers.pickle')
# Open the pickle file in binary mode
with open(picklefile, "rb") as file:
    # Load the object from the file
    data = pickle.load(file)


##obj = pd.read_pickle(picklefile)
   



