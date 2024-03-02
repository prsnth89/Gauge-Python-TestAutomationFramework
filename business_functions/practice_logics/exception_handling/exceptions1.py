try:
    character="ABC"[3]
except IndexError:
    print("Mishit")
except:
    print("failure")