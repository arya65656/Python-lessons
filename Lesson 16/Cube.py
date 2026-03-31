def cube(n):
    return(n**3)
def div(n):
    if n%3==0:
        return cube(n)
    else:
        return False
print(div(8))