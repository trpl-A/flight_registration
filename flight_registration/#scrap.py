
import time 
import os 
import colorama
from colorama import Fore, Back
colorama.init()

# my modules
from utilities import writer

# =========================


def all_seats():
    # alpha = "abcdefghijklmnopqrstuvwxyz"
    # alphaList = list(alpha)
    alphaList = "abcdefghijklm"


    # readind and displaying the occupied seats
    show_occ_seats = open("occupied_seats.txt", "r")
    seats = show_occ_seats.readlines()

    all_seats.occupied = []
    occupied = all_seats.occupied
    for s in seats:
        ss = s.strip("\n")
        occupied.append(ss)
        print(ss)


    # seat notations and omitting occupied seats from being displayed
    all_seats.seatList = []
    seatList = all_seats.seatList

    print(f"\n{Back.YELLOW + Fore.BLACK} Seat layout {Back.RESET + Fore.RESET}\n")
    time.sleep(1)

    for a in reversed(alphaList):
        for b in range(1, 11):
            # for occupied
            seat_notation = a + str(b)
            if seat_notation not in occupied:
                seatList.append(seat_notation)
                print(seat_notation, end=" ")

            else:
                # print(" ", end="")
                print(f"{Fore.RED}{seat_notation}{Fore.RESET}", end=" ")

        print("\n")
        time.sleep(0.25)

    # print(seatList)


    # additional info
    print("- The text in red indicate the occupied seats")
    print("- Row 'a' is the first row in the plane")
    print("- The first column and last columns are at the windows of the airplane")
    print()

# end of function =============================================
# all_seats()



def seat_selection():
    seat_selection.seat = input(f"\nPlease select a seat: {Fore.YELLOW}")
    
    confirm = input(f"{Fore.RESET}Are you sure? (y/n) ").lower()

    c = False 
    while c == False:
        if confirm == "y":
            c = True 

        else:
            seat_selection.seat = input(f"\nPlease select a seat: {Fore.YELLOW}")
            confirm = input(f"{Fore.RESET}Are you sure? (y/n) ").lower() 

# end of function ===========================================
# seat_selection()




def seat_reg():
    
    # displaying all seats
    all_seats()


    # selecting a seat
    seat_selection()

    seat_reg.seat = seat_selection.seat 
    seat = seat_reg.seat

    occupied = all_seats.occupied

    while seat not in all_seats.seatList or seat in occupied:
        if seat not in all_seats.seatList:
            print(f"{Fore.RED}invalid response{Fore.RESET}")
            seat = input(f"\nPlease select a seat: {Fore.YELLOW}")
        
        elif seat in occupied:
            print(f"{Fore.RED}that seat is occupied{Fore.RESET}")
            seat = input(f"\nPlease select a seat: {Fore.YELLOW}")


    # writing to text file (occupied seats)
    o = open("occupied_seats.txt", "a")
    o.write("\n")
    o.write(seat)

    writer(f"{Fore.RESET}\nYour seat has been reserved")
    time.sleep(1.5)

# end of function ===========================================
# seat_reg()



# main function 
def ticket():

    # selection a seat
    seat_reg()
    os.system("cls")


    # personal info
    name = input(f"{Fore.RESET}\n\nEnter your name: ").capitalize()

    surname = input(f"{Fore.RESET}\nEnter your surname: ").capitalize()
    
    age = input("\nEnter your age: ")

    cell_nr = input(f"{Fore.RESET}\nEnter your cellphone number: ").capitalize()

    date_of_booking = time.asctime()

    price = "R20000"

    location = "FROM Cape Town International Airport TO London Internation Airport"

    estimated_flight_duration = "4 hours"

    departure = "Sun 20 Dec 2022 14:00"

    flight_nr = "flight_251122_Lon_CT_2012222" 
    # Eg. flight number based on date of reservation/booking, destination Town/city, starting town/city, date of flight
    # from 25/11/22, London, Cape Town, 20/12/22; ticket = flight_251122_Lon_CT_2012222

    ticket_id = "flight_251122_Lon_CT_2012222_pass167" 
    # a seemingly random string of numbers and letters. Dates, Day, Fight Class, other flight-meta data, etc...


    # used to create the name of the text file
    seat = seat_selection.seat 


    # end message
    writer(f"\n{Fore.YELLOW}Information recorded")
    time.sleep(1)

    # saving ticket
    ticket = open(f"tickets/{seat}.txt", "w")

    ticket.write(f"\nDate of registration: {date_of_booking}\n")
    ticket.write(f"Date and time of departure: {departure}\n")
    ticket.write(f"Route: {location}\n")
    ticket.write(f"Flight nr: {flight_nr}\n")
    ticket.write(f"Ticket ID: {ticket_id}\n\n")

    ticket.write(f"Name: {name}\n")
    ticket.write(f"Surname: {surname}\n")
    ticket.write(f"Age: {age}\n")
    ticket.write(f"Cellphone nr: {cell_nr}\n")
    ticket.write(f"Price: {price}\n")
    ticket.write(f"Estimated flight duration: {estimated_flight_duration}\n")
    ticket.write(f"Seat: {seat}\n")


    # writing to text file (patrons)
    f = open('patronSeating.txt', 'a')
    f.write(f"\nname: {name}_{surname}_{age} \nseat number: {seat} \n")

# end of function ===========================================
ticket()



# def main():

#     ticket()

#     seat_reg()

# end of function ===========================================


# <<< end >>>  