# Name: Maximilian Kirsh
# Date: 2026-11-11
# Program: paycheck calculator
# Description: prints weekly pay stub

#Constants
FEDERAL_TAX_RATE = 0.10
STATE_TAX_RATE = 0.035
SOCIAL_SECURITY_RATE = 0.062
MEDICARE_RATE = 0.0145
WEEKS_PER_YEAR = 52


employee_name = input("Employee Name: ")
hourly_pay_rate = input("Hourly Pay Rate: ")
pay = int(hourly_pay_rate)
hours_worked_this_week = input("Hour Worked This Week: ")
hours = int(hours_worked_this_week)

#Heading
print("=" *32)
print("PAY STUB")
print("=" *32)

print("Hours Worked: ", hours)
print("Hourly Rate: ", pay)
gross_pay = pay * hours
print("Gross Pay: ", gross_pay)
print("-" *32)

federal_tax = gross_pay * FEDERAL_TAX_RATE
state_tax = gross_pay * STATE_TAX_RATE
social_security = gross_pay * SOCIAL_SECURITY_RATE
medicare = gross_pay * MEDICARE_RATE
total = federal_tax + state_tax + social_security + medicare

print(f"Federal Tax (10%): ${federal_tax:.2f}")
print(f"State Tax (3.5%): ${state_tax:.2f}")
print(f"Social Security: ${social_security:.2f}")
print(f"Medicare: ${medicare:.2f}")
print(f"Total Taken Out: ${total:.2f}")

print("-" *32)

net_pay = gross_pay - total
print(f"NET PAY: ${net_pay:.2f}")

print("=" *32)

percent_kept = net_pay / gross_pay *100
print(f"You keep {percent_kept:.1f}% of what you earn.")

yearly_gross = gross_pay * WEEKS_PER_YEAR
yearly_net = net_pay * WEEKS_PER_YEAR
print(f"Yearly gross: ${yearly_gross:.2f}")
print(f"Yearly net: ${yearly_net:.2f}")

