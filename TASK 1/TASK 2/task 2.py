
OTP = "4821"
attempts = 0

while attempts < 3:
    enter = input("Enter OTP: ")

    if enter == "":
        print("Blank entry! Try again.")
        continue

    if enter == OTP:
        print("OTP Verified Successfully")
        break
    else:
        attempts += 1
        print("Wrong OTP! Attempts left:", 3 - attempts)

else:
    print("Account locked for 30 minutes")
