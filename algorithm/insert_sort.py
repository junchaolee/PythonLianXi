#coding:utf-8

if __name__ =='__main__':
    I=[54,26,93,17,77,31,44,55,20]

    def insert_sort(I):
        for i in range(len(I)):
            min_index=i
            for j in range(i+1,len(I)):
                if I[min_index]>I[j]:
                    min_index=j
                    tmp=I[i]
                    I[i]=I[min_index]
                    I[min_index]=tmp
            print(str(I))
        print("Result:"+str(I))

    insert_sort(I)
    print("insert_sort success!!!")
