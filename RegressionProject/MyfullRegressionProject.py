import matplotlib.pyplot as plt


class RegressionPredict:
    def __init__(self, x, y, projecttitle, xlabel="X", ylabel="Y"):

        self.x = x
        self.y = y
        self.projecttitle = projecttitle
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.n = len(x)
        self.sigmax = sum(self.x)
        self.sigmay = sum(self.y)
        self.x2 = [i*i for i in x]
        self.y2 = [i*i for i in y]
        self.sigmax2 = sum(self.x2)
        self.sigmay2 = sum([i * i for i in y])
        self.sigmaxy = sum([x[i] * y[i] for i in range(self.n)])

    # defined a function pass the written arguments
    def plotdata(self, x, y, xlabel, ylabel, plotlabel, projecttitle):
        # Sets the title of the plot window to the value of projecttitle on the upper Screen
        plt.title(projecttitle)
        plt.xlabel(xlabel)  # Assign the name to X-Axis
        plt.ylabel(ylabel)  # Assign the name to Y-Axis
        # Activate the grid in the plot to help us analyze how data are changes
        plt.grid(True)
        # Draws a red line plot of the x and y data.  2->Assign a label to plottedline
        plt.plot(x, y, color="red", label=plotlabel,linestyle="--",marker='o')
        # Draws a Scatter line to x and y data. 2->Assign a label to plotted scatter line
        plt.scatter(x, y, color="blue", label=plotlabel,marker="X",s=100)
        plt.legend()  # display a legend what blue and red line name show
        plt.show()  # plot the desired diagram which is required

    def plotXY(self):
        self.plotdata(self.x, self.y, self.xlabel, self.ylabel,
                      "Runs per innings", self.projecttitle)

    def plotXX2(self):
        self.plotdata(self.x, self.x2, self.xlabel, "Innings2", "Runs per innings",
                      self.projecttitle+"\nInnings="+str(self.x)+str(self.x2))

    def plotXvsXY(self):
        xy = [self.x[i] * self.y[i] for i in range(self.n)]
        self.plotdata(self.x, xy,self.xlabel, "Innings × Runs","Innings vs Runs", self.projecttitle + "\nInnings x Runs = " + str(xy))


    def plotXvsY2(self):
        self.plotdata(self.x, self.y2,self.xlabel, "Innings²","Runs vs Innings²", self.projecttitle + "\nRuns² = " + str(self.y2))


    # def plotXvsSigmaY(self):
    #     sigmay_list = [self.sigmay] * self.n  # Constant list
    #     self.plotdata(self.x, sigmay_list,self.xlabel, "ΣInnings","Runs vs ΣInnings", self.projecttitle + "\nΣInnings = " + str(self.sigmay))


rgp = RegressionPredict([1, 2, 3, 4, 5], [44, 32, 57, 90, 16],"Virat's Runs in IPL", "Innings", "Runs")

rgp.plotXY()

# this function will return a plot containing lines and scatter point according to innings vs Runs of virat kohli In  Ipl Format

rgp.plotXX2()
# this function will return a plot containing lines and scatter point according to innings Square vs Innings of virat kohli In  Ipl Format
rgp.plotXY()
rgp.plotXX2()
rgp.plotXvsXY()
rgp.plotXvsY2()
#rgp.plotXvsSigmaY()
