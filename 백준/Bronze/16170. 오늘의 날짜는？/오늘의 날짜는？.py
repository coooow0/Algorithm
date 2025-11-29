from datetime import datetime

arr = datetime.now()
arr = str(arr)
arr = list(map(str, arr.split()))
arr = arr[0].replace('-', '\n')
print(arr)