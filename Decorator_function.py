
# Decorators are blueprint
def dec1(func1):
    def nowExec():
        print("Executing now")
        func1()
        print("Executed")
    return nowExec

@dec1
def who_is_khand():
    print("Khand is 420 ladka")
    # who_is_khand = dec1(who_is_khand)
who_is_khand    
