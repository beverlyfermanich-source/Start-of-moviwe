# foods = [
#     "pizza", "popcorn", "Candy", "Nachos", "Pretezel", "Chicken Tenders", "Fries"]
# price_food = [13.48, 12.48, 10.48, 10.98, 19.48, 13.48, 9.48]
seats = {
    "A":[1, 2, 3, 4, 5],
    "B": [1, 2, 3, 4, 5],
    "C": [1, 2, 3, 4, 5],
    "D": [1, 2, 3, 4, 5],
    "E": [1, 2, 3, 4, 5],
    "F": [1, 2, 3, 4, 5],
    "G": [1, 2, 3, 4, 5],
    "H": [1, 2, 3, 4, 5],
    "I":[1, 2, 3, 4, 5],
    "J": [1, 2, 3, 4, 5],
    "K": [1, 2, 3, 4, 5],
    "L":[1, 2, 3, 4, 5],
    "M": [1, 2, 3, 4, 5],
}

# Had Chat gpt to simplfy the seats using range. (range is the numbers inbetween 1 and whatever the ending numner is)
# for row, seat_numbers in seats.items():
#     print(row, list(seat_numbers))
ShowRooms = {
    "Show Room 1": "Movie 1",
    "Show Room 2": "Movie 2",
    "Show Room 3": "Movie 3",
    "Show Room 4": "Movie 4",
    "Show Room 5": "Movie 1",
}
unavalible = []

def show_movies():
    print("Avalible Movies")
    for room, movie in ShowRooms.items():
        print(room, "->", movie)
# show_movies()

def pickseats():

    print("Here are the Available rows:", list(seats))
    row = input("What Row?").upper() #upper helps with case inputs

    if row in seats:

        def pickseats():
    # 1. Show available rows and get row choice
    print("Available rows:", list(seats.keys()))
    chosen_row = input("What row? ").upper() # .upper() handles lowercase inputs like 'a'
    
    if chosen_row in seats:
        print(f"Available seats in Row {chosen_row}: {seats[chosen_row]}")
        
        chosen_seat = int(input("What number? "))
        
        if chosen_seat in seats[chosen_row]:
            print(f"Success! You booked Row {chosen_row}, Seat {chosen_seat}.")
            seats[chosen_row].remove(chosen_seat) 
        else:
            print("Invalid seat number. That seat doesn't exist or is taken.")
            
    else:
        print("Invalid row. Please choose a row from the list.")
    #     print(f"Avalible seats in {row}: {seats[row]}")
    # chosen_seat = int(input("What number?"))

    # if chosen_seat in seats[row]:
    #     print(f"You have booked {row}, Seat {seat}")
    # row = input("What row?")
    # if input == rows in seats:
        
    # # prints all rows user chooses one after user chooses one then they choose number
    # seat = input(int("What number?"))
# pickseats()
def seats_avalible():
    pass

def seats_unavalible():
    pass

# def payment(): (Consider this a challange to do)

