password = 'a123456'
i = 3 # remaining times
while True:
	pwd = input('Please enter the password: ')
	if pwd == password:
		print('Log in success!')
		break #逃出迴圈
	else:
		i = i - 1
		print('Password is incorrect! Remaining', i,'times')
		if i == 0:
			break