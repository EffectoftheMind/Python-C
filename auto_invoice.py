print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print()

service1 = input("Select first service:\n")
service2 = input("Select second service:\n")
print()

services = ['Oil change', 'Tire rotation', 'Car wash', 'Car wax']

prices = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12}

print("Davy's auto shop invoice")
print()

if (service1 in services) and (service2 in services):
    print("Service 1:", str(service1) + ",", "$" + str(prices[service1]))
    print("Service 2:", str(service2) + ",", "$" + str(prices[service2]))
    print()
    print("Total:", "$" + str(int(prices[service1]) + int(prices[service2])))
elif (service1 == "-") and (service2 in services):
    print("Service 1:", "No service")
    print("Service 2:", str(service2) + ",", "$" + str(prices[service2]))
    print()
    print("Total:", "$" + str(prices[service2]))
elif (service1 in services) and (service2 == "-"):
    print("Service 1:", str(service1) + ",", "$" + str(prices[service1]))
    print("Service 2:", "No service")
    print()
    print("Total:", "$" + str(prices[service1]))
