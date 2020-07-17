'''
A Sample Program for testing Prime number
'''
def prime(num_ber):
    '''
    A Sample Program for testing Prime number
    '''
    if num_ber > 1:
        for i in range(2, num_ber):
            if(num_ber % i) == 0:
                print(num_ber, "is not a Prime Number")
                return num_ber
                break
        else:
            print(num_ber, "is Prime Number")
            return num_ber
    else:
        print(num_ber, "is not a Prime Number")
        return num_ber
