''' This application is in Python 3.
 and created by Christina Smithers.

 The first half of the program encodes
 numbers and the latter half decodes.

 The final output is stored in a text file.

'''
from struct import pack

input_integers_list = [6111, 340, -2628, -25, 7550]
new_integers_list = []
hexed_intermediate_number_list = []
new_hexed_list = []
stringified_hex_list = []

# Greet the user
print ("Hello there. Let's encode some numbers.")
print ("\nHere's what I have: ")
print (input_integers_list)



# Add 8192 to the input integer so its range is translated to [0..16383]
print ("\nLet's scale to make conversion easier:")
for index, integer_value in enumerate(input_integers_list):
    new_integers_list.append(integer_value + 8192)

# Splitting up into bytes then stuffing those into a list
print ("\nNow I'll translate the range to pack it into bytes with a little magic...")
for index, new_integer_value in enumerate (new_integers_list):
	hexed_intermediate_number_list = [((new_integer_value << 16) | (new_integer_value >> 16)) for new_integer_value in new_integers_list]
	#Now that everything is in bytes, let's make it into hex
	for index, byte in enumerate (new_integers_list):
		hexed_intermediate_number = hex(byte)
		hexed_intermediate_number_list.append(hexed_intermediate_number)
		# Slice off the non-hex part
		new_hexed_list = hexed_intermediate_number_list[5:]

# Turn that hex into string
for index, hex_value in enumerate (new_hexed_list):
	stringified_hex_list.append(hex_value)
	hex_string = ' '.join(str(item) for item in stringified_hex_list)

	with open('ConvertedData.txt', 'w') as outfile:
		outfile.write(hex_string)