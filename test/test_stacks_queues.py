from src.stacks_queues import MaxStack

'''
Chapter 9: Stacks and Queues
'''
class TestMaxStack:
    def test_basic_configuration(self):
        '''
        Test basic incrementing list
        '''
        stack = MaxStack()
        for idx in xrange(1,11):
            stack.push(idx)
            assert idx == stack.get_max()

        for idx in xrange(10,0,-1):
            assert idx == stack.get_max()
            assert idx == stack.pop()

    def test_reverse_config(self):
        '''
        Reverse configuration
        '''
        stack = MaxStack()
        for idx in xrange(10,0,-1):
            stack.push(idx)
            assert 10 == stack.get_max()

        for _ in xrange(0,10):
            assert 10 == stack.get_max()
            stack.pop()
