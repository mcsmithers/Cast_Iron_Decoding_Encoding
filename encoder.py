''' This application is in Python 3.
 and created by Christina Smithers.

 The first half of the program encodes
 numbers and the latter half decodes.

 The final output is stored in a text file.

'''
from struct import pack

# Going to use lists to store all the values through various points 
input_integers_list = [6111, 340, -2628, -25, 7550]
new_integers_list = []
hexed_intermediate_number_list = []
new_hexed_list = []
stringified_hex_list = []
exercise_hex_list = ["0A0A", "0029", "3F0F", "4400", "5E7F"]
exercise_hex_list_tranformed = []

# Greet the user
print ("Hello there. Let's encode some numbers.")
print ("\nHere's what I have: ")
print (input_integers_list)

# Add 8192 to the input integer so its range is translated to [0..16383]
print ("\nLet's scale to make conversion easier...")
for index, integer_value in enumerate(input_integers_list):
    new_integers_list.append(integer_value + 8192)
print (new_integers_list)

# Splitting up into bytes then stuffing those into a list
print ("\nNow I'll translate the range to pack it into bytes with a little magic to give us some hex numbers:")
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
print (hex_string)

# Write the list into a text file
thefile = open('ConvertedData.txt', 'w')
for item in hex_string:
  thefile.write("%s" % item)


# Let's do the opposite now
print ("\nFor my last trick, I am going to do the opposite and turn a hex string into an integer:")
for (index, string_hex_value) in enumerate (exercise_hex_list):
	hex_to_int = int(string_hex_value, 16)
	hex_string_to_hex = hex(hex_to_int)
	final_number = str(int(hex_string_to_hex, 16))
	exercise_hex_list_tranformed.append(final_number)
print (exercise_hex_list_tranformed)

# Write this one to a text file too
for item in exercise_hex_list_tranformed:
  thefile.write("\n%s " % item)


print ("\nAnd I even made all the conversions write into a text file called '%s.'  That's all for now.  Hope you enjoyed the rabbit-free magic show." % thefile.name)
