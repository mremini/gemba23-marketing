def count_zeros(my_array):
    nbr_zero=0
    for row in my_array:
        for cell in row:
            if cell==0:
               nbr_zero=nbr_zero+1
    return nbr_zero