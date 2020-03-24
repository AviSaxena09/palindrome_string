string = input("Enter a String to check if palindrom posible : ")
palin_str = ''
odd_ele = ''
no_odd = 0
uni_elmnts = set(string)
for i in uni_elmnts:
    if (string.count(i))%2==1:
        no_odd+=1
        odd_ele = i
        string = string.replace(i,'')

if no_odd>1:
    print("Palindrom Not Possible")
else :
    item = (list(uni_elmnts))
    item.sort()
    for i in item:
        palin_str+= i*(string.count(i)//2)
    palin_str = palin_str+odd_ele+palin_str[::-1]
    print("Palindrom Possible")
    print("Palindrom String : ",palin_str)
