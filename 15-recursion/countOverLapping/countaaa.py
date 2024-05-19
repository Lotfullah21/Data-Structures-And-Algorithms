def countaaaNonOverlapping(st, idx, count):
    # non-over lapping
    if idx >= len(st) - 2:
        return count
    if st[idx] == 'a' and st[idx] == st[idx + 1] and st[idx + 1] == st[idx + 2]:
        temp = countaaaNonOverlapping(st, idx + 3, count + 1)
        return temp
    else:
        temp = countaaaNonOverlapping(st, idx + 1, count)
        return temp
# over lapping
def countaaaOverlapping(st, idx, count):
    if idx == len(st) - 2:
        return count
    if st[idx] == 'a' and st[idx] == st[idx + 1] and st[idx + 1] == st[idx + 2]:
        temp = countaaaOverlapping(st, idx + 1, count + 1)
        return temp
    else:
        temp = countaaaOverlapping(st, idx + 1, count)
        return temp

if __name__ == "__main__":
    st = input("Enter a string: ")

    print(countaaaOverlapping(st, 0, 0))
    print(countaaaNonOverlapping(st, 0, 0))
