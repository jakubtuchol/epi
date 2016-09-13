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

    def size(self):
        return self._cur_size

def merge_sorted_arrays(arrs):
    '''
    Question 11.1: merge n sorted arrays
    '''
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


def almost_sorted(ls, k):
    '''
    Question 11.3: Sort an almost-sorted array,
    where all elements are within k elements of being sorted
    '''
    heap = Heap(lambda x,y: x < y)
    res = []

    for idx, val in enumerate(ls):
        heap.insert(val)
        if idx - k >= 0:
            res.append(heap.pop())

    while not heap.empty():
        res.append(heap.pop())

    return res


def find_closest_stars(limit, stars):
    '''
    Question 11.4: Find k closest stars
    to a location
    '''
    # create max heap to handle keeping
    # track of closest stars
    heap = Heap(lambda x,y: x > y)

    for star in stars:
        heap.insert(star)

        if heap.size() > limit:
            heap.pop()

    closest_stars = []
    while not heap.empty():
        closest_stars.append(heap.pop())

    return closest_stars
