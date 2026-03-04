# This program performs matrix multiplication of two matrices A and B, and prints the result.
def matrix_multiplication(A, B):
   # Check if the number of columns in A matches the number of rows in B
   if len(A[0]) != len(B):
      print("The width of matrix A must match the height of matrix B.")
   # Initialize the result matrix with zeros
   result = [[0 for i in range(len(B[0]))] for j in range(len(A))]
   # Perform matrix multiplication
   for i in range(len(A)):
   # Iterate through rows of A
      for j in range(len(B[0])):
      # Iterate through columns of B
         for k in range(len(B)):
         # Iterate through rows of B
            result[i][j] += A[i][k] * B[k][j]
   return result
# test
A = [
[1, 2, 3],
[4, 5, 6]
]
B = [
[7, 8],
[9, 10],
[11, 12]
]
result = matrix_multiplication(A, B)
print("Matrix A:")
for row in A:
   print(row)
   print("\nMatrix B:")
for row in B:
   print(row)
   print("\nDot Product (Result):")
for row in result:
   print(row)
