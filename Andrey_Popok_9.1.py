class QueueError(IndexError):
    def __init__(self):
        IndexError.__init__(self)

class Queue:
    def __init__(self):
        self.__queue_list = []
    
    def elem_count_check(self):
        if len(self.__queue_list) > 0:
            return True
        else:
            raise QueueError

    def put(self, elem):
        self.__queue_list.insert(0,elem)
    
    def get(self):
        if self.elem_count_check():
            elem = self.__queue_list[-1]
            del self.__queue_list[-1]
            return elem

def main():
    que = Queue()
    que.put(1)
    que.put("dog")
    que.put(False)
    try:
        for i in range(4):
            print(que.get())
    except QueueError:
        print("Queue error")

main()
