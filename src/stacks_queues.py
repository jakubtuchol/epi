'''
Chapter 9: Stacks and Queues
'''

class MaxStack(object):
    '''
    Question 9.1
    '''
    def __init__(self):
        self.contents = []
        self.max_at = [0]

    def push(self, elt):
        cur_max = self.max_at[-1]
        if cur_max >= elt:
            self.max_at.append(cur_max)
        else:
            self.max_at.append(elt)
        self.contents.append(elt)

    def pop(self):
        self.max_at.pop()
        return self.contents.pop()

    def get_max(self):
        return self.max_at[-1]
