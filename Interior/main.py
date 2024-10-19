import numpy as np
from numpy import diag, dot, eye, transpose, subtract, absolute, add, ones
from numpy.linalg import inv, norm

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
        print("in the iteration", count, "vector is:\n ", x, "\n")
        count += 1

        if count > 300:
            print("the problem is unsolvable or try another initiail solution!")
            return 
    
    print("the last iteration vector:\n", x)

    res = 0
    for i in range(len(C)):
        res += C[i] * x[i]
    
    print("answer:", res if result == "max" else -1 * res)
        
    
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
    # Interior(C=C, A=A, b=b, x_0=x_0)
    # OUTPUT
    # the last iteration vector:
    #  [
    #   5.99995001e+00
    #   1.00002143e+00
    #   1.42838248e-05
    #   1.42838248e-05
    #  ]
    #  answer: 6.999971433492358


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
    # Interior(C=C, A=A, b=b, x_0=x_0, result = "min")
    # OUTPUT
    # the last iteration vector:
    #  [
    #   1.70625437e-06 
    #   3.00000057e+00 
    #   3.99999431e+00 
    #   3.41250874e-06
    #  ]
    # answer: 3.0000022764013425


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
    # Interior(C=C, A=A, b=b, x_0=x_0)
    # OUTPUT
    #  the last iteration vector:
    #  [
    #   2.96713352e-06 
    #   7.99999110e+00 
    #   2.00000009e+01 
    #   6.67605042e-05
    #   8.90140056e-06 
    #   9.60000086e+01
    #  ]
    # answer: 399.9999522676773


    # 4 not complited yet
    # max z = 10*x1 + 20*x2
    # subject to the constraints:
    # -1*x1 + 2*x2 <= 15
    # 1*x1 + 1*x2 <= 12
    # 5*x1 + 3*x2 <= 45
    # C = [10, 20, 0, 0, 0]
    # A = [
    #         [-1, 2, 1, 0, 0],
    #         [1, 1, 0, 1, 0], 
    #         [5, 3, 0, 0, 1]
    #     ]
    # b = [15, 12, 45]
    # x_0 = [1, 1, 0, 0, 0]
    # Interior(A=A, C=C, b=b, x_0=x_0)


if __name__ == "__main__":
    main()