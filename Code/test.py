def tester():
    for i in range(5):
        print(i)
    return True

loginTrue = False
while not loginTrue:
    loginTrue = tester()
print("out")