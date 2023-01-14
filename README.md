# interactive_plot
Step 1. initial question
From the given dataset, I am raising the questions list below:
1.	An overall calculation for athletes participates from all countries in total or detailed in certain year.
2.	A summary athlete’s numbers for different sports sorted by country and year.
3.	To find a potential connection between winning medal and age, height and weight. For example, if a team have an overall history with younger age athlete are they more likely to win more medals.

Step 2. Assess the fitness of the data
The dataset is reformed by using pandas to filter out the information we needed for the answer. In interactive part I filter the specific country name and year by adding widgets. In 3d plot I use value count and create a dataset for overall calculation.

Step 3. Design three visualization techniques and describe
1. Visualization techniques and visual encodings
a) Choropleth (plotly, ipywidgets)
b) Histogram (plotly, ipywidgets)
c) 3d plot (Axes3D)
2. Colors
	I choose the spectrum that color is differ to different scale.


3.Description of Design
a) Choropleth (map plot)
![1](https://user-images.githubusercontent.com/102940480/212443953-7cd956fa-7df1-4364-b5ba-fe62b937ae52.png)

Figure 1Choropleth map
Figure1 shows a total athlete number by countries overall, by choosing the year it will show the summary for that year. Map is the most straight forward technique to show the overall state for the world, and have a rough image about a country is the participate number consider high or low, and changes overtime. However, this technique is weak on showing connections between the features.

b) Histogram
 ![2](https://user-images.githubusercontent.com/102940480/212443956-256d4919-19ba-43a2-bef5-342ada055707.png)

Figure 2 Sports histogram by country
Figure2 shows athletes number by teams, by choosing one sport or a certain year. This plot shows the preference for athletes in one country by total and by certain year. By comparing the data, we will be able to know the changes overtime for one country participate in one sport or we can compare between the countries we select, if their athletes are increasing or decreasing overtime in some sports. 
c) 3d plot
 ![3](https://user-images.githubusercontent.com/102940480/212443959-db4a5102-e670-49fb-b444-27ff31401523.png)

Figure 3 Comparison 3D plot
Figure3 shows the relationships between how much medals got in history and athlete’s age, weight and height by country. In this plot we can see a country that has athletes in younger ages with high height and light weight are more likely to get more medals. However, this technique could be lack of details since the gap in total medals between countries are large so that the difference is not evidently identify.

Conclusion.
All three figures are corresponded to the questions I have for this dataset. The visual plot shows an overall comparison by different conditions that could help us to filter the information we need. While some technique is design to visualize the data overall and some are more specific to certain area. I think the histogram is most suitable for the initial question.

