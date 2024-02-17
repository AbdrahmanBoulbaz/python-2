
while True :

   while True :
     try:
      first_number = float(input('entre le premié nomber :' ))
      break
     except ValueError :
         print('please entere numinc variabl')

   while True :
    try:
     op =input('enter opération  :')
     if op in ('+','/','*','-') :
        break
     else:
         raise ValueError
    except ValueError :
     print('invalid op pleas entrer / * + -')
   while True :
    try:
     second_number = float(input('enter le dexiéme nomber :'))
     if second_number == 0 and op == '/' :
         raise ZeroDivisionError
     break
    except ValueError:
       print('please entere numinc variabl')
    except ZeroDivisionError:
        print('cannot divide by zero , please enter the new number')

   if op == '+':
        résulta = first_number + second_number
   elif op == '−':
       résulta = first_number -second_number
   elif op == '/':
        résulta = first_number / second_number
   elif op == '*':
        résulta = first_number * second_number
   else:
        résulta = ('error')
   print(résulta)
   if résulta != None :
     print('result is ',résulta)
   else:
      print('error')
   break
