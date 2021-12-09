units=int(input("enter the units"))
if units>0 and units<=50:
    total_units=units*0.50
    print("cost of electricity",total_units)
elif units<=100:
    total_units=50*0.50 +units*0.75
    print("cost of electricity",total_units)
elif units<=250:
    total_units=50*0.50+100*0.75+units*1.20
    print("cost of electricity",total_units)
elif units>250:
    total_units=50*0.50+100*0.75+250*1.20+units*1.50+0.2
    print("cost of electricity",total_units)
else:
    print("enter the units",units)