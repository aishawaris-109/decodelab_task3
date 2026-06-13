print("=== Movie Recommendation System ===")

movies = {
    "Action": ["John Wick", "Avengers", "Mission Impossible"],
    "Comedy": ["Mr. Bean", "The Mask", "Home Alone"],
    "Horror": ["The Conjuring", "Insidious", "Annabelle"],
    "Romance": ["Titanic", "The Notebook", "Me Before You"]
}

genre = input("Enter your favorite genre: ").title()

if genre in movies:
    print("\nRecommended Movies:")
    for movie in movies[genre]:
        print("-", movie)
else:
    print("Sorry, no recommendations available.")