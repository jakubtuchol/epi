'''
Chapter 11: Heaps
'''

class Heap(object):
    def __init__(self, comp):
        self._heap_list = [0]
        self._cur_size = 0
        self.comp = comp

    def _perc_up(self, i):
        while i // 2 > 0:
            if self.comp(self._heap_list[i], self._heap_list[i // 2]):
                tmp = self._heap_list[i // 2]
                self._heap_list[i // 2] = self._heap_list[i]
                self._heap_list[i] = tmp
            i = i // 2

    def _perc_down(self, i):
        while i * 2 <= self._cur_size:
            mc = self._min_child(i)
            if not self.comp(self._heap_list[i], self._heap_list[mc]):
                tmp = self._heap_list[i]
                self._heap_list[i] = self._heap_list[mc]
                self._heap_list[mc] = tmp
            i = mc

    def _min_child(self, i):
        if i * 2 + 1 > self._cur_size:
            return i * 2

        if self.comp(self._heap_list[i * 2], self._heap_list[i * 2 + 1]):
            return i * 2
        return  i * 2 + 1

    def insert(self, k):
        self._heap_list.append(k)
        self._cur_size += 1
        self._perc_up(self._cur_size)

    def pop(self):
        retval = self._heap_list[1]
        self._heap_list[1] = self._heap_list[self._cur_size]
        self._cur_size -= 1
        self._heap_list.pop()
        self._perc_down(1)
        return retval

    def peek(self):
        return self._heap_list[1]

    def build_heap(self, alist):
        i = len(alist) // 2
        self._cur_size = len(alist)
        self._heap_list = [0] + alist[:]
        while i > 0:
            self._perc_down(i)
            i -= 1

    def empty(self):
        return self._cur_size == 0

def merge_sorted_arrays(arrs):
    # create min-heap sorted on first element in tuple
    heap = Heap(lambda x,y: x[0] < y[0])

    # initialize heap with first value from each arr
    for idx,ls in enumerate(arrs):
        new_item = ls.pop(0)
        heap.insert((new_item, idx))

    output = []
    # keep pulling of elts from heap
    # and pushing new elts from same
    # list on, until have no elts in heap
    while not heap.empty():
        (val, idx) = heap.pop()
        output.append(val)
        if len(arrs[idx]):
            new_elt = arrs[idx].pop(0)
            heap.insert((new_elt, idx))

    return output
