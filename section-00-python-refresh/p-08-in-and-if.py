movies_watched = {"The Matrix", "Inception", "Interstellar", "The Dark Knight"}
user_movie = input("Enter a movie name: ")

if user_movie in movies_watched:
    print(f"I've wathced {user_movie} too!")
else:
    print("I haven't watched that movie yet.")
