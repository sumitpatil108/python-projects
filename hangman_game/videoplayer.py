import string
msg=input("send a message").lower()
code=int(input("code:"))
letter=[]
letter += map(str,string.ascii_lowercase)
letter+=letter
letter.insert(0," ")

def encrypt(x,msg):


   encrypt_msg=""
   word_count=[]

   print(letter)
   for i in msg:
      word_count.append(letter.index(i))

   word_count=[i+x  for i in word_count]
   for word in word_count:

      encrypt_msg+=letter[word]
   return  encrypt_msg

def decrypt(msg,x):


   decrypt_count=[]
   decrypt_msg=""
   for i in msg:
      decrypt_count.append(letter.index(i))
   decrypt_count=[i-x for i in decrypt_count]
   for i in decrypt_count:
      decrypt_msg+=letter[i]
   return decrypt_msg




encrypt_send=encrypt(code,msg)
print(string.ascii_lowercase)
print(encrypt_send)
decrypt_recv=decrypt(encrypt_send,code)
print(decrypt_recv)


