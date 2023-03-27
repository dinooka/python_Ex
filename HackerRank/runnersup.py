if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    sort_arr = sorted(arr)
    count = len(sort_arr)   
    
    max = sort_arr[count-1]   
    for i in range(0,(count)):             
        if  sort_arr[i]!=max:
            new_list = [None]*(count)
            new_list[i] = sort_arr[i]

    for j in range(0,(len(new_list)-1)):        
        if new_list[j] != None:
            print(new_list[j])
  
      


        
    

        