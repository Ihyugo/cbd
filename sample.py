class sample:
    sum=0.0
    total=0.0
    for i in range(10000000):
        sum=2*i+1
        if i%2 == 0:
            total += 1/sum
        else:
            total -= 1/sum

    print(4*total)
