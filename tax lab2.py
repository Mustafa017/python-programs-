# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:06:48 2017

@author: mustafa
"""
earnings = {"James":20500, "Mary":500, "Evan":70000}

def tax_calculator(start,stop,percentage):
    tax_bracket = stop - start
    return tax_bracket* float(percentage/100)  

def calculate_tax(income):
    if not isinstance(income,dict):
        raise ValueError("The provided input is not a dictionary.")
    else:
        result = {}
        for key,value in income.items():
            if not isinstance(value, int):
                raise ValueError("Allow only numeric input")
            else:
                total_tax = 0
                
                if value > 1000 :
                    if value > 10000:
                        total_tax += tax_calculator(1000,10000,10)
                else:
                    total_tax += total_tax
                    result[key] = float(total_tax)
                    continue
                
                if value > 10000 :
                    if value > 20200:
                        total_tax += tax_calculator(10000,20200,15)
                else:
                    total_tax += tax_calculator(1000,value,10)
                    result[key] = float(total_tax)
                    continue
                    
                if value > 20200:        
                    if value > 30750:
                        total_tax += tax_calculator(20200,30750,20)         
                else:
                    total_tax += tax_calculator(10000,value,15)
                    result[key] = float(total_tax)
                    continue
                
                if value > 30750:        
                    if value > 50000:
                        total_tax += tax_calculator(30750,50000,25)
                        
                else:
                    total_tax += tax_calculator(20200,value,20)
                    result[key] = float(total_tax)
                    continue
                            
                if value > 50000:
                    total_tax += tax_calculator(50000,value,30)
                    result[key] = float(total_tax)
                else:
                    total_tax += tax_calculator(30750,value,25)
                    result[key] = float(total_tax)          
        print(result)
    print(income)
        
calculate_tax(earnings)