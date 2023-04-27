def filename():
    with open ('FileHistory.txt', 'r') as f:
        lines = f.readlines()
        last_line = lines[-1]
        f.close()
    return last_line
obj = filename()
print(obj)