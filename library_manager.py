def manage_library():
    library = []
    wishlist_books = []
    print(f"Welcome to library manger (:\n\n")
    owned_book = input("enter the name of a book you own: ").lower().strip()
    library.append(owned_book)
    
    another_owned_book = input("enter the name of another book you own (or press 'enter' to skip): ").lower()
    if another_owned_book:
        library.append(another_owned_book)
        
    print(f"your library: {library}")
    
    wish_to_own_book = input("enter the name of a book you wish to own in the future: ").lower()
    wishlist_books.append(wish_to_own_book)
    
    another_wish_to_own_book = input("enter the name of another book you wish to own in the future (or press 'enter' to skip): ").lower()
    if another_wish_to_own_book:
        wishlist_books.append(another_wish_to_own_book)
        
    print(f"your wishlist: {wishlist_books}")
    
    already_owned_book = input("enter the name of a book from the wishlist you've acquired (or press 'enter' to skip): ").lower()
    if already_owned_book:
        if already_owned_book in wishlist_books:
            wishlist_books.remove(already_owned_book)
            library.append(already_owned_book)
        else:
            print(f"the book {already_owned_book} isn't in your wishlist!")
            
    print(f"updated library: {library}")
    print(f"updated wishlist: {wishlist_books}")
    
    book_wish_to_donate = input("enter the name of a book from your library you wish to donate(or press 'enter' to skip): ").lower()
    if book_wish_to_donate:
        if book_wish_to_donate in library:
            library.remove(book_wish_to_donate)
        else:
            print(f"the book {book_wish_to_donate} isn't in your library!")
            
    print(f"final library after donations: {library}")

if __name__ == "__main__":
    manage_library()
