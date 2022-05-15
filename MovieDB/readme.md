This is a basic sqlite program that fetches the data stored in an sql database, being movies, directors and actors details.
The relationship set between the entities is as follow: 
![ERD](https://user-images.githubusercontent.com/84664682/168487827-0dc74e56-4cb0-4d80-9afe-aad5e923bef8.jpg)
Note that the relationship is established by the use of foreign key with respect to directors and movies, assuming that each movie is directed by one singular person.
And the relationship between actors and movies is established with the use of a weak entity, which relates actor_ID with movie_ID. This is to ensure that all the actors acting in a movie are listed.
The program simply lists all the movies. Note that a single movie+director might be listed multiple times to cover all the actors that might have acted in the movie.
