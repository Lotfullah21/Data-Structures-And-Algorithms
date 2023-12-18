for outer_loop in range(3):
    print("Outer Loop Iteration:", outer_loop + 1)
    
    for i in range(1, 11):
        if i == 2:
            print("  Skipping i =", i)
            continue
        elif i == 10:
            print("  Breaking at i =", i)
            break
        print("  Inner Loop Iteration:", i)

print("End of Program")
