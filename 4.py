def suppr_car(x,y):
    a=-1
    for i in x:
        a=a+1
        if i==y:
            x=x.replace(x[a],"")
    return x

