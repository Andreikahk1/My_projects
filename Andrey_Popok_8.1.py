class Stack:
    def __init__(self):
        self.__stack_list = []
    
    def push(self, val):
        self.__stack_list.append(val)
    
    def pop (self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

class CountingStack (Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__incoming_count = 0
    
    def get_counter(self):
        return self.__incoming_count

    def pop(self):
        val = Stack.pop(self)
        self.__incoming_count += 1
        return val

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())