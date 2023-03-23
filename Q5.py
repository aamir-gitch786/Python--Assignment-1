'''5. Develop a Python program to accept the salary of an employee from the user. Calculate
the gross salary on the following basis: '''

Basic = float(input("Enter your basic salary : "))

if Basic>=1 and Basic<=4000:
 HRA = Basic*0.1
 DA = Basic*0.5
elif Basic>=4001 and Basic<=8000:
 HRA = (Basic-4000)*0.2+400
 DA =  (Basic-4000)*0.6+2000
elif Basic>=8001 and Basic<=12000:
 HRA = (Basic-8000)*0.25+400+800
 DA = (Basic-8000)*0.7+2000+2400
else:
 HRA = (Basic-12000)*0.3+400+800+1000
 DA = (Basic-12000)*0.8+2000+2400+2800

print(f"Gross salary is : {Basic+HRA+DA}")