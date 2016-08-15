'''
Chapter 11: Heaps
'''

class Heap(object):
    def __init__(self, comp):
        '''
        comp is function that is
        used for ranking values
        '''
        self.comp = comp
        self.contents = []
        self.num_elts = 0

    def add(self, elt):
        self.contents.append(elt)
        self.num_elts += 1

        self._swap_elts(0,-1)
        # rebalance

    def pop(self):
        '''
        Get root of heap, removin root
        from heap in process
        '''
        ret = self.peek()
        if self.num_elts > 1:
            self._rebalance()
        pass

    def peek(self):
        '''
        Get root of heap, allowing
        root to remain in heap
        '''
        if self.num_elts == 0:
            return None
        return self.contents[0]

    def _swap_elts(self, idx1, idx2):
        '''
        swaps specified elements
        '''
        self.contents[idx1] = self.contents[idx2],
            self.contents[idx2] self.contents[idx1]

    def _rebalance(self):
        '''
        Rebalance elements, starting
        from root
        '''
        root = self.contents[0]
        pass

    def _get_left_child(self, idx):
        return idx * 2 + 1

    def _get_right_child(self, idx):
        return idx * 2 + 2

def merge_sorted_arrays(arrs):
    # create min-heap
    heap = []
