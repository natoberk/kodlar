def st_dev():
    global entry
    global sizeplt
    entry=[]
    sizeplt=[]
    variations=[]
    count = mean = total = totalvar = st_dev1 = variance = z_score = odd = even = coefficient= 0
    size =int(input("Enter number of days: "))
    while count<size:
        val = int(input("Please enter {}. day cases: ".format(count+1)))
        entry.append(val)
        count += 1
    print("\n")
    for i in entry:
        total += i
    mean = total/len(entry)
    print("Mean is: ", mean)
    for j in range(0,len(entry)):
        variations.append((entry[j]-mean)**2)
    for k in variations:
        totalvar += k
    variance = (float(totalvar/(len(entry))))
    st_dev1=variance**0.5
    coefficient=(st_dev1/mean)*100
    print("Variance is:",variance)
    print("Standard Deviation is:",st_dev1)
    print("Coefficient of Variation:",coefficient)
    for c in range(0,len(entry)):
        z_score = (entry[c]-mean)/st_dev1
        print("Z Score is {}. int:".format(c+1),z_score)
    if len(entry) % 2==1:
        odd = entry[len(entry) // 2] 
        print("Median is: ",odd)
    else:        
        even = (len(entry)+1) // 2
        print("Median is: ",(entry[even - 1] + entry[even])/2)
    for z in range(1,len(entry)+1):
        sizeplt.append(z)
    return entry
    return sizeplt
def graph():
    from matplotlib import pyplot as plt
    plt.plot(sizeplt,entry)
    plt.title("Turkey Covid-19 Daily Date Information")
    plt.xlabel("Day")
    plt.ylabel("Cases")
    plt.show()
def main():
    st_dev()
    graph()
main()