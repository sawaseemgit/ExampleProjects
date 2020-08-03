def Do(num=0):
    try:
        if num:
            return int(num) + 10
        else:
            return "Please enter a number"
    except ValueError as err:
        return err
