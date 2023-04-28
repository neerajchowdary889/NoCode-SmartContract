import os

def filecreate():
    filename = 'SolSmartContract'
    i = 1
    while os.path.exists(filename):
            filename = f'SolSmartContract{i}'
            i += 1
    with open('created_dir.txt', 'w') as f:
          f.write(filename)
          f.close()
    return filename
obj = filecreate()
print(obj)