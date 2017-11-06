#coding:utf-8

if __name__ =='__main__':
    I=[4,1,9,13,34,26,10,7,4]

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
