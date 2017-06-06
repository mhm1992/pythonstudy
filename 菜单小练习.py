def ptcd1():
	#江苏子菜单
	print('+++++++++++++++')
	print('江苏徐州请按1')
	print('江苏苏州请按2')
	print('返回上层请按0')
	print('+++++++++++++++')
	b=int(input('输入 '))
	if b==1:
		print('江苏徐州 ')
	elif b==2:
		print('江苏苏州 ')
	elif b==0:
		ptcd()
	else:
		ptcd1()
def ptcd2():
	#山东子菜单
	print('+++++++++++++++')
	print('山东临沂请按1')
	print('山东济南请按2')
	print('返回上层请按0')
	print('+++++++++++++++')
	c=int(input('输入 '))
	if c==1:
		print('山东临沂 ')
	elif c==2:
		print('山东济南 ')
	elif c==0:
		ptcd()
	else:
		ptcd2()
def ptcd3():
	#浙江子菜单
	print('+++++++++++++++')
	print('浙江杭州请按1')
	print('浙江台州请按2')
	print('返回上层请按0')
	print('+++++++++++++++')
	d=int(input('输入 '))
	if d==1:
		print('浙江杭州 ')
	elif d==2:
		print('浙江台州 ')
	elif d==0:
		ptcd()
	else:
		ptcd3()
	
def ptcd():
	#主菜单
	print('+++++++++++++++')
	print('江苏请按1')
	print('山东请按2')
	print('浙江请按3')
	print('+++++++++++++++')
	a=int(input('输入数字'))
	print('\n'*17)
	if a==1:
		print('进入菜单1江苏 ')
		ptcd1()		
	elif a==2:
		print('进入菜单2山东 ')
		ptcd2()		
	elif a==3:
		print('进入菜单3浙江 ')
		ptcd3()
	else:
		print('输入错误,结束')	

ptcd()
