# -*- coding: utf-8 -*-
"""Kohler_Assignment3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SYXJFIOr0i4bv1JZOUWZsqNW6ElbnDat
"""

import sys
import csv
import urllib.request
import codecs
from operator import itemgetter
import time
start_time = time.time() 
print("loading URLs...")
url1="https://old.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download"
ftpstream=urllib.request.urlopen(url1)
csvfile1=csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))
    
url2 = "https://old.nasdaq.com/screening/companies-by-industry.aspx?exchange=NYSE&render=download"
ftpstream2 = urllib.request.urlopen(url2)
csvfile2 = csv.reader(codecs.iterdecode(ftpstream2, 'utf-8'))
  
url3 = "https://old.nasdaq.com/screening/companies-by-industry.aspx?exchange=AMEX&render=download"
ftpstream3 = urllib.request.urlopen(url3)
csvfile3 = csv.reader(codecs.iterdecode(ftpstream3, 'utf-8')) 

l = list(csvfile1)[1:] + list(csvfile2)[1:] + list(csvfile3)[1:]

print("Execution time to merge URLs:", time.time()-start_time, "Seconds")

# =================================
# Assignment 3 - Stock Analyzer
# Name: Jonathan Kohler
# ID: 011165333
# =================================

import sys
import csv
import urllib.request
import codecs
from operator import itemgetter
import time
def makeFile():
    filename=input("\nGive this file a name (don't forget file extension)\n")
    f = open(filename, "w")
    writer = csv.writer(f)
    for row in sorted(l, key=itemgetter(0)):
        writer.writerow(row)      
    f.close()
    print('\nfile has been saved to folder as', filename, "\n")
    menu()
  
def findCompany():
    Syms = []  
    Names = []
    LSales = []
    MCaps = []
    ADRs = []
    IPOs = []
    Secs = []
    Inds = []
    SumQs =[]
    for line in l:
        Sym = line[0]
        Name = line[1]
        LSale = line[2]
        MCap = line[3]
        ADR = line[4]
        IPO = line[5]
        Sec = line[6]
        Ind = line[7]
        SumQ = line[8]
        Syms.append(Sym)
        Names.append(Name)
        LSales.append(LSale)
        MCaps.append(MCap)
        ADRs.append(ADR)
        IPOs.append(IPO)
        Secs.append(Sec)
        Inds.append(Ind)
        SumQs.append(SumQ)
    whatCompany = input('\nWhat company are you looking for? (must use symbol name in caps)\n')
    try:
          namdex = Syms.index(whatCompany)
          name = Names[namdex]
          ls = LSales[namdex]
          mc = MCaps[namdex]
          adr = ADRs[namdex]
          ipo = IPOs[namdex]
          sec = Secs[namdex]
          ind = Inds[namdex]
          sumq = SumQs[namdex]
          print('\nInformation about "',whatCompany,'":')
          print('Name:', name)
          print('LastSale:', ls)
          print('MarketCap:', mc)
          print('ADR TSO:', adr)
          print('IPOyear:', ipo)
          print('Sector:', sec)
          print("Industry:", ind)
          print("Summary Quote:", sumq, "\n")
    except ValueError:
          print('\nWrong input, make sure symbol is capitalized')
          print("Try again")
          findCompany()
    menu()
  
def top15():
    count = 0
    print("\nThe top 15 Company Market Caps are:\n")
    print("Rank".ljust(5, ' '), "Symbol".ljust(8, ' '), "Name".ljust(31, ' '),
          "Last Sale".ljust(10, ' '), "Market Cap".ljust(16, ' '), "ADR".ljust(5, ' '),
          "IPO".ljust(5, ' '), "Sector".ljust(20, ' '), "Industry".ljust(50, ' '), "Summary Quote")
    print("-".ljust(194, '-'))
    for line in sorted(l, key=lambda x: float(x[3]), reverse=True)[0:15]: 
        count+=1
        print('{:<2d}'.format(count), ":".ljust(2, ' '), line[0].ljust(8,' '), line[1].ljust(31, ' '),
              line[2].ljust(10, ' '), line[3].ljust(16, ' '), line[4].ljust(5, ' '), line[5].ljust(5, ' '),
              line[6].ljust(20, ' '), line[7].ljust(50, ' '), line[8])
    print("\n")
    menu()
  
def sysexit():
    print ("system exiting...")
    sys.exit(0)
  
def wronginput():
    print("wrong input, please choose a number 1 through 4\n")
    menu() 
  
def menu():
    print("Kohler’s CompanyList Data Analyzer:")
    print("=================================================")
    print("1.	Export to merged/sorted(by stock symbol) CSV file")
    print("2.	Search by stock symbol")
    print("3.	Display 15 companies with the highest MarketCap value")
    print("4.	Exit")
    print("----------------------------------------------\n")
    choice = input("Please choose one of the above:\n")
    while True:
        if choice == '1':
            makeFile()
        if choice == '2':
            findCompany()
        if choice == '3':
            top15()
        if choice == '4':
            sysexit()
            break
        else:
            wronginput()

def main():
    menu()
    if __name__ == "__main__":
        main()

main()