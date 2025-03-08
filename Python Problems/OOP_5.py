
class Train:
    domain = 'Indian Railway'

    def __init__(self, trainNumber, name, seats, fare):
        self.trainNumber = trainNumber
        self.name = name
        self.seats = seats
        self.fare = fare
        self.filename = 'OOP_5_Train_' + trainNumber + '.txt'
        with open(self.filename, 'w') as file:
            file.write(str(seats))
        print (f"Train Number : {self.trainNumber}\tTrain Name : {self.name}\tSeats : {self.seats}\tFare : {self.fare}")

                
    def availableSeats(self, seats, trainNumber):
        self.filename = 'OOP_5_Train_' + trainNumber + '.txt'
        with open(self.filename, 'r') as file:
            data = int(file.read())
        with open(self.filename, 'w') as file:
            if (data < 1):
                Status = "\nSeats not available !!!"
            elif (data < seats):
                Status = f"\nInsufficiant seats available in train !!! Seats available are only {data}"
            else:
                data = data-seats
                Status = "\nTickets are booked successfully !!!"
            file.write(str(data))
        return(Status)

    
    def bookTicket(self,trainNumber, pasName, seats):
        self.trainNumber = trainNumber
        self.name = pasName
        self.seats = seats
        self.checkSeats = self.availableSeats(seats, trainNumber)
        print(self.checkSeats)

########################################################################################################

print("******** Indian Railways ***********\nTrain Details---------\n")
t12122 = Train('12122','Solapur Intercity', 764, 300)
t12144 = Train('12144','Mumbai Express', 1202, 150)


flag = True
while(flag):
    Pname = str(input("\nEnter your name : "))
    PTrainId = str(input("Enter Train number for which you want to book ticket : "))
    Pseat = int(input("How many seats you have to book : "))
  
    if (PTrainId == '12122'):
        t12122.bookTicket(PTrainId, Pname, Pseat)
    elif (PTrainId == '12144'):
        t12144.bookTicket(PTrainId, Pname, Pseat) 
    else:
        print("\nInvalid Train Number !!!")
    
    Wantmore = int(input("\nWant more booking(1 for yes/ 0 for no) : "))
    if (Wantmore == 0):
        flag = False

