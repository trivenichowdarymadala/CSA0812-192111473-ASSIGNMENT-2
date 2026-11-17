def subsidy(units, ration, senior):

    if units <= 100:
        return "FULL SUBSIDY"

    elif units <= 200:
        if ration == "yes":
            return "PARTIAL SUBSIDY"
        else:
            return "NO SUBSIDY"

    else:
        if senior == "yes":
            return "SENIOR SUBSIDY"
        else:
            return "NO SUBSIDY"


# Main program
units = int(input("Enter electricity units: "))
ration = input("Do you have ration card (yes/no): ").lower()
senior = input("Is any member above 80 years (yes/no): ").lower()

result = subsidy(units, ration, senior)

print("Subsidy:", result)
