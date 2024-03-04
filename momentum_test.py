

   
import momentum_data_test
import momentum_posis_test
import pickle
import pandas as pd
import os


def main1():
   etfstring = ['BUG']
   momentum_data_test.main(etfstring)
   momentum_posis_test.main(etfstring)

def main2():
   etfstring = ['SPX', 'QQQ']
   momentum_data_test.main(etfstring)
   momentum_posis_test.main(etfstring)

if __name__ == "__main__":
   main1()
   ##main2()



