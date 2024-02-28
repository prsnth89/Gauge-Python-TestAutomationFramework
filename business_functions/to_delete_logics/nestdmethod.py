# def walk(stop, start=1):
#     print(start, end="  ")
#     if start+1<stop:
#         walk(stop,start+1)

# walk(4)

def walk(top):
    if top==0:
        return 0
    else:
        a= top+walk(top-1)
        print("a---",a)
        return a

print(walk(10))