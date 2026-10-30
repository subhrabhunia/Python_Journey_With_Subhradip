def converter(usd_value):
    inr_value = usd_value * 82.74
    print(f"{usd_value} USD is equal to {inr_value} INR")
usd_value = float(input("Enter the amount in USD: "))    
converter(usd_value)