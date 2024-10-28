import numpy as np
from numpy import diag, dot, eye, transpose, subtract, absolute, add, ones
from numpy.linalg import inv, norm
from simplex import solve_llp as simplex_from_previous_assignment

def compute_p(n : int, A_telda):
    #identity matrix
    I = eye(n)
    #A'A'^T
    AtAtt = dot(A_telda, transpose(A_telda))
    #(A'A'^T)^-1
    AtAttMO = inv(AtAtt)
    #A'^T(A'A'^T)^-1
    TEMP = dot(transpose(A_telda), AtAttMO)
    #A'^T(A'A'^T)^-1A;
    Full_A = dot(TEMP, A_telda)

    # I - A'^T(A'A'^T)^-1A;
    return subtract(I, Full_A) 



def Interior(C : list, A : list[list], b : list, x_0 : list, 
             alpha : float = 0.5, eps : float = 0.00001, result : bool = "max") -> None:
    
    if (result != "max"):
        C = [-1 * x for x in C]
    x = x_0.copy()
    count = 1
    while(1):
        D = diag(x)
        A_telda = dot(A, D)
        C_telda = dot(D, C)
        
        P = compute_p(n=len(C), A_telda=A_telda)

        C_p = dot(P, C_telda)
        v =  absolute(np.min(C_p))
        X_telda = add(ones(len(C), float), alpha/v * C_p)

        X_star = dot(D, X_telda)

        if norm(subtract(X_star, x), ord=2) < eps:
            x = X_star
            break

        x = X_star
        # print("in the iteration", count, "vector is:\n ", x, "\n")
        count += 1

        if count > 300:
            print("the problem is unsolvable or try another initiail solution!")
            return 
    
    print("the last iteration vector:\n", x)

    res = 0
    for i in range(len(C)):
        res += C[i] * x[i]
    
    print("alpha = ", alpha, "answer:", res if result == "max" else -1 * res)
        
    
