def validate_pin(pin):
    # check pin is made of only digits
    if pin.isdigit() == True:
        # check pin length is valid
        if len(pin) == 4 or len(pin) == 6:
            return True
        else:
            return False
    else:
        return False
