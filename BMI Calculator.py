import pandas as pd

#loading json data locally
data = pd.read_json("C:/Users/LENOVO/Documents/Data Analysis with Python/data.json")

#converting HeightCm to Height(m)
data["HeightCm"] = data["HeightCm"]/100
data.rename(columns={"HeightCm":"Height(m)"},inplace=True)

#Calculate the BMI
data["BMI"] = data["WeightKg"]/(data["Height(m)"]*data["Height(m)"])

#initialise overWeightCount and temporary list
overWeightCount=0
templist1 = []
templist2 = []

#assigning BMI Category and the Health Risk.
for y in data["BMI"]:
        if y > 40:
            templist1.append("Very severely obese")
            templist2.append("Very high risk")
        if y > 35 and y < 39.9:
            templist1.append("Severely obese")
            templist2.append("High risk")
        if y > 30 and y < 34.9:
            templist1.append("Moderately obese")
            templist2.append("Medium risk")
        if y > 25 and y < 29.9:
            templist1.append("Overweight")
            templist2.append("Enhanced risk")
            overWeightCount +=1
        if y > 18.5 and y <24.9:
            templist1.append("Normal weight")
            templist2.append("Low risk")
        if y < 18.4:
            templist1.append("Underweight")
            templist2.append("Malnutrition risk")

#assigning BMI Category and the Health Risk in dataframe
data["BMI category"] = templist1
data["Health risk"] = templist2

#observations
print("the total number of overweight:",overWeightCount)
print("data describe", data.describe())

data.to_csv("D:/BMI Calculator/outputData.csv")