import matplotlib.pyplot as plt

class RegressionPredict:
    def __init__(self, x, y, projecttitle, xlabel="Innings", ylabel="Runs"):
        self.x = x                      # innings
        self.y = y                      # runs
        self.projecttitle = projecttitle
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.n = len(x)
        self.sigmax = sum(self.x)
        self.sigmay = sum(self.y)
        self.x2 = [i * i for i in x]
        self.y2 = [i * i for i in y]
        self.sigmax2 = sum(self.x2)
        self.sigmay2 = sum(self.y2)
        self.sigmaxy = sum([x[i] * y[i] for i in range(self.n)])

    def plotdata(self, x, y, xlabel, ylabel, plotlabel, projecttitle):
        plt.title(projecttitle)
        plt.xlabel(xlabel)  # X-axis = Innings
        plt.ylabel(ylabel)  # Y-axis = Runs
        plt.grid(True)
        plt.plot(x, y, color="red", label=plotlabel + " (Line)")    # Red line plot
        plt.scatter(x, y, color="blue", label=plotlabel + " (Points)")  # Blue scatter plot
        plt.legend()
        plt.show()

    def plotXY(self):
        self.plotdata(self.x, self.y, self.xlabel, self.ylabel,
                      "Innings vs Runs", self.projecttitle)

    def plotXX2(self):
        self.plotdata(self.x, self.x2, self.xlabel, "Innings²",
                      "Innings vs Innings²", self.projecttitle)

    def plotXvsXY(self):
        xy = [self.x[i] * self.y[i] for i in range(self.n)]
        self.plotdata(self.x, xy, self.xlabel, "X × Y", "Innings vs XY",
                      self.projecttitle + "\nXY = " + str(xy))

    def plotXvsY2(self):
        self.plotdata(self.x, self.y2, self.xlabel, "Runs²", "Innings vs Runs²",
                      self.projecttitle + "\nRuns² = " + str(self.y2))

    def plotXvsSigmaY(self):
        sigmay_list = [self.sigmay] * self.n
        self.plotdata(self.x, sigmay_list, self.xlabel, "ΣRuns", "Innings vs ΣRuns",
                      self.projecttitle + "\nΣRuns = " + str(self.sigmay))

    def plotXvsSigmaXY(self):
        sigmaxy_list = [self.sigmaxy] * self.n
        self.plotdata(self.x, sigmaxy_list, self.xlabel, "ΣInnings And Runs", "Innings vs ΣInnings x Runs",
                      self.projecttitle + "\nΣInnings_Runs = " + str(self.sigmaxy))

# Example use
innings = [1, 2, 3, 4, 5]
runs = [44, 32, 57, 90, 16]

rgp = RegressionPredict(innings, runs, "Virat's Runs in IPL")

rgp.plotXY()
rgp.plotXX2()
rgp.plotXvsXY()
rgp.plotXvsY2()
rgp.plotXvsSigmaY()
rgp.plotXvsSigmaXY()
