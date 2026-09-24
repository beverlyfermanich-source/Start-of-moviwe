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
    "Show Room 1": "Movie 1",
    "Show Room 2": "Movie 2",
    "Show Room 3": "Movie 3",
    "Show Room 4": "Movie 4",
    "Show Room 5": "Movie 1",
}# show_movies() come back and make it go to pick seats when a movie is chosen.
def movie_spots():
    print("See list of Movies (1) \nChoose Movie and Spots (2) \nCheck out (3)")
    int(input("What First?"))
    if input == 1:
        print(movie_list)
def movie_list():
        print("Hello")
def show_movies():
        print("Avalible Movies:")
        for room, movie in ShowRooms.items():
            print(movie)
        choice_movie = input("What Movie?")

def pickseats():
        print("Available rows:", list(seats.keys()))
        chosen_row = input("What row? ").upper() # .upper() handles lowercase inputs like 'a'
        while True:
            if chosen_row in seats:
                print(f"Available seats in Row {chosen_row}: {seats[chosen_row]}")
                
                chosen_seat = int(input("What number? "))
                
                if chosen_seat in seats[chosen_row]:
                    print(f"Success! You booked Row {chosen_row}, Seat {chosen_seat}.")
                    seats[chosen_row].remove(chosen_seat) 
                    break
                else:
                    print("Invalid seat number. That seat doesn't exist or is taken.")

            else:
                print("Invalid row. Please choose a row from the list.")
                return pickseats()
# movie_spots()
# movie_list()
pickseats()
# show_movies()
