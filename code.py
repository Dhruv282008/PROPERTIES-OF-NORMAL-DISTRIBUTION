import plotly.figure_factory as ff 
import statistics  
import pandas as pd 
import plotly.graph_objects as go
df = pd.read_csv("StudentsPerformance.csv")
heightlist = df["Height(Inches)"].to_list()
stdev = statistics.stdev(heightlist)
mean = statistics.mean(heightlist)
median = statistics.median(heightlist)
mode = statistics.mode(heightlist)

height_firststdev_start, height_firststdev_end = mean - stdev, mean + stdev
height_secondstdev_start, height_secondstdev_end = mean - (2*stdev), mean + (2*stdev)
height_thirdstdev_start, height_thirdstdev_end = mean - (3*stdev), mean + (3*stdev)

#Lists
height_datawithin_firststdev = [result for result in heightlist if result > height_firststdev_start and result < height_firststdev_end]
height_datawithin_secondstdev = [result for result in heightlist if result > height_secondstdev_start and result < height_secondstdev_end]
height_datawithin_thirdstdev = [result for result in heightlist if result > height_thirdstdev_start and result < height_thirdstdev_end]

print("Standard Deviation of Height column is {}".format(stdev))
print("Median of the data is {}".format(median))
print("Mode of the data is {}".format(mode))
print("Mean of the data is {}".format(mean))

print("{}% of data lies with 1 Standard Deviation".format(len(height_datawithin_firststdev)*100 / len(heightlist)))
print("{}% of data lies with 2 Standard Deviation".format(len(height_datawithin_secondstdev)*100 / len(heightlist)))
print("{}% of data lies with 3 Standard Deviation".format(len(height_datawithin_thirdstdev)*100 / len(heightlist)))

fig = ff.create_distplot([heightlist], ["Height"])
fig.add_trace(go.Scatter(x = [height_firststdev_start, height_firststdev_start], y = [0, 0.2], mode = "lines", name = "1 Standard Deviation Start"))
fig.add_trace(go.Scatter(x = [height_firststdev_end, height_firststdev_end], y = [0, 0.2], mode = "lines", name = "1 Standard Deviation End"))
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.2], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [height_secondstdev_start, height_secondstdev_start], y = [0, 0.2], mode = "lines", name = "2 Standard Deviation Start"))
fig.add_trace(go.Scatter(x = [height_secondstdev_end, height_secondstdev_end], y = [0, 0.2], mode = "lines", name = "2 Standard Deviation End"))
fig.show()