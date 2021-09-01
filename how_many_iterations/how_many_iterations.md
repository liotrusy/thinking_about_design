# How Many Iterations

Today, we ask a super quick question.

**Can we improve the execution time by moving a single line of code?**

The scripts we use today, will return us three pieces of information:

* the average rating for apps above a price point
* the number of apps above a price point
* the number of apps below or equal to a price point

## The outcome

Turns out that by nesting a variable assignment inside the body of an if statement we can speed things up. That's because the variable assignment fires only in those instances where the condition is met, instead that in all records of the dataset. 

By running timing the program on 50 executions on my machine I get the following result:

* Subject_1 time: 1.3613s. 
* Subject_2 time: 1.2679s. 

Basically, the code becomes ~0.1s faster by moving the placement of one line of code.

Now on a dataset of only 7,197 entries this time gain may not be significant. However, if we find ourselves dealing with much larger volumes of data - maybe even with a time sensitive program - things may be quite different. Anyways, love this stuff!

All the best
Pierre


