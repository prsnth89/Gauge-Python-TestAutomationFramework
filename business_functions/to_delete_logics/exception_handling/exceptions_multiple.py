try:

    a=int(input("Enter a number---"))
    b=a/1

except ZeroDivisionError:
    print("Entering into zero division error")
except ValueError:
    print("Entering into value error")
finally:
    print("Entering into finally  block")