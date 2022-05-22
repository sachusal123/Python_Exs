total_items=int(input("Enter total number of items buying:"))
cost_1=cost_2=cost_3=0

if total_items<10:
    cost_1=total_items*12
    print("Total no of items:-",total_items)
    print("Cost of ",total_items," items =",cost_1)

elif total_items>10 and total_items<99:
    cost_2=total_items*10
    print("Total no of items:-",total_items)
    print("Cost of ",total_items," items =",cost_2)

elif total_items>=100:
    cost_3=total_items*7
    print("Total no of items:-",total_items)
    print("Cost of ",total_items," items =",cost_3)
