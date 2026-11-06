def calculate_emi(principal,annual_rate,months):
    r=annual_rate/12/100
    if annual_rate==0:
        emi=principal/months
    else:
        emi= principal*r*(1+r)**months/((1+r)**months-1)
    return float(f"{emi:.2f}")
def total_payable_amount(emi,months):
    total_payable= emi*months
    return float(f"{total_payable:.2f}")
def total_interest(total_payable, principal):
    interest=total_payable-principal
    return float(f"{interest:.2f}")
def check_eligibility(emi,income):
    limit=income*0.4
    if emi<=limit:
        return True
    else:
        return False
def validate_inputs(principal,annual_rate,income,months):
    if principal<=0:
        return "Invalid loan amount. Enter a positive amount."
    elif annual_rate<0 or annual_rate>30:
        return "Invalid interest rate"
    elif months<1 or months>360:
        return "Invalid tenure"
    elif income<=0:
        return "Invalid monthly income"
    else:
        return None

principal= float(input("Principal: "))
annual_rate= float(input("Annual rate: "))
months = int(input("Tenure: "))
income= float(input("Monthly income: "))
validate= validate_inputs(principal,annual_rate,income,months)
if validate:
    print(validate)
else:
    emi=calculate_emi(principal,annual_rate,months)
    total =total_payable_amount(emi,months)
    interest= total_interest(total, principal)
    eligible=check_eligibility(emi,income)
    if eligible:
        print(f"EMI: Rs.{emi:.2f}|Total Payable: Rs.{total:.2f}")
        print(f"Total Interest: rs.{interest:.2f}|Eligible:Yes")
    else:
        max_emi=income*0.4
        print(f"EMI:Rs.{emi:.2f}")
        print(f"Maximum allowed EMI(40% of income):RS:{max_emi:.2f}")
        print("Loan not eligible: EMI exceeds the allowed limit")
