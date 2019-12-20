#coding:utf-8
lists=[49,38,65,97,76,13,27,49,55,4]

def shell_sort(lists):
    count=len(lists)
    step=2
    group=count/step

    while group>0:
        for i in range(group):
            j=i+group
            while j<count:
                key=lists[j]
                k=j-group
                while k>=0:
                    if lists[k]>key:
                        lists[k+group]=lists[k]
                        lists[k]=key
                    k=k-group
                j=j+group
            print str(lists)
        group=group/step
    return lists
shell_sort(lists)



