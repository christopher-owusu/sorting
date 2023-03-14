

# def sort(data):
data = [3,1,5,2,7,0,6]
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if (data[j] < data[i]): # for decending order data[i] < data[j]
            data[i], data[j] = data[j], data[i]
print(data)


    