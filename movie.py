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
ShowRooms = {
    "1": "Name Movie (1)",
    "2": "Name Movie (2)",
    "3": "Name Movie (3)",
    "4": "Name Movie (4)",
    "5": "Name Movie (5)",
}# show_movies() come back and make it go to pick seats when a movie is chosen.
def movie_spots():
    print("See list of Movies (1) \nChoose Movie and Spots (2) \nCheck out (3)")
    choice = int(input("What First? "))
    if choice == 1:
        return movie_list()  
    elif choice == 2:
        return pickseats() 

def movie_list():
    print("Hello")

def pickseats():
        print("Avalible Movies:")
        for room, movie in ShowRooms.items():
            print(movie)
        choice_movie = int(input("What Movie?"))
        if choice_movie == ShowRooms:
            print("Available rows:", list(seats.keys()))
            chosen_row = input("What row? ").upper() # .upper() handles lowercase inputs like 'a'
            while True:
                if chosen_row in seats:
                    print(f"Available seats in Row {chosen_row}: {seats[chosen_row]}")
                    
                    chosen_seat = int(input("What number? "))
                    
                    if chosen_seat in seats[chosen_row]:
                        print(f"Success! You are in Show room {choice_movie} in row {chosen_row}, Seat {chosen_seat}.")
                        seats[chosen_row].remove(chosen_seat) 
                        break
                    else:
                        print("Invalid seat number. That seat doesn't exist or is taken.")

                else:
                    print("Invalid row. Please choose a row from the list.")
                    return pickseats()
        else:
            print("Please Choose a Movie")
movie_spots()

