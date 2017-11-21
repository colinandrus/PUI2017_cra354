![plot](andrusplot.png)

Hi Colin,

I've looked at your dataset and your plot and see that its reflects the ratio of accidents caused by drunk driving compared to the total number of vehicular accidents. In terms of color and labels it is very well done but I think there are a couple of things you can change. In your legend it says "Alcohol contributing factor for Vehicle 1" but this may not be fully representative. It would be best to take the sum of alcohol contributing factor for all vehicles in the dataset. Also I'm not sure it was clear why you needed to use a log scale to make the plot. The ratio of values change when you take the log of values. For instance, say the number of accidents caused by drunk driving is 100 and total accidents is 1000 and the ratio is .10 but if using log base 10, 100 becomes 2 and 1000 becomes 3 making the ratio .66 which is clearly not the case. Try plotting the data without taking the logs which would also allow us to see the true number of accidents.

Best,
Prince