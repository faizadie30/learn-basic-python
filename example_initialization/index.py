import package
import datetime

addition = package.math.addition(1,2,3,4,5,6,7)
print(f"1+2+3+4+5+6+7 = {addition}")

substraction = package.math.substraction(100,50)
print(f"100 - 50 = {substraction}")

celcToFahrenheit = package.physics.celciusToFahrenheit(33)
print(f"30c to fahrenheit = {celcToFahrenheit}")

celcToKelvin = package.physics.celciusToKelvin(33)
print(f"30c to Kelvin = {celcToKelvin}")

celcToReamur = package.physics.celciusToReamur(33)
print(f"30c to Reamur = {celcToReamur}")

birthOfDay = datetime.date(1921,5,8)
profile = package.profile.setUser(name = "Jenderal Besar TNI H. M. Soeharto",birthDay = birthOfDay.strftime("%X"),domicile="Jakarta")
print(f"biograf soeharto: {profile}")