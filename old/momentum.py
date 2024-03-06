

   
import momentum_data_QQQ_SPX
import momentum_posis
import pickle
import pandas as pd
import os


def main():
   momentum_data_QQQ_SPX.main()
   momentum_posis.main()
   momentum_data_SOXX.main()
   momentum_posis.main()

if __name__ == "__main__":
   main()


