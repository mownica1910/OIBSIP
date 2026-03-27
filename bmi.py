# BMI Calculator with Suggestions

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height ** 2)

# Category + Suggestions
if bmi < 18.5:
    category = "Underweight"
    suggestion = "Increase calorie intake, eat protein-rich foods, and consult a nutritionist."

elif bmi < 25:
    category = "Normal"
    suggestion = "Maintain your healthy lifestyle with balanced diet and regular exercise."

elif bmi < 30:
    category = "Overweight"
    suggestion = "Exercise regularly, reduce sugar intake, and follow a balanced diet."

else:
    category = "Obese"
    suggestion = "Consult a doctor, follow a strict diet plan, and increase physical activity."

# Output
print("BMI:", round(bmi, 2))
print("Category:", category)
print("Suggestion:", suggestion)