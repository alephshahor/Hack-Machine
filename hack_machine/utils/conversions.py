

def dec_to_bin(n_bit, dec_number):
    bin_str_format = "{0:0"+str(n_bit)+"b}"
    return bin_str_format.format(dec_number)