def walk(top):
    if top==0:
        return 0
    a= top+walk(top-1)
    print("top---",top)
    print("a---",a)
    return a

print(walk(5))