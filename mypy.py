
num1=int(input('enter 1 st num '))
num2=int(input('enter 2 nd num '))

#this functn adds two num
def ad(num1,num2):
    sum=num1+num2
    return sum

#this functn sub two num
def su(num1,num2):
    sub=num1-num2
    return sub

def mul(num1,num2):
    mul=num1*num2
    return mul

def div(num1,num2):
    div=num1/num2
    return div


addi=ad(num1,num2)
subt=su(num1,num2)
muli=mul(num1,num2)
divi=div(num1,num2)

#output to be shown to user
opt=int(input('enter your option: \n1.Add\n2.Sub\n3.Mul\n4.div\nyour option: '))

if opt==1:
    print(f'the sum is {addi} ')
elif opt==2:
    print(f'the sub is {subt}')
elif opt==3:
    print(f'the product id {muli}')    
elif opt==4:
    print(f'the div is {divi}')
else:
    print('enter valid option')
    




