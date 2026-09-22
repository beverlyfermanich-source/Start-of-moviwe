# foods = [
#     "pizza", "popcorn", "Candy", "Nachos", "Pretezel", "Chicken Tenders", "Fries"]
# price_food = [13.48, 12.48, 10.48, 10.98, 19.48, 13.48, 9.48]
seats = {
    "Row A": range(1, 10),
    "Row B": range(1, 12),
    "Row C": range(1, 13),
    "Row D": range(1, 11),
    "Row E": range(1, 13),
    "Row F": range(1, 12),
    "Row G": range(1, 13),
    "Row H": range(1, 12),
    "Row I": range(1, 13),
    "Row J": range(1, 12),
    "Row K": range(1, 13),
    "Row L": range(1, 12),
    "Row M": range(4, 13),
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
    row = input("What row?")
    if input == rows in seats:
        
    # prints all rows user chooses one after user chooses one then they choose number
    seat = input(int("What number?"))
def seats_avalible():
    pass

def seats_unavalible():
    pass

# def payment(): (Consider this a challange to do)

