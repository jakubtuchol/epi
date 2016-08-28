'''
Chapter 11: Heaps
'''

class Heap(object):
    def __init__(self, comp):
        self.heap_list = [0]
        self.cur_size = 0
        self.comp = comp

    def perc_up(self, i):
        while i // 2 > 0:
            if self.comp(self.heap_list[i], self.heap_list[i // 2]):
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.cur_size += 1
        self.perc_up(self.cur_size)

    def perc_down(self, i):
        while i * 2 <= self.cur_size:
            mc = self.min_child(i)
            if not self.comp(self.heap_list[i], self.heap_list[mc]):
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.cur_size:
            return i * 2

        if self.comp(self.heap_list[i * 2], self.heap_list[i * 2 + 1]):
            return i * 2
        return  i * 2 + 1

    def pop(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.cur_size]
        self.cur_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return retval

    def peek(self):
        return self.heap_list[1]

    def build_heap(self, alist):
        i = len(alist) // 2
        self.cur_size = len(alist)
        self.heap_list = [0] + alist[:]
        while i > 0:
            self.perc_down(i)
            i -= 1

def merge_sorted_arrays(arrs):
    # create min-heap
    heap = []
