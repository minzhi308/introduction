def read_csv(file_path):
    """
    Reads the CSV file manually and returns the header and data rows separately.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            header = lines[0].strip().split(',')
            data = [line.strip().split(',') for line in lines[1:]]
        return header, data
    except Exception as e:
        print(f"Error reading file: {e}")
        return [], []

#1
def top_3_movies_highest_ratings_2016(file_path):
    """
    Finds and prints the top-3 movies with the highest ratings in 2016.
    """
    # Find the index of necessary columns
    try:
        year_idx = header.index("Year")
        rating_idx = header.index("Rating")
        title_idx = header.index("Title")
    except ValueError as e:
        print(f"Column not found: {e}")
        return
    
    # Filter movies released in 2016
    movies_2016 = [row for row in data if row[year_idx] == '2016']
    
    if not movies_2016:
        print("No movies found for the year 2016.")
        return
    
    # Sort movies by rating in descending order
    try:
        movies_2016_sorted = sorted(movies_2016, key=lambda x: float(x[rating_idx]), reverse=True)
    except ValueError as e:
        print(f"Error converting rating to float: {e}")
        return
    
    # Get top-3 movies
    top_3_movies = movies_2016_sorted[:3]
    
    # Print the results
    print("#1")
    for i, movie in enumerate(top_3_movies, 1):
        print(f"Top-{i} Movie: {movie[title_idx]} with Rating: {movie[rating_idx]}")
    print()

#2
def most_prolific_director(file_path):
    """
    Finds and prints the director who has been involved in the most movies.
    """
    # Find the index of the 'Director' column
    try:
        director_idx = header.index("Director")
    except ValueError as e:
        print(f"Column not found: {e}")
        return
    
    # Count the number of movies each director has directed
    director_count = {}
    for row in data:
        directors = row[director_idx].split(', ')
        for director in directors:
            if director in director_count:
                director_count[director] += 1
            else:
                director_count[director] = 1
    
    # Find the director with the maximum count
    most_movies_director = max(director_count, key=director_count.get)
    most_movies_count = director_count[most_movies_director]
    
    # Print the result
    print(f"#2\nThe director involved in the most movies is {most_movies_director} with {most_movies_count} movies.\n")

#3
def actor_highest_total_revenue(file_path):
    """
    Finds and prints the actor generating the highest total revenue.
    """
    # Find the index of the necessary columns
    try:
        revenue_idx = header.index("Revenue (Millions)")
        actors_idx = header.index("Actors")
    except ValueError as e:
        print(f"Column not found: {e}")
        return
    
    # Calculate total revenue for each actor
    actor_revenue = {}
    for row in data:
        revenue_str = row[revenue_idx]
        if revenue_str:
            try:
                revenue = float(revenue_str)
            except ValueError:
                continue
            actors = row[actors_idx].split('| ')
            for actor in actors:
                if actor in actor_revenue:
                    actor_revenue[actor] += revenue
                else:
                    actor_revenue[actor] = revenue
    
    # Find the actor with the highest total revenue
    highest_revenue_actor = max(actor_revenue, key=actor_revenue.get)
    highest_revenue = actor_revenue[highest_revenue_actor]
    
    # Print the result
    print(f"#3\nThe actor generating the highest total revenue is {highest_revenue_actor} with a total revenue of ${highest_revenue:.2f} million.\n")

#4
def average_rating_emma_watson(file_path):
    """
    Calculates and prints the average rating of Emma Watson's movies.
    """
    # Find the index of necessary columns
    try:
        actors_idx = header.index("Actors")
        rating_idx = header.index("Rating")
    except ValueError as e:
        print(f"Column not found: {e}")
        return

    # Filter movies with Emma Watson and calculate the average rating
    total_rating = 0
    count = 0

    for row in data:
        actors = row[actors_idx].split('| ')
        if "Emma Watson" in actors:
            try:
                rating = float(row[rating_idx])
                total_rating += rating
                count += 1
            except ValueError:
                print(f"Invalid rating value: {row[rating_idx]}")
                continue
    
    if count == 0:
        print("No movies found with Emma Watson.")
        return
    
    average_rating = total_rating / count
    print(f"#4\nThe average rating of Emma Watson's movies is {average_rating:.2f}\n")

#5
def top_4_actors_most_movies(file_path):
    """
    Finds and prints the top-4 actors playing the most movies.
    """
    # Find the index of the 'Actors' column
    try:
        actors_idx = header.index("Actors")
    except ValueError as e:
        print(f"Column not found: {e}")
        return
    
    # Count the number of movies each actor has acted in
    actor_count = {}
    for row in data:
        actors = row[actors_idx].split('| ')
        for actor in actors:
            if actor in actor_count:
                actor_count[actor] += 1
            else:
                actor_count[actor] = 1
    
    # Find the top-4 actors with the maximum count
    top_4_actors = sorted(actor_count.items(), key=lambda x: x[1], reverse=True)[:4]
    
    # Print the result
    print("#5")
    for i, (actor, count) in enumerate(top_4_actors, 1):
        print(f"Top-{i} Actor: {actor} with {count} movies")
    print()

#6
def top_7_collaboration_pairs(file_path):
    """
    Finds and prints the top-7 frequent collaboration pairs of director and actor.
    """
    # Find the index of the necessary columns
    try:
        director_idx = header.index("Director")
        actors_idx = header.index("Actors")
    except ValueError as e:
        print(f"Column not found: {e}")
        return
    
    # Count collaboration pairs of director and actor
    collaboration_count = {}
    for row in data:
        director = row[director_idx]
        actors = row[actors_idx].split('| ')
        for actor in actors:
            pair = (director, actor)
            if pair in collaboration_count:
                collaboration_count[pair] += 1
            else:
                collaboration_count[pair] = 1
    
    # Find the top-7 frequent collaboration pairs
    top_7_pairs = sorted(collaboration_count.items(), key=lambda x: x[1], reverse=True)[:7]
    
    # Print the result
    print("#6")
    for i, (pair, count) in enumerate(top_7_pairs, 1):
        director, actor = pair
        print(f"Top-{i} Collaboration Pair: Director {director} & Actor {actor} with Count: {count}")
    print()

#7
def top_3_directors_most_collaborative_actors(file_path):
    """
    Finds and prints the top-3 directors who collaborate with the most actors.
    """
    # Find the index of necessary columns
    try:
        director_idx = header.index("Director")
        actors_idx = header.index("Actors")
    except ValueError as e:
        print(f"Column not found: {e}")
        return
    
    # Create a dictionary to store directors and their collaborative actors
    director_collaborative_actors = {}
    for row in data:
        director = row[director_idx]
        actors = row[actors_idx].split('| ')
        if director in director_collaborative_actors:
            director_collaborative_actors[director].update(actors)
        else:
            director_collaborative_actors[director] = set(actors)
    
    # Find the top-3 directors with the most collaborative actors
    top_3_directors = sorted(director_collaborative_actors.items(), key=lambda x: len(x[1]), reverse=True)[:3]
    
    # Print the result
    print("#7")
    for i, (director, collaborative_actors) in enumerate(top_3_directors, 1):
        print(f"Top-{i} Director: {director} collaborates with {len(collaborative_actors)} actors.")
    print()

#8
def top_6_actors_most_genres(file_path):
    """
    Finds and prints the top-6 actors playing in the most genres of movies.
    """
    # Find the index of the necessary columns
    try:
        genres_idx = header.index("Genre")
        actors_idx = header.index("Actors")
    except ValueError as e:
        print(f"Column not found: {e}")
        return
    
    # Count the number of genres each actor has played in
    actor_genres_count = {}
    for row in data:
        genres = row[genres_idx].split('| ')
        actors = row[actors_idx].split('| ')
        for actor in actors:
            if actor in actor_genres_count:
                actor_genres_count[actor] += len(genres)
            else:
                actor_genres_count[actor] = len(genres)
    
    # Find the top-6 actors with the most genres
    top_6_actors = sorted(actor_genres_count.items(), key=lambda x: x[1], reverse=True)[:6]
    
    # Print the result
    print("#8")
    for i, (actor, count) in enumerate(top_6_actors, 1):
        print(f"Top-{i} Actor: {actor} playing in {count} genres")
    print()

#9
def top_3_actors_largest_gap_years(file_path):
    """
    Finds and prints the top-3 actors whose movies lead to the largest maximum gap of years.
    """
    # Find the index of necessary columns
    try:
        actor_idx = header.index("Actors")
        year_idx = header.index("Year")
    except ValueError as e:
        print(f"Column not found: {e}")
        return
    
    # Create a dictionary to store actors and their maximum year gaps
    actor_max_year_gaps = {}
    for row in data:
        actors = row[actor_idx].split('| ')
        years = [int(year) for year in row[year_idx].split(', ') if year.strip()]  # Convert years to integers
        if not years:
            continue  # Skip if no years available for the movie
        # print(years)
        max_gap = max([abs(years[i] - years[j]) for j in range(i+1, len(years)) for i in range(len(years))]) if len(years) > 1 else 0
        for actor in actors:
            if actor in actor_max_year_gaps:
                actor_max_year_gaps[actor] = max(actor_max_year_gaps[actor], max_gap)
            else:
                actor_max_year_gaps[actor] = max_gap
    
    # Find the top-3 actors with the largest maximum year gaps
    top_3_actors = sorted(actor_max_year_gaps.items(), key=lambda x: x[1], reverse=True)[:3]

    # Print the result
    print("#9")
    for i, (actor, max_year_gap) in enumerate(top_3_actors, 1):
        print(f"Top-{i} Actor: {actor} has a maximum gap of {max_year_gap} years between movies.")

# Usage
file_path = 'C:/Users/minzh/Downloads/test folder/sources/IMDB-Movie-Data.csv'  # Update this with the actual file path
header, data = read_csv(file_path)
top_3_movies_highest_ratings_2016(file_path)
most_prolific_director(file_path)
actor_highest_total_revenue(file_path)
average_rating_emma_watson(file_path)
top_4_actors_most_movies(file_path)
top_7_collaboration_pairs(file_path)
top_3_directors_most_collaborative_actors(file_path)
top_6_actors_most_genres(file_path)
top_3_actors_largest_gap_years(file_path)

#會計系 H14126173 賈閔之