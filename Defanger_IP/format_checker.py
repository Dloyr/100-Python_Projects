from defanger import defanger

def format_checker(adress):
    tokens = adress.split(".")
    errors = []

    if len(tokens) == 4:
        for token in tokens:
            if not token.isdigit():
                errors.append("\nERROR| {} is not a number".format(token))
                break
            elif not 1 <= int(token) <= 255:
                errors.append("\nERROR| {} is out of range. He must be between 0 and 255".format(token))
                break

        if errors:
            for error in errors:
                print(error)
                return 1
        else:
            defanger(adress)
    else:
        print("\nERROR |The format of IP adress must be: xxx.xxx.xxx.xxx")
        return 1
