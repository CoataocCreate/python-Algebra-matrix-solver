#Python Algebra Equation Solver
def solve_equation(insert: str):
    num1 = int(insert[0])
    num2 = int(insert[5])
    num3 = int(insert[9:])
    print("")
    print(f"First Extract {num2} from {num3} then you have {num3 - num2} then divide {num3 - num2} from {num1} and you have")
    afterminus = num3 - num2
    result = (afterminus / num1)
    print("x :",result)
    print("")

#Python Matrix Add Function 
def plus_matrix(matrix0, matrix1):
    m1n1 = matrix0[0]; m1n2 = matrix0[1]; m1n3 = matrix0[2]; m1n4 = matrix0[3]
    m1n5 = matrix0[4]; m1n6 = matrix0[5]; m1n7 = matrix0[6]; m1n8 = matrix0[7]
    m1n9 = matrix0[8]
    
    m2n1 = matrix1[0]; m2n2 = matrix1[1]; m2n3 = matrix1[2]; m2n4 = matrix1[3]
    m2n5 = matrix1[4]; m2n6 = matrix1[5]; m2n7 = matrix1[6]; m2n8 = matrix1[7]
    m2n9 = matrix1[8]
    
    plus = [[m1n1 + m2n1, m1n2 + m2n2, m1n3 + m2n3],
            [m1n4 + m2n4, m1n5 + m2n5, m1n6 + m2n6],
            [m1n7 + m2n7, m1n8 + m2n8, m1n9 + m2n9]]
    
    print(plus[0])
    print(plus[1])
    print(plus[2])
    