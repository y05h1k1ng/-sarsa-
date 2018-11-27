from math import fabs
from game import Type

def view(Q):
    print('    | {0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14}'.format(Type(0).name, Type(1).name, Type(2).name, Type(3).name, Type(4).name, Type(5).name, Type(6).name, Type(7).name, Type(8).name, Type(9).name, Type(10).name, Type(11).name, Type(12).name, Type(13).name, Type(14).name))
    print('------------------------------------------------------------------')
    for i in range(15):
        print('{0} | '.format(Type(i).name), end = '')
        for j in range(15):
            if Q[i][j] == 0.0:
                print(' x ', end = ' ')
            elif fabs(Q[i][j] - 0.5) < 0.001:
                print(' ^ ', end = ' ')
            elif fabs(Q[i][j] - 1.0) < 0.001:
                print(' - ', end = ' ')
            elif fabs(Q[i][j] - 2.0) < 0.001:
                print(' o ', end = ' ')
            else:
                print(' ? ', end = ' ')
        print('')
