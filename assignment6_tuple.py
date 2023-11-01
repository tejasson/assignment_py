sample = [('item1', '13.10'), ('item2', '17.10'), ('item3', '25.3')]
tempTuple = ()
while(True):
    if sample[0][1]<sample[1][1]:
        tempTuple=sample[0]
        sample[0]=sample[1]
        sample[1]=tempTuple
    elif sample[1][1]<sample[2][1]:
        tempTuple=sample[1]
        sample[1]=sample[2]
        sample[2]=tempTuple
    else:
        break

print(sample)