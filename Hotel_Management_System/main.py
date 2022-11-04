from colorama import Fore  # gives colour to your context
import array as arr


history = []  # list which includes rooms that are currently booked
book_log = []  # list which contains all transactions
rooms = arr.array('i', [101, 102, 103, 104, 105, 201, 202, 203, 204, 205, 301, 302, 303, 304, 305, 401, 402, 403, 404,
                        405, 501, 502, 503, 504, 505]) # available rooms are in array, while booked are in LL


class Node:  # node class declared
    def __init__(self, data):  # constructor
        self.__data = data  # data and next declared private members
        self.__next = None

    def get_data(self):  # returns data part of node
        return self.__data

    def set_data(self, data):  # sets value for data part of node
        self.__data = data

    def get_next(self):  # returns next part of node
        return self.__next

    def set_next(self, next_node):  # sets value of next part of node
        self.__next = next_node


class LinkedList:  # Declared linked list class
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):  # returns head node
        return self.__head

    def get_tail(self):  # returns tail node
        return self.__tail

    def add(self, data):  # create&insert node at end
        new_node = Node(data)  #calls Node class, and passes data
        if(self.__head is None):  # LL is empty
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)  # calls next part of tail node to set its value
            self.__tail = new_node

    def display(self):  # displays LL
        temp = self.__head
        while(temp is not None):
            print(temp.get_data())
            temp = temp.get_next()  # points to next node

    def find_node(self, data):  # Search for particular node using data part
        temp = self.__head
        while(temp is not None):
            if(temp.get_data() == data):
                return temp  # returns temp node
            temp = temp.get_next()
        return None

    def delete(self, data):  # delete node
        node = self.find_node(data)  # value of node depends on return value of find_node
        if(node is not None):  #if temp node is returned from find_node
            if(node == self.__head):
                if(self.__head == self.__tail):  # i.e. LL has only one node
                    self.__tail = None
                self.__head = node.get_next()  # value of head set to next node
            else:
                temp = self.__head  # new pointer declared pointing to head node
                while(temp is not None):
                    if(temp.get_next() == node):  # if next part of node is equal to given data
                        temp.set_next(node.get_next())  # set value of next part of temp equal to the node after given data
                        if(node == self.__tail):
                            self.__tail = temp  # tail is set to node before itself
                        node.set_next(None)  #  detach the node to be deleted
                        break
                    temp = temp.get_next()
        else:
            print(Fore.RED, data, "Sorry, but this room is either available or invalid number.")


customer = LinkedList()  # object of LinkedList class declared as customer


def search_arr(room_no):  # linear search in array
    for i in range(len(rooms)):
        if rooms[i] == room_no:
            return 1
    return -1


def sort_arr():  # bubble sort the array
    for i in range(0, len(rooms)):
        for j in range(i+1, len(rooms)):
            if rooms[i] > rooms[j]:
                temp = rooms[j]
                rooms[j] = rooms[i]
                rooms[i] = temp


def book_room():  # book a room
    while True:  # infinity loop declared
        room_no = input(Fore.LIGHTYELLOW_EX + 'Enter room number you want to book: ')  # text has light yellow color
        try:  # used to avoid any kind of error
            room_no = int(room_no)  # tries converting data type of room_no from string to integer
        except:  # if try fails except is run
            print('{0}Invalid room number!'.format(Fore.RED))
            continue  # next loop runs without running further commands of current loop

        return_val = search_arr(room_no)  # depending on this value further commands executed
        if return_val == 1:  # if room is available
            rooms.remove(room_no)  # removes from array
            customer.add(room_no)  # room number added to linked list
            return room_no
        elif return_val == -1:  # if room is not available
            val = customer.find_node(room_no)  # used to check whether room is occupied or is an invalid number
            if val == room_no:
                print(Fore.RED + 'Room unavailable!')
            else:
                print("Invalid room number! The available rooms are: ")
                for i in rooms:
                    print(i)


def name():  # for taking name of customer
    f_name = input(Fore.LIGHTYELLOW_EX + 'First name: ')  # text is printed in light yellow
    s_name = input(Fore.LIGHTYELLOW_EX + 'Surname: ')
    full_name = f_name + ' ' + s_name  # concatenation
    return full_name


def phone_num():  # for taking phone number of customer
    while True:
        phone_no = input(Fore.LIGHTYELLOW_EX + 'Phone number: ')
        try:
            phone_no = int(phone_no)  # tries converting data type of phone_no from string to integer
        except:  # runs if try fails
            print(Fore.RED + "Invalid number, please enter numeric values!")
            continue

        if len(str(phone_no)) != 10:  # if length of phone number is not 10 digits long
            print(Fore.RED + "Number must have 10 digits!")
        else:
            return phone_no


def occupy():  # takes no. of days room should be booked
    while True:
        time = input(Fore.LIGHTYELLOW_EX + "Enter no. of days: ")
        try:
            time = int(time)
        except:
            print(Fore.RED + "Enter numeric value only.")
        return time


