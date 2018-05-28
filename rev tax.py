# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 10:47:53 2017

@author: mustafa
"""

income_input = {"Alex":500, "James":9050}
print(income_input)

def percent(number,percentage):
    return (float(number*percentage))/100

def calculate_tax(income_list):
    if isinstance(income_list, dict):
        result = {}
        for key, value in income_list.items():
            if not isinstance(value, int):
                raise ValueError("The input should be Numbers Only")
                
                total_tax = 0
                value = value - 1000
                
                if value > 1000:
                    if value > 9000:
                        total_tax += percent(9000,10)
                        value = value - 9000
                        continue
                    else:
                        total_tax += percent(value,10)
                        result[key] = float(total_tax)
                        continue
                else:
                    result[key] = total_tax
            
        print(result)
    else:
        raise ValueError("The argument should be a dictionary")

calculate_tax(income_input)