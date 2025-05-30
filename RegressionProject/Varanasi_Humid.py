import StateHumid as fp

Days= [1, 2, 3, 4, 5]   #Take five days of varanasi district
Humidity_Data = [24, 36, 57, 4, 6]   #corresponding Days Humidity Data
reg = fp.RegressionPredictor(Days,Humidity_Data)
reg.plot("Plot Title", "Regression Plot", "X-axis", "Y-axis")
output = reg.predict([6, 7, 8])
print("Predicted values for [6, 7, 8]:", output)
print(reg)

reg.plot("Humidity plot","Varanasi Humidity","Days","Humidity that day")
