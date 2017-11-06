# coding:utf8
queue = []

def enq():
    queue.append(raw_input('请输入你的内容:').strip())

def deq():
    if len(queue) == 0:
        print '***不能从一个空队列中删除任何元素***'
    else:
        print '删除[', queue.pop(0), ']'

def viewq():
    print queue

CMDs = {'e': enq, 'd': deq, 'v': viewq}

def showmenu():
    pr= """
    (E)增加
    (D)删除
    (V)打印
    (Q)退出
    请输入你的选择:
    """
    while True:
        while True:
            try:
                choice=raw_input(pr).strip()[0].lower()
            except(EOFError, KeyboardInterrupt, IndexError):
                choice='q'
            print '\n你选择的是:[%s]' % choice
            if choice not in 'devq':
                print '选择错误，请重试'
            else:
                break

        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    showmenu()