def main():
    pass

    # MESSAGE FOR DEAR GUYS FROM MY AWESOME TEAM
    # I LOVE YOU
    
    # Test 1
    # Problem 1.1 from Ali lab 6
    # maximize F(x1, x2) = x1 + x2
    # subject to
    # 2x1 + 4x2 ≤ 16, (1)
    # x1 + 3x2 ≥ 9, (2)
    # x1 ≥ 0, (3)
    # x2 ≥ 0 (4)
    # CODE 
    # C = [1, 1, 0, 0]
    # A = [
    #         [2, 4, 1, 0],
    #         [1, 3, 0, -1]
    #     ]
    # b = [
    #     16,
    #     9
    # ]
    # x_0 = [ 1/2, 7/2, 1, 2]
    # Interior(C=C, A=A, b=b, x_0=x_0, alpha=0.5)
    # Interior(C=C, A=A, b=b, x_0=x_0, alpha=0.9)
    # print("simplex from previous assignment result: ")
    # simplex_from_previous_assignment(C, A, b)
    #
    # OUTPUT
    #  the last iteration vector:
    # [
    #   5.99999375e+00
    #   1.00000267e+00 
    #   1.78547810e-06
    #   1.78547810e-06
    # ]
    # alpha =  0.5 answer: 6.9999964238601855
    #
    # the last iteration vector:
    #  [
    #   5.99999779e+00
    #   1.00000086e+00
    #   9.58553224e-07
    #   3.77264613e-07
    #  ]
    # alpha =  0.9 answer: 6.999998653833897
    #
    # simplex from previous assignment result: 
    # METHOD IS NOT APPLICABLE DUE TO >= IN CONSTRAINS !!



    # Test 2 
    # Problem 1.2 from ALi lab 6
    # minimize F(x1, x2) = x1 + x2
    # z = -x1 - x2
    # subject to
    # 2x1 + 4x2 ≤ 16, (1)
    # x1 + 3x2 ≥ 9, (2)
    # x1 ≥ 0, (3)
    # x2 ≥ 0 (4)
    # CODE 
    # C = [1, 1, 0, 0]
    # A = [
    #         [2, 4, 1, 0],
    #         [1, 3, 0, -1]
    #     ]
    # b = [
    #     16,
    #     9
    # ]
    # x_0 = [ 1/2, 7/2, 1, 2 ]
    # Interior(C=C, A=A, b=b, x_0=x_0, alpha=0.5, result="min")
    # Interior(C=C, A=A, b=b, x_0=x_0, alpha=0.9, result="min")
    # print("simplex from previous assignment result: ")
    # simplex_from_previous_assignment(C, A, b, res="min")
    # Output
    # the last iteration vector:
    #  [
    #   1.70625437e-06
    #   3.00000057e+00
    #   3.99999431e+00
    #   3.41250874e-06
    #  ]
    # alpha =  0.5 answer: 3.0000022764013425
    #
    # the last iteration vector:
    #  [
    #   5.87024599e-07
    #   3.00000080e+00
    #   3.99999563e+00
    #   2.98268467e-06
    #  ]
    # alpha =  0.9 answer: 3.000001384187187
    #
    # simplex from previous assignment result: 
    # METHOD IS NOT APPLICABLE DUE TO >= IN CONSTRAINS!!


    # Test 3
    # Problem 2 from Ali lab 6
    # maximize z = 9x_1 + 10x_2 + 16x_3 
    # subject to 
    # 18x1 + 15x2 + 12x3 ≤ 360, (1)
    # 6x1 + 4x2 + 8x3 ≤ 192, (2)
    # 5x1 + 3x2 + 3x3 ≤ 180, (3)
    # x1 ≥ 0, (4)
    # x2 ≥ 0, (5)
    # x3 ≥ 0. (6)   
    # CODE
    # C = [9, 10, 16, 0, 0, 0]
    # A = [
    #         [18, 15, 12, 1, 0, 0],
    #         [6, 4, 8, 0, 1, 0],
    #         [5, 3, 3, 0, 0, 1]
    #     ]
    # b = [
    #     360,
    #     192,
    #     180
    # ]
    # x_0 = [1, 1, 1, 315, 174, 169]
    # Interior(C=C, A=A, b=b, x_0=x_0, alpha=0.5)
    # # Interior(C=C, A=A, b=b, x_0=x_0, alpha=0.9)
    # print("simplex from previous assignment result: ")
    # simplex_from_previous_assignment(C, A, b) 
    # OUTPUT
    #  the last iteration vector:
    #  [
    #   3.70891690e-07
    #   7.99999910e+00
    #   2.00000003e+01
    #   8.34506302e-06
    #   1.11267507e-06
    #   9.60000013e+01
    #  ]
    # alpha =  0.5 answer: 399.9999983350454
    #
    # alpha = 0.9 answer: numpy.linalg.LinAlgError: Singular matrix exception
    #
    # simplex from previous assignment result: 
    # max z = 9*x1 + 10*x2 + 16*x3 + 0*x4 + 0*x5 + 0*x6 
    # subject to the constraints:
    # 18*x1 + 15*x2 + 12*x3 + 1*x4 + 0*x5 + 0*x6 <= 360
    # 6*x1 + 4*x2 + 8*x3 + 0*x4 + 1*x5 + 0*x6 <= 192
    # 5*x1 + 3*x2 + 3*x3 + 0*x4 + 0*x5 + 1*x6 <= 180
    # 400.0
    # [0, 8.0, 20.0, 0, 0, 0]


    # 4 Problem
    # max z = 10*x1 + 20*x2
    # subject to the constraints:
    # -1*x1 + 2*x2 <= 15
    # 1*x1 + 1*x2 <= 12
    # 5*x1 + 3*x2 <= 45
    # CODE
    # C = [10, 20, 0, 0, 0]
    # A = [
    #         [-1, 2, 1, 0, 0],
    #         [1, 1, 0, 1, 0], 
    #         [5, 3, 0, 0, 1]
    #     ]
    # b = [15, 12, 45]
    # x_0 = [1, 1, 14, 10, 37]
    # Interior(C=C, A=A, b=b, x_0=x_0, alpha=0.5)
    # Interior(C=C, A=A, b=b, x_0=x_0, alpha=0.9)
    # print("simplex from previous assignment result: ")
    # simplex_from_previous_assignment(C, A, b) 
    #
    # OUTPUT
    #  the last iteration vector:
    #  [
    #   3.00000076e+00
    #   8.99999788e+00
    #   4.76837158e-06
    #   1.19209290e-06
    #   3.00000199e+00
    #  ]
    # alpha =  0.5 answer: 209.9999652452779
    #
    # the last iteration vector:
    #  [
    #   2.99999977e+00
    #   8.99999868e+00
    #   4.27428187e-07
    #   2.71566561e-07
    #   3.00000089e+00
    #  ]
    # alpha =  0.9 answer: 209.9999713325084
    #
    # simplex from previous assignment result: 
    # max z = 10*x1 + 20*x2 + 0*x3 + 0*x4 + 0*x5 
    # subject to the constraints:
    # -1*x1 + 2*x2 + 1*x3 + 0*x4 + 0*x5 <= 15
    # 1*x1 + 1*x2 + 0*x3 + 1*x4 + 0*x5 <= 12
    # 5*x1 + 3*x2 + 0*x3 + 0*x4 + 1*x5 <= 45
    # 210.0
    # [3.0, 9.0, 0, 0, 0]


    # 5 Problem
    # max z = 7*x1 + 5*x2 + 3*x3
    # subject to the constraints:
    # 2*x1 + 3*x2 + 1*x3 <= 15
    # 4*x1 + 1*x2 + 2*x3 <= 25
    # 3*x1 + 2*x2 + 4*x3 <= 30
    # Code
    # C = [7, 5, 3, 0, 0, 0]
    # A = [
    #       [2, 3, 1, 1, 0, 0], 
    #       [4, 1, 2, 0, 1, 0],
    #       [3, 2, 4, 0, 0, 1]
    #     ]
    # b = [
    #       15, 
    #       25, 
    #       30
    #     ]
    # x_0 = [1, 1, 1, 9, 19, 21]
    # Interior(C=C, A=A, b=b, x_0=x_0, alpha=0.5)
    # Interior(C=C, A=A, b=b, x_0=x_0, alpha=0.9)
    # print("simplex from previous assignment result: ")
    # simplex_from_previous_assignment(C, A, b) 
    #
    # Output
    #  the last iteration vector:
    #  [
    #   6.29999819e+00
    #   7.99999816e-01
    #   2.56229555e-06
    #   9.85498289e-07
    #   1.16467980e-06
    #   9.49999462e+00
    #  ]
    # alpha =  0.5 answer: 48.09999409751068
    #
    # the last iteration vector:
    #  [
    #   6.30000015e+00
    #   7.99999920e-01
    #   8.61225235e-07
    #   2.08653501e-07
    #   1.60843782e-07 
    #   9.49999798e+00
    # ]
    # alpha =  0.9 answer: 48.100003217663385
    #
    # simplex from previous assignment result: 
    # max z = 7*x1 + 5*x2 + 3*x3 + 0*x4 + 0*x5 + 0*x6 
    # subject to the constraints:
    # 2*x1 + 3*x2 + 1*x3 + 1*x4 + 0*x5 + 0*x6 <= 15
    # 4*x1 + 1*x2 + 2*x3 + 0*x4 + 1*x5 + 0*x6 <= 25
    # 3*x1 + 2*x2 + 4*x3 + 0*x4 + 0*x5 + 1*x6 <= 30
    # 47.0
    # [6.0, 1.0, 0, 0, 0, 0]

   


if __name__ == "__main__":
    main()