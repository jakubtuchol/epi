from src.stacks_queues import MaxStack, evaluate_rpn

'''
Chapter 9: Stacks and Queues
'''
class TestMaxStack(object):
    '''
    Question 9.1
    '''
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

class TestRpnEvaluation(object):
    '''
    Question 9.2
    '''
    def test_singleton(self):
        '''
        Test singleton evaluation
        '''
        assert 1729 == evaluate_rpn(['1729'])

    def test_operation(self):
        '''
        Test simple operation
        '''
        assert 738 == evaluate_rpn(['6','123','*'])

    def test_complex_operation(self):
        '''
        Test complex operation
        '''
        assert 15 == evaluate_rpn(['3','4','+','2','*','1','+'])

    def test_division_operation(self):
        '''
        Test complex division operation
        '''
        assert 80 == evaluate_rpn(['8','64','/','640','/'])
