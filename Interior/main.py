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



def Interior(C : list, A : list[list], b : list, x_0 : list, alpha : float, eps : float) -> None:
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
    
    print("the last iteration vector:\n", x)

    res = 0
    for i in range(len(C)):
        res += C[i] * x[i]
    
    print("answer:", res)
        
    
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
    # x_0 = [ 1/2, 7/2, 1, 2 ]
    # alpha = 0.5
    # epsilon = 0.0001
    # Interior(C=C, A=A, b=b, x_0=x_0, alpha=alpha, eps=epsilon)
    # OUTPUT
    # the last iteration vector:
    #  [
    #   5.99995001e+00
    #   1.00002143e+00
    #   1.42838248e-05
    #   1.42838248e-05
    #  ]
    #  answer: 6.999971433492358

    # Test 2 not complited yet
    # Problem 1.2 from ALi lab 6
    # manimize F(x1, x2) = x1 + x2
    # z = -x1 - x2
    # subject to
    # 2x1 + 4x2 ≤ 16, (1)
    # x1 + 3x2 ≥ 9, (2)
    # x1 ≥ 0, (3)
    # x2 ≥ 0 (4)
    # be provided soon....

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
    # alpha = 0.5
    # epsilon = 0.0001
    # Interior(C=C, A=A, b=b, x_0=x_0, alpha=alpha, eps=epsilon)
    # OUTPUT
    #  the last iteration vector:
    #  [
    #   2.96713352e-06 
    #   7.99999110e+00 
    #   2.00000009e+01 
    #   6.67605042e-05
    #   8.90140056e-06 
    #   9.60000086e+01
    # ]
    # answer: 399.9999522676773

if __name__ == "__main__":
    main()