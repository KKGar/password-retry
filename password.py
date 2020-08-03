password = 'a123456'
i = 3 # remaining times
while i > 0:
	pwd = input('Please enter the password: ')
	if pwd == password:
		print('Log in success!')
		break #逃出迴圈
	else:
		i = i - 1
		print('Password is incorrect! Remaining', i,'times')
		