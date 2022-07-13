class Reservation:
	def __init__(self, adult, kids, grandTotal):
		self.adult = adult
		self.kids = kids
		self.grandTotal = grandTotal


class GenerateReport:
	'''def __init__(self,adult, kids, grandTotal):
		super().__init__(adult, kids, grandTotal)'''


	def generateReport(self):
		lines = []
		line = []
		adultTotal = 0
		childTotal = 0
		adultCount = 0
		childCount = 0
		grandTotal = 0

		data = open("record.txt", "r")	
		for x in data.readlines():
			if "#" in x:
				pass
			else:
				lines.append(x)
		
		
		data.close()

		y = 0
		switc_h = True
		while y < len(lines):
			line = lines[y].split()
			adultCount += int(line[4]) 
			childCount += int(line[5]) 

			subtotal = (adultCount*500) + (childCount*300)
			grandTotal += subtotal

			f = open("report.txt","a")
			f.write("\n{} {}".format(lines[y],subtotal))
			f.close()

			adultTotal += adultCount
			childTotal += childCount

			adultCount = 0
			childCount = 0
			y+=1




		summary = open('report.txt','r')
		print(summary.read())
		summary.close()

		print("\n\n")
		print("Total num of Adults: {}".format(adultTotal))
		print("Total number of kids: {}".format(childTotal))
		print("Grand Total:PHP {}".format(grandTotal))

class DeleteReservation:
	def __init__(self,iD):
		self.iD = iD


	def deleteReservation(self):
		i_d = int(self.iD)
		row = ""
		with open("record.txt", "r+") as f:
			row = f.readlines()[i_d]


		with open("record.txt", "r+") as f:
			d = f.readlines()
			f.seek(0)
			for i in d:
				if i not in row:
					f.write(i)
			f.truncate()

		return True




class MakeReservation:
	def __init__(self, name, date, time, adultNum, childrenNum):
		self.name = name
		self.date = date
		self.time = time
		self.adultNum = adultNum
		self.childrenNum = childrenNum

	def postReservation(self):

		try:
			#get the last row first to get the last id and generate id
			id_counter = 0
			lines = []
			with open("record.txt","r") as a:
				lines = a.readlines()[-1]
				print(lines)
			
			if lines[0] == '#':
				id_counter+=1
			else:
				id_counter = int(lines[0])
				id_counter+=1

			#store reservation data
			f = open("record.txt", "a")
			f.write("\n{}  {}  {}  {}  {}  {}".format(id_counter, self.name,self.date,
														self.time,self.adultNum,
														self.childrenNum))
			f.close()
			return True
		except Exception as e:
			return False, e
		




class ViewReservation:
	def getReservation(self):
		f = open('record.txt', 'r')
		return f.read()


def main():
	print("===================== RESTAURANT RESERVATION SYSTEM =================== \n")
	print("System Menu \n a. View all Reservation \n b. Make Reservation \n c. Delete Reservation \n d. Generate Report \n e. Exit")
	option = input("Select Option: ").upper()

	match option:
		case 'A':
			print("\n ====================These are the Records found ================ \n")
			reserv = ViewReservation()
			print(reserv.getReservation())
		case 'B':
			print("\n ==================== Make Reservation ========================== \n")

			name = input("Input Name: ")
			date = input("Input Date: ")
			time = input("Input Time: ")
			adult = input("Number of Adult: ")
			children = input("Number of  Children: ")

			

			postReserv = MakeReservation(name, date, time, adult, children)
			post = postReserv.postReservation()

			if post == True:
				print("\n => Reserved Sucessfully! ")
			else:
				print("\n => Internal Server Error!")
		case 'C':
			print("\n ===================Delete Reservation================= \n")
			iD = input("Input ID to delete Reservation: ")

			delete = DeleteReservation(iD)
			if delete.deleteReservation():
				print("=> Sucessfully Deleted.")
			else:
				print("=> ID Not Found!")
		case 'D':
				print("\n======================= Reservation Report ========================\n")
				generated = GenerateReport()
				generated.generateReport()

			





if __name__ == '__main__':
	main()