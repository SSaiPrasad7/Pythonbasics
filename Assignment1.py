def ask():
    while True:
        try:
            i=int(input("Enter a value"))
        except:
            print("Not a integer")
            continue
        else:
            print(i**2)
            break


if __name__=='__main__':
    try:
        ask()
        x = 5
        y = 0
        z = x / y
        for i in ['a', 'b', 'c']:
            print(i ** 2)
    except ZeroDivisionError:
        print("cannot be divide by zero")
    except:
        print("error")
    else:
        print(z)
    finally:
        print("All Done")