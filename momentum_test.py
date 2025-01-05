

   
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

def main3():
   etfstring = ['SOXX']
   momentum_data_test.main(etfstring)
   momentum_posis_test.main(etfstring)

def main4():
   etfstring = ['IGV']
   momentum_data_test.main(etfstring)
   momentum_posis_test.main(etfstring)

def main5():
   etfstring = ['WCLD']
   momentum_data_test.main(etfstring)
   momentum_posis_test.main(etfstring)

def main6():
   etfstring = [ 'XLE']
   momentum_data_test.main(etfstring)
   momentum_posis_test.main(etfstring)
   

def main7():
   etfstring = ['SP400']
   momentum_data_test.main(etfstring)
   momentum_posis_test.main(etfstring)
   
if __name__ == "__main__":
   main1()
   main2()
   main3()
   main4()
   #main5()
   main6()
   main7()



