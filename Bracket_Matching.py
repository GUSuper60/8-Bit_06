#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        arr=[" "]
        for i in s:
            if(i=='(' or i=='{' or i=='['):
                arr.append(i)
            elif(i==')' and arr[-1]=='('):
                arr.pop()
            elif(i=='}' and arr[-1]=="{"):
                arr.pop()
            elif(i==']' and arr[-1]=="["):
                arr.pop()
            else:
                arr.append(i)
        if(len(arr)==1):
            return True
        else:
            return False
