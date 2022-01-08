#!/usr/bin/env python3
import string
import random

characters=list(string.ascii_letters + string.digits + string.punctuation)

def generate_password():

	length = int(input("How long should your password be: "))

	random.shuffle(characters)

	password = []

	for i in range(length):
		password.append(random.choice(characters))

	random.shuffle(password)

	print("Here is your password:")
	print("".join(password))

#Invoking the function
generate_password()
