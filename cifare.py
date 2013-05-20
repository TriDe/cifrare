import time



def encryptmessage(message,key):
  i = 0
	s = list(message)
	for letter in message:
		if letter != " ":
			ascii_value = ord(letter)
		
			if ascii_value > 64 and ascii_value < 91:
				final_value = ascii_value + key
				
			        """If the alphabet is between (A:Z)"""                                                                  		
				if final_value >= 91:
					while final_value > 26:                  
						final_value = final_value - 90
					final_value = 64 + final_value
					letter = chr(final_value)
					s[i] = letter
				else:
					letter = chr(final_value)
					s[i] = letter
				
				"""If the alphabet is between (a:z)"""
				
			elif ascii_value > 96 and ascii_value < 123:
				final_value = ascii_value + key
				
				if final_value >= 123:
					while final_value > 26:                  
						final_value = final_value - 122
					final_value = 96 + final_value
					letter = chr(final_value)
					s[i] = letter
				else:
					letter = chr(final_value)
					s[i] = letter
				
	 	i = i + 1
	return "".join(s)


def decryptmessage(message,key):
	i = 0
	s = list(message)
	for letter in message:
		if letter != " ":
			ascii_value = ord(letter)
		
			if ascii_value > 64 and ascii_value < 91:
				final_value = ascii_value - key
				
			        """If the alphabet is between (A:Z)"""                                                                  		
				if final_value <= 64:
					while final_value > 26:                  
						final_value = 64 - final_value
					final_value = 90 - final_value
					letter = chr(final_value)
					s[i] = letter
				else:
					letter = chr(final_value)
					s[i] = letter
				
				"""If the alphabet is between (a:z)"""
				
			elif ascii_value > 96 and ascii_value < 123:
				final_value = ascii_value - key
				
				if final_value <= 96:
					while final_value > 26:                  
						final_value = 96 - final_value
					final_value = 122 - final_value
					letter = chr(final_value)
					s[i] = letter
				else:
					letter = chr(final_value)
					s[i] = letter
				
	 	i = i + 1
	return "".join(s)
	
def encryption():
	print 
	print " "*20,
	input_message = raw_input("Enter the message: ")
	print " "*20,
	level = input("Enter the encryption level: ")
	print
	print " "*20,
	print "Encrypted Message: ",
	return encryptmessage(input_message,level)

def decryption():
	print 
	print " "*20,
	input_message = raw_input("Enter the message: ")
	print " "*20,
	level = input("Enter the Decryption level: ")
	print
	print " "*20,
	print "Decrypted Message: ",
	return decryptmessage(input_message,level)
	

def clrscr():
	print "\n" *30
	
"""Doing some styles"""
print " -~"*40
print " " *55,
print "Tri-De cipher (ver 1.0.0.1)"
print " -~"*40
"""ending styles"""

"""---------------Welcome screen----------------"""
print " "*20,
print "Hello,welcome to Tri-De cipher"
"----------------End of WS ---------------------"""

user_continue = "y"       
while user_continue != "N" and user_continue != "n":
	
	time.sleep(1)
	clrscr()
	
	"""--------Style----------------------------"""
	print " -~"*50
	print " " *55,
	print "Tri-De cipher (ver 1.0.0.1)"
	print " -~"*50
	"""---------EO Style-----------------------"""
	
	"""-----------Menu screen ----------------------"""
	print "\n"*2
	print " "*20,
	print " 1.Encrypt your string "
	print "\n"
	print " "*20,
	print " 2.Decrypt your string"
	print "\n"
	print " "*20,
	print " (hit ctrl-c for exit)"
	"""---------End of MS -------------------------"""

	print 
	print " "*10,
	choice = raw_input("Select a choice: ")
	
	if choice == "1":
		print
		print " "*20,
		print " Encryption"
		print " "*20,
		print encryption() 
		print
	elif choice == "2":
		print
		print " "*20,
		print " Decryption"
		print 
		print " "*20,
		print decryption() 
		print
		
	print "\n"*2
	print " "*20,
	user_continue = raw_input("Do you want to continue using Tri-De cipher ? (Y/n)")
	print

print "\n"*2
print " "*20,
print "Thanks for using Tri-De cipher . Se u"





