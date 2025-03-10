from datetime import date
movie_rating_system = {}

print("Bokku movie box")

def menu():
	return """
	1.Add a movie 🎬
	2.Rate a movie
	3.View average rate
	4.Exit
	"""

def add_movie(movie_name):
	if movie_name in movie_rating_system:
		return "Movie is already added"
	else:
		movie_rating_system[movie_name] = {"ratings": [], "added_on": str(date.today())}
		return "movie added succesfully 🎬"
		
		
def get_movie_input():
    while True:
	    movie_name = input("Enter the name of the movie: ").strip()
	    if not movie_name:
	        raise ValueError("invalid input.Enter again")
	    return movie_name

    
    
def rate_movie(movie_name, rating_input):
    if movie_name in movie_rating_system:
        movie_rating_system[movie_name]["ratings"].append(float(rating_input))
        return f"Rating  added for {movie_name} {rating_input}."

    else: 
        return "Movie is not found. Add a movie first"

def get_rating_input():
    return input("Enter rating from (1 - 5): ").strip()

def get_current_date():
    return str(date.today())
    
def calculate_average_rating(movie_name):
    if movie_name in movie_rating_system:
        rating = movie_rating_system[movie_name]['ratings']
        if rating:
            return sum(rating) / len(rating) 
        else:
            return "No rating yet"
    else: 
        return "No movie found"
        
def view_average_rating():
    if not movie_rating_system:
        return "No movie yet"
        
    current_date = get_current_date()
    result = f"\n🎬 Movie List (Viewed on {current_date}):\n"

    for movie, details in movie_rating_system.items():
        aveg = calculate_average_rating(movie)
        result += f"🎬 {movie} - Added on {details['added_on']} - Average Rating: {aveg}\n"
        
    return result
       
       
        
			
def main():
	while True:
		print(menu())
		try:
			choice = int(input("Choose from the menu above: "))
		except ValueError:
			print("invalid input.Choose from the menu above")
			continue

		if choice == 1:
			movie_name = get_movie_input()
			result = add_movie(movie_name)
			print(result)
		
		elif choice == 2:
		    movie_name = get_movie_input() 
		    rating_input = get_rating_input()
		    result = rate_movie(movie_name, rating_input)
		    print(result)
		    
		elif choice == 3:
		    print(view_average_rating())
		    
		elif choice == 4:
		    print("exiting App. Goodbye")
		
		else:
		    print("invalid input. Enter 1 - 4")
	    
	        
	
		    		

if __name__ == "__main__":
    main()
		                	
			
		
