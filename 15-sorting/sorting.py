def basedOnLength(s):
    return len(s)
l_1 = ["rohid","king", "ayaan-ali"]
l_1.sort()
print(l_1)
l_1.sort(key=basedOnLength)
print(l_1)