
def print_operation_table(operation, num_rows=9, num_columns=9):
    #print('\n'.join(['\t'.join([str(operation(i, j)) for j in range(1, num_columns + 1)]) for i in range(1, num_rows + 1)]))
    i=0
    j=0
    while i < num_rows:
        while j < num_columns:
            print(operation(i,j))
            j=j+1
        i=i+1
print_operation_table(lambda x,y:x*y)
