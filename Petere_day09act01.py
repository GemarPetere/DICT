#initialize variable
answer = 'Y'
while answer == 'Y':
	print("a. Add record \n b.View record \n c.Clear all record \n d.Exit :")
	choice = input().upper()
	print("=====================================")

	match choice:
		case 'A':
			print("Input the following user information:")
			username = input("Username: ")
			email = input("Email: ")
			address = input("Address: ")

			f = open("record.txt", "a")

			f.write("{},{},{} \n".format(username,email,address))
			f.close()
		case 'B':
			print("These are the records below:")

			f = open("record.txt","r")
			print(f.read())
		case 'C':
			with open("record.txt", "r+") as f:
				f.truncate(0)
			print("No Record Found!")
		case 'D':
			answer = 'N'
			print("Thank you!")


