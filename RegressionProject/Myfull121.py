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
        self.x2 = [i * i for i in x]
        self.y2 = [i * i for i in y]
        self.sigmax2 = sum(self.x2)
        self.sigmay2 = sum([i * i for i in y])
        self.sigmaxy = sum([x[i] * y[i] for i in range(self.n)])

    # defined a function pass the written arguments
    def plotdata(self, x, y, xlabel, ylabel, plotlabel, projecttitle):
        plt.title(projecttitle)
        plt.xlabel(xlabel)  # Assign the name to X-Axis
        plt.ylabel(ylabel)  # Assign the name to Y-Axis
        plt.grid(True)
        plt.plot(x, y, color="red", label=plotlabel,linestyle="--",marker='o')
        plt.scatter(x, y, color="blue", label=plotlabel,marker="X",s=100)
        plt.legend()
        plt.show()

    def plotXY(self):
        self.plotdata(self.x, self.y, self.xlabel, self.ylabel,"Runs per innings", self.projecttitle)

    def plotXX2(self):
        self.plotdata(self.x, self.x2, self.xlabel, "Innings²", "Innings squared",self.projecttitle + "\nInnings=" + str(self.x) + "\nInnings²=" + str(self.x2))

    def plotXvsXY(self):
        xy = [self.x[i] * self.y[i] for i in range(self.n)]
        self.plotdata(self.x, xy, self.xlabel, "  Innings x Runs", "Innings vs Innings And Runs",self.projecttitle + "\nInnings _Runs = " + str(xy))

    def plotXvsY2(self):
        self.plotdata(self.x, self.y2, self.xlabel, "Runs²", "Innings vs Runs²",self.projecttitle + "\nRuns² = " + str(self.y2))

    # def plotXvsSigmaY(self):
    #     sigmay_list = [self.sigmay] * self.n  # Constant list
    #     self.plotdata(self.x, sigmay_list, self.xlabel, "ΣInnings", "Innings vs ΣRuns",self.projecttitle + "\nΣRuns = " + str(self.sigmay))


    # def plotXvsSigmaXY(self):
    #     sigmaxy_list = [self.sigmaxy] * self.n  # Repeat scalar for plotting
    #     self.plotdata(self.x, sigmaxy_list, self.xlabel, "ΣXY", "X vs ΣXY",self.projecttitle + "\nΣXY = " + str(sigmaxy_list))


# Create object and call the plotting methods
rgp = RegressionPredict([1, 2, 3, 4, 5], [44, 32, 57, 90, 16], "Virat's Runs in IPL", "Innings", "Runs")

rgp.plotXY()
rgp.plotXX2()
rgp.plotXvsXY()
rgp.plotXvsY2()
# rgp.plotXvsSigmaY()

