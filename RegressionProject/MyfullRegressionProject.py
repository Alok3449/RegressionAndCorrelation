import matplotlib.pyplot as plt
class RegressionPredict:
    def __init__(self,x,y,projecttitle,xlabel="X",ylabel="Y"):

        self.x=x
        self.y=y
        self.projecttitle=projecttitle
        self.xlabel=xlabel
        self.ylabel=ylabel
        self.x2=[i*i for i in x]


    def plotdata(self,x,y,xlabel,ylabel,plotlabel,projecttitle): #defined a function pass the written arguments
        plt.title(projecttitle) #Sets the title of the plot window to the value of projecttitle on the upper Screen
        plt.xlabel(xlabel)  #Assign the name to X-Axis
        plt.ylabel(ylabel) #Assign the name to Y-Axis
        plt.grid(True)   #Activate the grid in the plot to help us analyze how data are changes
        plt.plot(x,y,color="red",label=plotlabel)  #Draws a red line plot of the x and y data.  2->Assign a label to plottedline
        plt.scatter(x,y,color="blue",label=plotlabel)   #Draws a Scatter line to x and y data. 2->Assign a label to plotted scatter line
        plt.legend()   #display a legend what blue and red line name show 
        plt.show() #plot the desired diagram which is required



    def plotXY(self):
        self.plotdata(self.x,self.y,self.xlabel,self.ylabel,
                      "Runs per innings",self.projecttitle)
        
    def plotXX2(self):
        self.plotdata(self.x,self.x2,self.xlabel,"Innings2","Runs per innings",self.projecttitle+"\nInnings="+str(self.x)+str(self.x2))

rgp=RegressionPredict([1,2,3,4,5],[44,32,57,90,16],"Virat's Runs in IPL","Innings","Runs")

rgp.plotXY()

#this function will return a plot containing lines and scatter point according to innings vs Runs of virat kohli In  Ipl Format 

rgp.plotXX2()
#this function will return a plot containing lines and scatter point according to innings Square vs Innings of virat kohli In  Ipl Format 