def customer_details():  # compilation of all data provided by customer
    if len(rooms) == 0:  # if array is empty i.e. all rooms are booked
        print(Fore.LIGHTGREEN_EX + "Sorry, booking is full!")
        return -1  # return statement used to avoid execution of further commands
    print(Fore.LIGHTYELLOW_EX + "Please enter the following details:\n")
    customer_name = name()  # has values returned by the functiom
    number = phone_num()
    room = book_room()
    time = occupy()
    bill = 3000*time + 500  # bill calculated

    details = {'name': customer_name, 'Number': number, 'Room_no': room, 'Time': time, 'Bill': bill, 'Status': 'Booked'}  # detail dictionary created
    print(Fore.CYAN, '\n', "Name: ", details['name'], Fore.LIGHTWHITE_EX, "\nPhone number: ",
          details['Number'], "\nRoom no.: ", details['Room_no'], "\nNo. of days: ", details['Time'], Fore.LIGHTGREEN_EX,
          "\nStatus: ", details['Status'], "\nBill: ", details['Bill'])  # details dictionary printed
    history.append(details)  # append dictionary to history list
    book_log.append(details)  # append dictionary to book_log


def cancel_booking():  # to cancel booking
    name = input(Fore.LIGHTCYAN_EX + "Enter your name: ")
    room_no = int(input("Enter room no.: "))
    for i in range(len(history)):  # loop has range from 0 to the no. of elements in history, 1 dictionary = 1 element
        if history[i]['name'] == name:  # access name of customer and compares with input given by user
            customer.delete(room_no)  # deletes node from LL
            rooms.append(room_no)  # appends to array
            del history[i]  # deletes the given element of history
            sort_arr()
            book_log[i]['Status'] = 'Cancelled'  # set value of status equal to cancelled
            book_log[i]['Bill'] = '500'  # set billing to Rs.500
            while True:  # for payment
                pay = input(Fore.LIGHTGREEN_EX + "Please pay the booking amount (Rs. 500): ")
                if pay == '500':
                    print("Payment successful! You have cancelled your booking.")
                    break
                else:
                    print(Fore.RED + "Invalid amount!")


def check_out():  # for checking out, everything is same as cancel_booking function
    name = input("Enter your name: ")
    room_no = int(input("Enter room no.: "))
    for i in range(len(history)):
        if history[i]['name'] == name:
            customer.delete(room_no)
            rooms.append(room_no)
            del history[i]
            sort_arr()
            book_log[i]['Status'] = 'Checked out'
            while True:
                pay = input(Fore.LIGHTGREEN_EX + "Please pay your rent: ")
                pay = int(pay)
                amount = book_log[i]["Bill"]
                if pay == amount:
                    print("Payment successful! You have checked out.")
                    break
                else:
                    print(Fore.RED + "Invalid amount!")


def print_details(name):  # print history or book_log according to the list passed
    for index, log in enumerate(name):  # enumerate allows access to elements of the dictionary in the list
        print(Fore.CYAN, '\n', index + 1, "Name: ", log['name'], Fore.LIGHTWHITE_EX, "\nPhone number: ",
              log['Number'], "\nRoom no.: ", log['Room_no'], "\nNo. of days: ", log['Time'], Fore.LIGHTGREEN_EX,
              "\nStatus: ", log['Status'], "\nBill: ", log['Bill'])  # print the list
    if len(name) == 0 :  # if list is empty
        print(Fore.CYAN + "No rooms booked!")


print(Fore.MAGENTA + "Welcome to our Hotel!!")  # prints text in magenta colour


while True:  # infinty loop,
    print(Fore.LIGHTMAGENTA_EX + "\n\n1. See available rooms\n2. See Pricing\n3. Book rooms\n4. Cancel booking \n"
                                 "5. Booked rooms' detail\n6. Check out\n7. See log\n8. Exit\n")
    choice = (input("Enter your option: "))

    try:  # used to avoid error in program
        choice = int(choice)  # tries converting data type of choice input fron string to integer
    except:  # executed if try fails
        print(Fore.RED + "Invalid input!")

    if choice == 1:  # displays available rooms
        for i in rooms:
            print(Fore.LIGHTGREEN_EX, i)

    if choice == 2:  # displays pricing details
        print(Fore.LIGHTBLUE_EX + "Each room has maximum accommodation of 4 people.")
        print("Rs.3000 per room for 1 day.")
        print("Booking amount is Rs.500.")

    if choice == 3:  # customer details taken by executing customer_detail function
        customer_details()

    if choice == 4:  # booking cancelled using cancel_booking function
        cancel_booking()
        
    if choice == 5:  # display rooms occupied
        print(Fore.LIGHTBLUE_EX + "Booked rooms: ")
        customer.display()  # displays LL which contains room numbers of those occupied
        print_details(history)  # history list displayed

    if choice == 6:  # check out using check_out function
        check_out()

    if choice == 7:  # displays all bookings carried out till now
        print_details(book_log)  # displays book_log list

    if choice == 8:  # exit hotel
        print(Fore.LIGHTCYAN_EX + "Thank you for visiting!")
        break  # while loop breaks
