#create a list

names = ["Blerta", "Erosi", "Driloni", "Brikena","Ylli"]

#Ilerate in the names list and print every name

for name in names:
    print(name)


################################

sentance = "Hello world"

for character in sentance:
    if character.isalpha(): #check if the charater is a letter
        print(character)


        # Range Function

        for number in range(1,6): #prints number from the number 1 to 5 or more intail n to m-1
            print(number)

##################################################

numbers = [12,45,6,72,21,8,94,57]

#initilaze a varable "maximum" with the first value from the list "numbers

maximum = numbers[0]

for num in numbers:  #Begin a loop iteratig through each element in the list "numbers"
    if num > maximum: # chech if the current element "num" is bigger then the current maximum value
        maximum = num # if so,update the maximum value to be the current element in num
    print("The maximum value in the list is: ", maximum)


##############################################
#while loop

count = 1 # Initialize the loop control variable

while count <= 5 #the condition if count is less then equal to 5
    print("Iteration", count)
    count +=1 #increment the loop control variable

    #########################################
    #Do While Loop

    # infinite loop

while True:
    # Promt user to enter a positive number
user_input = input("Enter a positive number: ")



#Check if the input is numeric
if user_input.isnumeric():
    number = int(user_input)

    if number > 0:
        break

        #Print the error message for invalid input
        print("invalide input please try again")
        #Print the valid positive numer entered by the user
        print("you have entered a valid positive number:", number)


########################################
#break


numberList = [1,2,3,4,5,6,7]
target =4

for number in list:
    print(number) #Print the current element that is being iterated
    if number == target: #Check if the current element is equal to the target value
        print("target found")
        break # End the loop immediatley after finding the target