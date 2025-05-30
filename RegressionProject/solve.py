import StateHumid as fp

x= [1, 2, 3, 4, 5]
y = [2, 3, 5, 4, 6]
reg = fp.RegressionPredictor(x,y)
reg.plot("Plot Title", "Regression Plot", "X-axis", "Y-axis")
output = reg.predict([6, 7, 8])
print("Predicted values for [6, 7, 8]:", output)
print(reg)

reg.plot("Humidity plot","State Humidity","Days","Humidity that day")
