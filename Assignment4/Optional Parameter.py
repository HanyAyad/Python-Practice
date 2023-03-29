def loop(number, debug=False):
    result=[i for i in range(1,number+1)]
    if debug:
        print("#Start Loop")
        print(result)
        print("#End Loop")
    else:
        return result
        

if __name__ =="__main__":
    print (loop(5, debug=False))
