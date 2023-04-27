import os

def filecreate():
    filename = 'SolSmartContract'
    i = 1
    while os.path.exists(filename):
            filename = f'SolSmartContract{i}'
            i += 1
    return filename
obj = filecreate()
print(obj)