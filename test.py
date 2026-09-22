# Example seat layout: Rows are keys, seats are lists of numbers
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

# Run the function
pickseats()
