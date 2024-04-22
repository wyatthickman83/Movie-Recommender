#list of movies with their genre, yeaer, and age rating
movies = [
    {"title": "The Shawshank Redemption", "genre": "Drama", "year": 1994, "age_rating": "R"},
    {"title": "The Godfather", "genre": "Crime", "year": 1972, "age_rating": "R"},
    {"title": "The Dark Knight", "genre": "Action", "year": 2008, "age_rating": "PG-13"},
    {"title": "12 Angry Men", "genre": "Drama", "year": 1957, "age_rating": "Not Rated"},
    {"title": "Schindler's List", "genre": "History", "year": 1993, "age_rating": "R"},
    {"title": "Pulp Fiction", "genre": "Crime", "year": 1994, "age_rating": "R"},
    {"title": "The Lord of the Rings: The Return of the King", "genre": "Fantasy", "year": 2003, "age_rating": "PG-13"},
    {"title": "The Avengers", "genre": "Action", "year": 2012, "age_rating": "PG-13"},
    {"title": "Inception", "genre": "Sci-Fi", "year": 2010, "age_rating": "PG-13"},
    {"title": "Forrest Gump", "genre": "Drama", "year": 1994, "age_rating": "PG-13"},
    {"title": "Frozen", "genre": "Animation", "year": 2013, "age_rating": "PG"},
    {"title": "Finding Nemo", "genre": "Animation", "year": 2003, "age_rating": "G"}
]
#asks the user questions
def get_user_preferences():
    print("Welcome to the Movie Recommendation System!")
    preferred_genre = input("What genre of movies do you prefer? ").capitalize()
    min_year = int(input("From what year should the movies be? (e.g., 2000): "))
    max_year = int(input("Until what year should the movies be? (e.g., 2020): "))
    age_rating = input("What age rating do you prefer? (G, PG, PG-13, R): ").upper()
    return preferred_genre, min_year, max_year, age_rating

#filters the database based on the answers
def recommend_movies(preferred_genre, min_year, max_year, age_rating):
    recommended = []
    for movie in movies:
        if (movie['genre'] == preferred_genre and
            min_year <= movie['year'] <= max_year and
            movie['age_rating'] == age_rating):
            recommended.append(movie['title'])
    return recommended

def main():
    genre, min_year, max_year, rating = get_user_preferences()
    recommended = recommend_movies(genre, min_year, max_year, rating)
    if recommended:
        print("\nWe recommend the following movies:")
        for title in recommended:
            print(title)
    else:
        print("\nNo movies found that match your criteria.")

if __name__ == "__main__":
    main()