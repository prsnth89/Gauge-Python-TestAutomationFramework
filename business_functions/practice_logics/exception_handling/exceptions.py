def process(data):
    data=[1,2,3]
    #data[1]=2
    print("in method---",data)
    return data[-2]

measurements=[0 for i in range(3)]
process(measurements)
print(measurements[-2])