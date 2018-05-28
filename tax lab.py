# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 23:09:58 2017

@author: mustafa
"""

income_input = {"James": 45000, "Mary": 500, "Evan": 70000}
print (income_input)
 
def percentage(number, per):
  return (float(number) * float(per))/100
 
def calculate_tax(income_list):
    if isinstance(income_list, dict):
        result = {};
        for key, value in income_list.items():
            if not isinstance(value, int):
                raise ValueError("Allow only numeric input");
            total_tax = 0;
            # 0- 1000
            value = value - 1000
 
            #
            if value > 1000:
                if value > 9000:
                    total_tax += percentage(9000,10)
                    value = value - 9000
                else:
                    total_tax += percentage(value,10)
                    result[key] = float(total_tax)
                    continue
            else:
                result[key] = total_tax
                continue
                 
            #
            if value > 9000:
                if value > 10200:
                    total_tax += percentage(10200,15)
                    value = value - 10200
            else:
                total_tax += percentage(value,15)
                result[key] = float(total_tax)
                continue
                             
 
            #
            if value > 10200:
                if value > 10550:
                    total_tax += percentage(10550,20)
                    value = value - 10550
            else:
                total_tax += percentage(value,20)
                result[key] = float(total_tax)
                continue
             
            #
            if value > 10550:
                if value > 19250:
                    total_tax += percentage(19250,25)
                    value = value - 19250
            else:
                total_tax += percentage(value,25)
                result[key] = float(total_tax)
                continue
 
            #
            if value > 0:
                total_tax += percentage(value,30)
                result[key] = float(total_tax)
                continue
             
        print (result)
    else:
        raise ValueError("The provided input is not a dictionary.")
                 
calculate_tax(income_input)
