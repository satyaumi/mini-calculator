print('~~~~~~~mini calculator~~~~~~~~~~~~~~')

num1=int(input("enter the 1st number"))
num2 =int(input('enter 2nd number'))

choice=int(input('enter the chocie betwen 1 to 5'))

if choice==1:
    print('the sum of the two number is',num1+num2)
elif choice==2:
    print('the subtraction of the two number is',num1-num2) 
elif choice==3:
    print('the multiplication of two number is ',num1*num2) 
elif choice==4:
    print('the division of the two number is',num1/num2)

elif choice==5:
    print('the percentile of two number is',num1%num2)
else:
    print('inva.lid input')
