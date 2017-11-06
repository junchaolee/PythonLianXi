# coding:utf8

# define a  list to store stack
stack=[]

def push_it():
    stack.append(raw_input('请输入字符串').strip())

def pop_it():
    if len(stack)==0:
        print '***不能从一个空栈删除元素***'
    else:
        print '删除[',stack.pop(),']'

def view_stack():
    print stack   #calls str() internally

CMDs={'u':push_it,'o':pop_it,'v':view_stack}

def show_menu():
    pr="""
    (U)进栈
    (O)出栈
    (V)查看
    (Q)退出
    请输入你的选择:
    """
    while True:
        while True:
            try:
                choice=raw_input(pr).strip()[0].lower()
            except(EOFError,KeyboardInterrupt,IndexError):
                choice='q'

            print '\n你选择的是:[%s]'%choice
            if choice not in 'uovq':
                print '***无效选项***'
            else:
                break
        if choice=='q':
            break
        CMDs[choice]()

if __name__=='__main__':
    show_menu()