def isoperator(n):
    if( (n=='+') or( n=='-') or (n=='*') or (n=='/')):
        return True
    
    return False
def posttopre(exp):
    s=[]
    for i in range(0,len(exp)):
        if(isoperator(exp[i])):
            op1=s[-1]
            s.pop()
            op2=s[-1]
            s.pop()
            n=exp[i]+op2+op1
            s.append(n)
        else:
            s.append(exp[i])
           
    string=""
    for i in s:
      string+=i
      return string
       
exp="AB+CD-*"
print(posttopre(exp))