# Super Duper Spork
This is a python 3 project for performing a search on wikipedia and getting
a summary of an article. This is intended as an exercise in using Beautiful
Soup 4 and NLTK.

## Dependencies
* python3
* NLTK
* bs4

## Usage
Just run the super_duper_spork.py script and supply it with a search term. If
it finds a disambiguation page or search suggestions page, it will print out
search suggestions for you. Otherwise, it will give you summmarized article
text.

```bash
python3 super_duper_spork.py <search term>
```

## License
MIT
