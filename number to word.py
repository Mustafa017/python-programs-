# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 19:57:13 2017

@author: mustafa
"""

 k=int(input())
b = {1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine', \
	10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen', \
     17:'Seventeen',18:'Eighteen',19:'Nineteen',20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', \
     60:'Sixty', 70:'Seventy', 80:'Eighty', 90:'Ninety'}
c = {2:'Twenty',3:'Thirty',4:'Forty',5:'Fifty',6:'Sixty',7:'Seventy',8:'Eighty',9:'Ninety'}

for i in range(k):
        a=input()
        def tens(a):
                if len(a)<=2:
                        if len(a)==1 and int(a[0]) == 0:
                                return ""
                        elif len(a)==1 and int(a[0]) != 0:
                                return b[int(a)]
                        elif len(a)>1 and int(a[0]) == 0 and int(a[1])==0:
                                return ""
                        elif int(a[0])== 0 and int(a[1])>=1:
                                return b[int(a)]
                        elif int(a[0])==1 and int(a[1])<10:
                                return b[int(a)]
                        elif int(a[0])>1 and int(a[1])==0:
                                return b[int(a)]
                        else:
                                return c[int(a[0])]+" "+b[int(a[1])]
        def hundreds(a):
                if len(a)==3:
                        if int(a[0]) == 0:
                                return tens(a[1:])
                        elif tens(a[1:])=="":
                               return tens(a[0])+" Hundred" 
                        else:
                                return tens(a[0])+" Hundred "+tens(a[1:])
        def thousands(a):
                if len(a)==4:
                        if int(a[0]) == 0:
                                return hundreds(a[1:])
                        elif hundreds(a[1:])=="":
                                return tens(a[0])+" Thousand"
                        else:
                                return tens(a[0])+" Thousand "+hundreds(a[1:])
        def tenthousands(a):
                if len(a)==5:
                        if int(a[0]) == 0:
                                return thousands(a[1:])
                        elif hundreds(a[2:])=="":
                                return tens(a[0:2])+" Thousand"
                        else:
                                return tens(a[0:2])+" Thousand "+hundreds(a[2:])
        def hundredthousands(a):
                if len(a)==6:
                        if int(a[0]) == 0:
                                return tenthousands(a[1:])
                        elif hundreds(a[3:])=="":
                                return hundreds(a[0:3])+" Thousand"
                        else:
                                return hundreds(a[0:3])+" Thousand "+hundreds(a[3:])
        def millions(a):
                if len(a)==7:
                        if int(a[0]) == 0:
                                return hundredthousands(a[1:])
                        elif hundredthousands(a[1:])=="":
                                return tens(a[0])+" Million"
                        else:
                                return tens(a[0])+" Million "+hundredthousands(a[1:])
        def tenmillions(a):
                if len(a)==8:
                        if int(a[0]) == 0:
                                return millions(a[1:])
                        elif hundredthousands(a[2:])=="":
                                return tens(a[0:2])+" Million"
                        else:
                                return tens(a[0:2])+" Million "+hundredthousands(a[2:])
        def hundredmillions(a):
                if len(a)==9:
                        if int(a[0]) == 0:
                                return tenmillions(a[1:])
                        elif hundredthousands(a[3:])=="":
                                return hundreds(a[0:3])+" Million"
                        else:
                                return hundreds(a[0:3])+" Million "+hundredthousands(a[3:])
        def billions(a):
                if len(a)==10:
                        if int(a[0]) == 0:
                                return hundredmillions(a[1:])
                        elif hundredmillions(a[1:])=="":
                                return tens(a[0])+" Billion"
                        else:
                                return tens(a[0])+" Billion "+hundredmillions(a[1:])
        def tenbillions(a):
                if len(a)==11:
                        if int(a[0]) == 0:
                                return billions(a[1:])
                        elif hundredmillions(a[2:])=="":
                                return tens(a[0:2])+" Billion"
                        else:
                                return tens(a[0:2])+" Billion "+hundredmillions(a[2:])
        def hundredbillions(a):
                if len(a)==12:
                        if int(a[0]) == 0:
                                return tenbillions(a[1:])
                        elif hundredmillions(a[3:])=="":
                                return hundreds(a[0:3])+" Billion"
                        else:
                                return hundreds(a[0:3])+" Billion "+hundredmillions(a[3:])
        def trillions(a):
                if len(a)==13:
                        if int(a[0]) == 0:
                                return hundredbillions(a[1:])
                        elif hundredbillions(a[1:])=="":
                                return tens(a[0])+" Trillion"
                        else:
                                return tens(a[0])+" Trillion "+hundredbillions(a[1:])

        if len(a)==1 or len(a)==2:
                print (tens(a))
        elif len(a)==3:
                print (hundreds(a))
        elif len(a)==4:
                print (thousands(a))
        elif len(a)==5:
                print (tenthousands(a))
        elif len(a)==6:
                print (hundredthousands(a))
        elif len(a)==7:
                print (millions(a))
        elif len(a)==8:
                print (tenmillions(a))
        elif len(a)==9:
                print (hundredmillions(a))
        elif len(a)==10:
                print (billions(a))
        elif len(a)==11:
                print (tenbillions(a))
        elif len(a)==12:
                print (hundredbillions(a))
        else:
                print (trillions(a))
        