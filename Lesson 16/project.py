def shutdown(o):
    s=o.lower()
    if s=="yes":
        print("SHUTTING DOWN...")
    elif s=="no":
        print("ABORT SHUT DOWN")
    else:
        print("Sorry? Only enter yes or no.")

cmnd=input("PLease enter command: ")
shutdown(cmnd)
