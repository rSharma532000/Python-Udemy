seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()

match seat_type:
    case "sleeper":
        print("sleeper - no ac, beds availabe")
    case "ac":
        print("AC - Air conditioned")
    case "general":
        print("general - cheap")
    case "luxury":
        print("luxury - premium")
    case _:
        print("invalid seat")
        