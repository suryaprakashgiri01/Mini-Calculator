
# This is a Mini calculator

print()
print('     ------------------------------------------------------------------')
print('     |                  Welcome to the mini calculator                |')
print('     |                                    Code By : SP                |')
print('     ------------------------------------------------------------------')
print()
con = True
while(con):
	print()
	print('Enter the expression as num1 sign num2 :',end=' ')
	exp = input()
	exp_l =  exp.split(' ')
	print()

	if exp_l[1] == '+':
		result = int(exp_l[0]) + int(exp_l[2])
		print(exp+' = '+str(result))
	elif exp_l[1] == '-':
        	result =  int(exp_l[0]) - int(exp_l[2])
        	print(exp+' = '+str(result))
	elif exp_l[1] == '*' or exp_l[1] =='×':
        	result = int(exp_l[0]) * int(exp_l[2])
        	print(exp+' = '+str(result))
	elif exp_l[1] == '/' or exp_l[1] == '÷':
        	result = int(exp_l[0]) / int(exp_l[2])
        	print(exp+' = '+str(result))
	elif exp_l[1] == '%':
        	result = int(exp_l[0]) % int(exp_l[2])
        	print(exp+' = '+str(result))
	elif exp_l[1] == '^':
        	result = int(exp_l[0]) ** int(exp_l[2])
        	print(exp+' = '+str(result))
	else:
		print('Invalid Type of Input')

	print('\nDo you want to continue[y/n] :',end=' ')
	x = input()
	if x=='n' or x=='N':
		print('\nThank you for using...')
		con = False
print()
