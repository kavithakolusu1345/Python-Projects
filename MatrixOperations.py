import numpy as np

def get_matrix(name):
    rows = int(input(f"Enter rows for Matrix {name}: "))
    cols = int(input(f"Enter columns for Matrix {name}: "))

    print(f"Enter elements for Matrix {name}:")
    matrix = []

    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            raise ValueError("Incorrect number of elements.")
        matrix.append(row)

    return np.array(matrix)

print("===== MATRIX OPERATIONS TOOL =====")

try:
    A = get_matrix("A")
    B = get_matrix("B")

    while True:
        print("\nChoose Operation")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose")
        print("5. Determinant")
        print("6. Inverse")
        print("7. Rank")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\nResult:")
            print(A + B)

        elif choice == "2":
            print("\nResult:")
            print(A - B)

        elif choice == "3":
            print("\nResult:")
            print(np.dot(A, B))

        elif choice == "4":
            print("\nTranspose of Matrix A:")
            print(A.T)

        elif choice == "5":
            if A.shape[0] == A.shape[1]:
                print("\nDeterminant:")
                print(np.linalg.det(A))
            else:
                print("Determinant requires a square matrix.")

        elif choice == "6":
            if A.shape[0] == A.shape[1]:
                print("\nInverse:")
                print(np.linalg.inv(A))
            else:
                print("Inverse requires a square matrix.")

        elif choice == "7":
            print("\nRank:")
            print(np.linalg.matrix_rank(A))

        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

except Exception as e:
    print("Error:", e)