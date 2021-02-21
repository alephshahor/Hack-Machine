def dec_to_bin(n_bit, dec_number):
    bin_str_format = "{0:0"+str(n_bit)+"b}"
    return bin_str_format.format(dec_number)

def dec_to_bin_arr(n_bit, dec_number):
    bin_str = dec_to_bin(n_bit, dec_number)
    bin_str_arr = list(bin_str)
    return [int(b_num) for b_num in bin_str_arr]

def bin_to_dec(bin_number):
    return int(bin_number, 2)
