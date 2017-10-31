# Assignment 1: 
# Review your classmate's Citibike project proposal
### Sarah Schoengold (ses515, @sebscho) reviewing Colin Andurs (cra354, @colinandurs)

### The experiement
Colin asks the question: Will senior riders ride significantly less time than young riders? He framed his null hypothesis correctly, both when spelled out and when expressed as a formula. In his null hypothesis, he clearly states the confidence level, and the exact age groups within his experiement. 

### Suggestions
It's possible to include average ages of riders instead of removing all NaN years. We could also substitute the mean age for riders that provided fake years. Alternatively, the threshold for which he removed users could be lower — he removes those riders who listed ages above 100, but we could instead remove all riders that are two sigma (or farther) away from the mean age. This stems from my hypothesis that not many 90 year olds are out on citi bikes. It's also possible to classify age into more groups than just "old" or "young." Outside of that, which I know Colin already addressed, he set up his question and data very well!

### The suggested significance test
To test significance, there are a few routes we could go. I recommend the **Chi Squared goodness of fit** test for the following reasons. First, the Chi Squared test is optimal when the main question is asking "do data match an expected ratio?" For comparing the duration of trips between two age categories, this describes what we're looking for well. Next, the test only focus on one sample, and also only has one variable (age group). 

# FBB: Sara and Colin : notice that is not Chi sq for goodness of fit bur chisq for proportions!

##### references: 
* [wikipedia chi squared](https://en.wikipedia.org/wiki/Chi-squared_test)
* [stats test flow chart](https://i.pinimg.com/originals/da/c9/60/dac96086a651aea01b0ef24da4faaa9f.jpg)
