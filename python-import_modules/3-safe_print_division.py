#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    except Exception as e:
        return None
    else:
        print("Inside result: {}".format(result))
    finally:
        return result