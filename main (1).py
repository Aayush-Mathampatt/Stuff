global possible_characters
possible_characters = [' ','!', '"', '#', '$', '%','&',"'",'(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','[',"\\",']', '^', '_', '`','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']

def vernam(crypt_type,cipherplain_text):


  if crypt_type == "n":
     while True:
      nums = cipherplain_text.split()
      cipherplain_text = []
      try:
        for i in nums:
          cipherplain_text.append(int(i))
        break
      except:
        print("Input a list of integers with spacing inbetween if decrypting a vernam cipher")
        cipherplain_text  = input("Enter cipher/plain text:")
        continue
      

  while True:
    
    key = input("Enter a key:")

    if len(key) == len(cipherplain_text):
      break
    else:
      print("The key and code must be the same length.")
      continue

  binary_values = [[],
                   []]
  for char in key:
    binary_char = bin(ord(char))
    binary_values[0].append(binary_char.removeprefix("0b"))

  for char in cipherplain_text:
    if crypt_type == "y":
      binary_char = bin(ord(char))
    else:
      binary_char = bin(char)
    binary_values[1].append(binary_char.removeprefix("0b"))

  binary_results = []

  for binary in binary_values[0]:
    
    binary_xor = "0"
    
    value_bin_key = binary_values[0][binary_values[0].index(binary)]
    value_bin_code = binary_values[1][binary_values[0].index(binary)]
    
    index_count = 0

    while len(value_bin_key)<7:
      value_bin_key = "0" + value_bin_key

    while len(value_bin_code)<7:
      value_bin_code = "0" + value_bin_code

    for char in value_bin_key:
      
      if char != value_bin_code[index_count]:
        binary_xor = binary_xor + "1"
      else:
        binary_xor = binary_xor + "0"
      index_count = index_count + 1
      
    binary_results.append(binary_xor)

  vernam_results = []
  
  for value in binary_results:
    
    value_reversed = value[::-1]

    char_count = 0
    num_added = 1
    num_total = 0
    
    for char in value_reversed:

      if char == "1":
        num_total = num_total + num_added
      num_added = num_added*2

      char_count = char_count + 1
    vernam_results.append(num_total)

  if crypt_type == "y":
    
    final_result = ""
    for i in vernam_results:
      final_result  = final_result + str(i) + " "

  else:

    temp_list = []
    for i in vernam_results:
      temp_list.append(chr(i))
    final_result = ""
    for i in temp_list:
      final_result = final_result + i

  print("The result:")
  return final_result

def vigenerie(crypt_type,cipherplain_text):

  while True:
    
    key = input("Enter a key:")

    if len(key) == len(cipherplain_text):
      break
      
    else:
      print("The key needs to be the same length as what you want to be encrypted/decrypted.")
      continue
      
  move_list = []
  
  for char in key:
    
    move_list.append(possible_characters.index(char))

    new_message = ""
    
  for char in cipherplain_text:
    
    original_index = possible_characters.index(char)
        
    if crypt_type == "y":   

      new_char = int(original_index + move_list[cipherplain_text.index(char)])

      if new_char > 94:
        new_message = new_message + possible_characters[new_char-94]
      else:
        new_message = new_message + possible_characters[new_char]
      
    else:
      
      new_char = int(original_index - move_list[cipherplain_text.index(char)])
      
      if new_char<0:
        new_message = new_message + possible_characters[new_char+94]
      else:
        new_message = new_message + possible_characters[new_char]

  print("The result:")
  return new_message


def reverse(cipherplain_text):

  print("The result:")
  return cipherplain_text[::-1]

  
def caesar(crypt_type,cipherplain_text):
  
  while True:

    pos_or_neg = input("Is the shift positive(y/n):")
    if pos_or_neg.lower() != "y" and pos_or_neg.lower() != "n":
      continue
    else:
      break  

  if pos_or_neg.lower() == crypt_type.lower():
    direction = "up"
  else:
    direction = "down"
    
  while True:
    
    try:   
      shift = int(input("Enter shift value:"))
      if shift < 0 or shift>999:
        print("A positive number under 1000 is needed.")
        continue
      else:
        break
        
    except:
      print("Enter an integer.")
      continue
  
  new_message = ""
  
  for char in cipherplain_text:
    
    if direction == "up":
        
      new_index = possible_characters.index(char) + shift
      amount_over = int(new_index/95)
    else:
      new_index = possible_characters.index(char) - shift
      amount_over = int((new_index/95)*(-1))
       
    if new_index<0:

      new_message = new_message + possible_characters[new_index + 95 + (amount_over*95)]
        
    elif new_index > 94:
      new_message = new_message + possible_characters[new_index  - (amount_over*95)]  
          
    else:
      new_message = new_message + possible_characters[new_index]  

  print("The result:")
  return new_message


def choose(option):
  
  while True:

    crypt_type = input("Do you want to encrypt or decrypt the data(y/n - y for encrypt and n for decrypt):")
      
    if crypt_type.lower() != "y" and crypt_type.lower() != "n":
      continue

    cipherplain_text = input("Enter cipher/plain text:")
    
    if option == 1:
      print(caesar(crypt_type,cipherplain_text))
      main()
        
    elif option == 2:
      print(reverse(cipherplain_text))
      main()
        
    elif option == 3:
      print(vigenerie(crypt_type,cipherplain_text))
      main()
        
    elif option == 4:
      print(vernam(crypt_type,cipherplain_text))
      main()
        
    break


def main():
  
  print("Choose an option (the option number):")
  print("1.Shift cipher")
  print("2.Reverse cipher")
  print("3.Vigenerie cipher")
  print("4.Vernam cipher")
  print("5.Quit")
  print("Note: Ciphers are using vsible ASCII characters only. ")
  
  while True:
    
    try:
      
      option = int(input("Enter the number here:"))
      
      if option>5 or option<1:
        print("Enter a value in the range.")
        continue
        
      else:
        break
        
    except:
      print("Enter the right data type (an integer).")
      continue
    
  if option == 5:
    print("Bye.")

  elif option !=5:
    choose(option)
      



main()