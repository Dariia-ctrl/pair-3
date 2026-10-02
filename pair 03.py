#name = "Ivan"
#age = "18"
#print(len(name))
#print(name[0])
#print(name[4])
#print(name[len(name) - 1])


#text = input()
#if len(text) > 0:
#    print(text[0])
#else:
 #   print("Рядок порожній")

# text = 'hello world'
#print(text[:5])
#print(text[6:])
#print(text[::2])
#print(text[::-1])

#text_upper = text.upper()
#print(text)
#print(text.lower()) # нижній регістр
#print(text.title()) # кожне слово з великої
#print(text.upper()) #верхній регістр
#print(text.capitalsize()) #Перша літера рядка з великої

#text = ' Python'
#print(text.lstrip()) #
#print(text.rstrip())
#print(text.strip())

#user_login = "admin"

#login = input("Enter your login : ").strip().lower
#if user_login == login:
 #   print("Welcome" + user_login)


#password = input() #2 цифри, 2 символи кепсом, довжина > 8
#digits = 0
#u_letter = 0
#if len(password) >= 8:
#    for char in password:
#        if char.isdigit():
 #           digits += 1
 #       if char.isupper():
 #           u_letter += 1
#    if digits >= 2 and u_letter >= 2:
#        print("relieble")
 #   else:
#        print("not relieble")
#else:
#    print("must contein more than 8 symbols")

#password.isdigit() #перевірка (тру фолс)
#password.isupper() #Всі букви капсом
#password.islower() #нижні
#password.isalpha() #тільки букви
#password.isalnum() #тільки цифри

#Golosni = "аеєиїоуяію"
#count = 0
#text = input("Введи текст: ").lower()
#for char in text:
#    if char in Golosni:
#        count += 1
#print(count)

#text = "Hello                     world! Python is the best!!"
#words = text.split()
#print(words)
#result = "-".join(words)
#print(result)
#new_text = text.place(old."Python", new."JavaScript")

#text = input().lower().strip()
#if text == text[::-1]:
#    print("palindrom") #однаково зліва направа і справа на ліво
#else:
#    print("not palidrom")

text = input().strip()

words = text.split()

max_word = words[0]
for word in words:
    if len(word) > len(max_word):
        max_word = word
    print(max_word)
