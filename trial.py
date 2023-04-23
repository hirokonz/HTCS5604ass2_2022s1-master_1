



def isValidChoice(choice):
    """
    @param choice: String
    @return valid: Bool
    """
    if choice in ["1", "2", "3", "4", "5", "6"]:
        return True
    return False

choice  = input("choice? ")

print(choice)
