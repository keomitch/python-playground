def hex_to_oct(hex_str):
  # library
  hex_chars = '0123456789abcdef'
  hex_binaries = [
    '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
    '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
  ]
  oct_binaries = [
    '000', '001', '010', '011', '100', '101', '110', '111'
  ]

  # hex_str to bin_str
  hex_str = hex_str.lower()
  bin_list = []
  for char in hex_str:
    if char not in hex_chars:
      raise ValueError(f'Invalid hex char "{char}"')
      return # exit when char is invalid
    bin_list.append(hex_binaries[hex_chars.index(char)])
  bin_str = ''.join(bin_list)

  # pad
  padding_length = (3 - (len(bin_str) % 3)) % 3
  padded_bin_str = '0' * padding_length + bin_str

  # padded_bin_str to oct_string
  bin_list = [padded_bin_str[i:i+3] for i in range(0, len(padded_bin_str), 3)]
  oct_list = [str(oct_binaries.index(bin_chunk)) for bin_chunk in bin_list]
  oct_string = ''.join(oct_list)

  # output
  return oct_string

print(hex_to_oct('z'))
