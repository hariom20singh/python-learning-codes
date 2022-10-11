def divid(a , divisor):
    try:
        return a/divisor
    except ZeroDivisionError as e:
        print('Divisor never be Zero !! Error Divide Terminating')
    finally:
        print('$$$$ divide successful $$$$')

print(divid(34,1))
print('program end.')