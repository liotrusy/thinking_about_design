# Keeping Tools Flexible

Here is an interesting question. How far into the future should we look at when building our analytical tools?


This is something I asked myself, as I revisisted some the code I built to analyze this the dataset 'AppleStore.csv'. Now why is this important?

## Not scripts, but software systems

Well, I believe that analytical scripts should be built using a software mentality. This means - quoting Max Kanat-Alexander - they should be "simple and easy-to-maintain/change". And here is why it is important.

Data explorations are driven by questions. For exmaple, I may ask myself:

*What is the average rating of Social and Gamings apps in my dataset?*

Now, especially if there is a tight deadline or the boss breathing down your neck, the first impulse might be to bust open the editor and start crunching out code to get a the answer quickly (social_and_games_exploration.py could be a good example). But, there is a problem.

What if the question changes a little bit? Maybe we want to explore other kinds of genres?

## Roadblocks to changes

A change in question is a change in requirements. So, does this mean that I need to re-write parts of my code? Well, it depends if your implementation was designed thinking about these possible changes.

In the social_and_games_exploration.py, I see the following roadblocks to changes in requirements/questions.

### Hard-coded values

The genres values are hard coded in the source. This means that each time I want to explore another category, I need to make edits to the source.

### Limit to always/only two genres

This implementation needs always two, and only two genres, to return the average rating.

This is a limiting feature. Because, in the dataset, we have 23 unique categories, so what if I want to explore more or less than two genres?






