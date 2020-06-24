

import hashlib
import ytbeta
import twitteri

#encode string
def encodeSHA512(string):
	hs =  hashlib.sha512()
	hs.update(string.encode("UTF-8"))
	hs = hs.hexdigest()
	return hs

#compare a strig with a hash
def testSHA512(string, hs):
	if encodeSHA512(str(string)) == hs:
		return True
	else:
		return False

#register an user
def regis(login, password):
	login = str(login)
	password = encodeSHA512(str(password))
	file = open("users.txt", 'a')
	file.write("\n"+login+"\n"+password)
	file.close()



print('''
=====================================- Welcome -========================================
	==============================================================================
				
			Note:- Users are local to device only. We are working on it

        				[1]>>> REGISTER
       					[2]>>> LOGIN 
	==============================================================================
========================================================================================  
	''')

op = int(input(">>> "))

if op == 1:
	#Register an user
	userName = input("Username: ")
	passWord = input("Password: ")
	passConf = input("Password: ")
	if passWord == passConf:
		try:
			regis(userName, passWord)
			print("\nSuccess!\n")
            
		except:
			print("\n;-; Fail... Try again\n")

else:
	userName = input("\nUsername: ")+"\n"
	passWord = input("Password: ")
	with open("users.txt", 'r') as users:
		loginAndPass = users.readlines()
		if userName in loginAndPass:
			posi = loginAndPass.index(userName)
			#make the login
			if posi % 2 != 0:
				if testSHA512(passWord, loginAndPass[int(posi)+1].replace('\n', '')):
					print("\nSuccess!\n")
                    
				else:
					print("\nInvalid login or password\n")
			else:
				print("\nInvalid login or password\n")
		else:
			print("\nInvalid login or password\n")





print('Welcome!', userName)

print('''Use Only for Educational porposes
            Author:- ISHAN GARG, DEEP SRESTHI''')

print('''
=====================================================================
   ==============================================================

            
            [1]>>> YOUTUBE
            [2]>>> TWITTER
            


	=============================================================
======================================================================
''')

up = int(input('>>>  '))

if up == 1:
	while True:
		ytbeta.run()
		print('Enter q to quit or c to search again')
		im = input('>> ')
		if im == 'q':
			break

    
if up == 2:
	while True:
		twitteri.runt()
		print('Enter q to quit or c to search again')
		iv = input('>> ')
		if iv == 'q':
			break
		