unit=int(input('Enter total consumed units :'))
cost=0
cost+=50*50
unit=unit-50
cost+=100*75
unit=unit-100
cost+=100*120
unit=unit-100
cost+=unit*150
print("total electricity bill :",cost)
