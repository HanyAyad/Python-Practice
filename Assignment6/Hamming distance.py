def hamming(s1,s2):
    count=0
    if len(s1)!=len(s2):
        return -1
    for i in range(0,len(s1)):
        if(s1[i]!=s2[i]):
            count+=1
    return count

if __name__=="__main__":
    print(hamming("lol","non"))
    