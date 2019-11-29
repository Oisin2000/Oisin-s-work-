List = []
i = 0
total = 0
stotal = 0
salesfigure = int(input("Please enter the sales figure : "))
total += salesfigure
while(salesfigure != -1) :
    List.append(salesfigure)
    salesfigure = int(input("Please enter the figure : "))
    total += salesfigure
    i = i+1

    print("The sales figure entered were ", List)
    for x in range(0,1) :
        List [x] +=0.23*List[x]
        stotal+=List[x]
print("The sales figure including vat were : ", List)
print("The total vat charged was : ",stotal - total)
print("The total sales for this period were : ",stotal)
    
