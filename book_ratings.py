def main():
    book_ratings = {}
    new_book = input("Enter book name:")
    new_rating = input("Enter your rating:")

    add_new_rating(book_ratings, new_book, new_rating)

    print(book_ratings)

def add_new_rating(book_ratings, book, rating):
    book_ratings[book] = rating

main()