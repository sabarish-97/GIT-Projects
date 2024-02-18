def compound_interest (principal, interest_rate, duration):
    if interest_rate <= 0 and interest_rate > 1:
        print(f"please enter a valid deccimal between 0 and 1, the interest rate {interest_rate} is not valid")
    elif duration <= 0:
        print(f"please enter a valid positive number of months, the given duration {duration} is not valid")
    else:
        total = principal * (1 + interest_rate) ** duration
        return total
principal_input = float(input("please enter the principal \n"))
interest_rate_input = float(input("please enter the interest rate \n"))
duration_input = float(input("please enter the duration in months \n"))
calculated_ci = compound_interest(principal_input, interest_rate_input, duration_input)
print(f"your matured amount in {duration_input} months will be :")
print("%.2f" % calculated_ci)
