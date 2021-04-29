# Kevin Nguyen
# Caesar Cipher Python Application

from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#function to encrypt secret message
def encrypt(user_input, shift_amount):
  decoded_message = "";
  for i in range(0,len(user_input)):
    temp = alphabet.index(user_input[i]);
    temp += shift_amount;
    decoded_message += alphabet[temp%26];
  print(f"The encoded message is {decoded_message}")

#function to decrypt secret message
def decrypt(user_input, shift_amount):
  encoded_message = "";
  for i in range(0,len(user_input)):
    temp = alphabet.index(user_input[i]);
    temp -= shift_amount;
    if temp < 0:
      encoded_message += alphabet[temp + 26];
    else:
      encoded_message += alphabet[temp];
  print(f"The decoded message is {encoded_message}")


stopProgram = True
while stopProgram:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if direction.lower() == "encode":
    encrypt(user_input=text, shift_amount=shift)
  else:
    decrypt(user_input=text, shift_amount=shift)

  temp = input("Did you want to exit the program? Enter yes or no.\n")
  if temp.lower() == "yes":
    stopProgram = False