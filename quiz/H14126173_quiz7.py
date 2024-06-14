library = {}

def add_book():
    """
    Prompts the user to enter the title, genre, and price of a book separated by vertical bars.
    Adds the book to the library dictionary with the title as the key and the genre and price as the value.
    Prints a message indicating that the book has been added.
    Returns True to indicate that the book was successfully added.
    """

    # your code here
        # Prompt user for input
    user_input = input("Enter the title, genre, and price of the book separated by vertical bars (|): ")

    # Split the input into title, genre, and price
    parts = user_input.split('|')

    # Check if the input is correctly formatted
    if len(parts) != 3:
        print("Invalid input. Please enter the details in the correct format: title | genre | price")
        return False

    title = parts[0].strip()
    genre = parts[1].strip()
    price_str = parts[2].strip()

    # Check if the price can be converted to a float
    if not price_str.replace('.', '', 1).isdigit():
        print("Invalid price. Please enter a numeric value for the price.")
        return False

    price = float(price_str)

    # Add the book to the library dictionary
    library[title] = (genre, price)

    # Print a confirmation message
    print(f"The book '{title}' has been added to the library.")
    
    for title, (genre, price) in library.items():
        print(f"{title}: ({genre}, ${price})")


def remove_book():
    """
    Prompts the user to enter the title of a book to remove.
    Removes the book from the library if it is found and prints a message indicating that the book has been removed.
    If the book is not found, prints an error message and returns False.
    Returns True if the book is successfully removed.
    """
    
    # your code here
    # Prompt user for the title of the book to remove
    title = input("Enter the title of the book to remove: ").strip()

    # Check if the book exists in the library
    if title in library:
        # Remove the book from the library
        del library[title]
        # Print a confirmation message
        print(f"The book '{title}' has been removed from the library.")
        # Return True to indicate success
        return True
    else:
        # Print an error message if the book is not found
        print(f"The book '{title}' was not found in the library.")
        # Return False to indicate failure
        return False

def get_book_info():
    """
    Prompts the user to enter the title of a book to get information about.
    Prints the title, genre, and price of the book if it is found in the library.
    If the book is not found, prints an error message.
    """

    # your code here
    # Prompt user for the title of the book to get information about
    title = input("Enter the title of the book to get information about: ").strip()

    # Check if the book exists in the library
    if title in library:
        genre, price = library[title]
        # Print the book information
        print(f"Title: {title}")
        print(f"Genre: {genre}")
        print(f"Price: ${price:.2f}")
    else:
        # Print an error message if the book is not found
        print(f"The book '{title}' was not found in the library.")

def list_books():
    """
    Lists all books in the library in alphabetical order by title.
    If the library is empty, prints a message indicating that it is empty and returns False.
    Returns True if there are books in the library.
    """
    if not library:
        print("\nThe library is empty.\n")
        return False
    print()
    for title, (genre, price) in sorted(library.items()):
        print("%s (%s, $%.2f)" % (title, genre, price))
    print()
    return True

def list_books_by_genre():
    """
    Prompts the user to enter a genre to search for.
    Lists all books in the library that match the specified genre in alphabetical order by title.
    If no books are found in the specified genre, prints an error message and returns False.
    Returns True if at least one book is found in the specified genre.
    """
    
    # your code here
    # Prompt user for the genre to search for
    genre_to_search = input("Enter the genre to search for: ").strip()

    # Find all books that match the specified genre
    matching_books = [title for title, (genre, price) in library.items() if genre.lower() == genre_to_search.lower()]

    # Check if any books were found
    if matching_books:
        # Sort the matching books by title
        matching_books.sort()
        # Print the list of matching books
        print(f"Books in the genre '{genre_to_search}':")
        for title in matching_books:
            genre, price = library[title]
            print(f"{title} ({genre}, ${price:.2f})")
        # Return True to indicate success
        return True
    else:
        # Print an error message if no books were found
        print(f"No books found in the genre '{genre_to_search}'.")
        # Return False to indicate failure
        return False

while True:
    print("Menu:\n1. Add a book\n2. Remove a book\n3. Get book information\n4. List all books\n5. List books by genre\n6. Quit")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_book_return = add_book()
        if add_book_return:
            list_books()
    elif choice == "2":
        remove_book_return = remove_book()
        if remove_book_return:
            list_books()
    elif choice == "3":
        get_book_info()
    elif choice == "4":
        list_books()
    elif choice == "5":
        list_books_by_genre()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

print("Goodbye!")

