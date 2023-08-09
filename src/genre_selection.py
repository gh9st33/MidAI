```python
# src/genre_selection.py

from src.constants import GENRES
from src.utils import post_message

selected_genre = None

def select_genre():
    global selected_genre
    print("Please select a genre from the following options:")
    for i, genre in enumerate(GENRES):
        print(f"{i+1}. {genre}")
    genre_index = int(input("Enter the number corresponding to your chosen genre: ")) - 1
    if genre_index < 0 or genre_index >= len(GENRES):
        print("Invalid selection. Please try again.")
        return select_genre()
    selected_genre = GENRES[genre_index]
    post_message("GenreSelectionComplete", selected_genre)
    return selected_genre
```