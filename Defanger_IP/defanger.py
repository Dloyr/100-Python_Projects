def defanger(adress):
    defanger_ip=""

    for i in adress:
        if i == ".":
            defanger_ip += "[.]"
        else:
            defanger_ip += i

    print("\nThe defanger IP is : {}".format(defanger_ip))
    return 0
