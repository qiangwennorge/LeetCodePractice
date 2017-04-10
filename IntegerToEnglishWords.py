# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 22:22:52 2017

@author: qiangwennorge
"""

'''
 Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,

123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
'''

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        result = ''
        numstr = str(num)
        if num < 1000:
            result += self.hundredfunc(numstr)
        elif num < 1000000:
            numstrright = numstr[-3:]
            numstrleft = numstr[:-3]
            result += self.hundredfunc(numstrright)
            result = ' Thousand ' + result
            result = self.hundredfunc(numstrleft) + result
        elif num < 1000000000:
            numstrright = numstr[-3:]
            numstrmiddle = numstr[-6:-3]
            numstrleft = numstr[:-6]
            if int(numstrright) == 0:
                result = ''
            else:
                result += self.hundredfunc(numstrright)
                
            if int(numstrmiddle) == 0:
                result = '' + result
            else:
                result = ' Thousand ' + result
                result = self.hundredfunc(numstrmiddle) + result
            result = ' Million ' + result
            result = self.hundredfunc(numstrleft) + result
        elif num < 1000000000000:
            numstrright = numstr[-3:]
            numstrmiddle = numstr[-6:-3]
            numstrleftmiddle = numstr[-9:-6]
            numstrleft = numstr[:-9]
            if int(numstrright) == 0:
                result = ''
            else:
                result += self.hundredfunc(numstrright)
                
            if int(numstrmiddle) == 0:
                result = '' + result
            else:
                result = ' Thousand ' + result
                result = self.hundredfunc(numstrmiddle) + result
                
            if int(numstrleftmiddle) == 0:
                result = '' + result
            else:                              
                result = ' Million ' + result
                result = self.hundredfunc(numstrleftmiddle) + result
            result = ' Billion ' + result
            result = self.hundredfunc(numstrleft) + result
            
        return result.strip()
            
    def hundredfunc(self,inputstr):
        englishdict = {0:'',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen',20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninety'}
        if int(inputstr) in englishdict:
            result = englishdict[int(inputstr)] 
        elif int(inputstr) < 100 and int(inputstr) > 20:
            result = englishdict[int(inputstr[-2] + '0')] + ' ' + englishdict[int(inputstr[-1])]
        elif int(inputstr) < 1000 and int(inputstr[-2:]) > 20:
            result = englishdict[int(inputstr[-3])] + ' Hundred ' + englishdict[int(inputstr[-2] + '0')] + ' ' + englishdict[int(inputstr[-1])]
        elif int(inputstr) < 1000 and int(inputstr[-2:]) <= 20:
            result = englishdict[int(inputstr[-3])] + ' Hundred ' + englishdict[int(inputstr[-2:])]
        return result.strip()    
    
        
f = Solution()
print f.numberToWords(10231090)        