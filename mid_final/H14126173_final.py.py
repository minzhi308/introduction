def parse_matrix(matrix_str):
    """Parse a matrix input string into a dictionary representation."""
    rows = matrix_str.strip().split('|')
    matrix = {}
    i = 0
    for row in rows:
        elements = row.split(',')
        j = 0
        for elem in elements:
            matrix[(i, j)] = int(elem)
            j += 1
        i += 1
    return matrix, len(rows)

def matrix_multiply(U, V, n):
    """Multiply two matrices U and V of size n x n."""
    M = {}
    for i in range(n):
        for j in range(n):
            M[(i, j)] = 0
            for k in range(n):
                M[(i, j)] += U[(i, k)] * V[(k, j)]
    return M

def format_matrix(M, n):
    """Format the matrix dictionary into a string."""
    rows = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(str(M[(i, j)]))
        rows.append(','.join(row))
    return '|'.join(rows)

def main():
    # Get user input
    U_input = input("Enter matrix U: ")
    V_input = input("Enter matrix V: ")
    print("M = U x V")
    
    # Parse the matrices
    U, n = parse_matrix(U_input)
    V, _ = parse_matrix(V_input)
    
    # Perform matrix multiplication
    M = matrix_multiply(U, V, n)
    
    # Format the result matrix
    M_output = format_matrix(M, n)
    M_output = M_output.split('|') # ['10,5', '22,13']
    
    # Convert the comma-separated strings to lists of integers
    int_list = [int(x) for row in M_output for x in row.split(',')]
    
    # Split the result into two halves
    mid = len(int_list) // 2
    first_half = int_list[:mid]
    second_half = int_list[mid:]
    
    # Output the result
    print(first_half)
    print(second_half)

# Run the main function
if __name__ == "__main__":
    main()
