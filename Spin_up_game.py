from random import shuffle

#INITIAL LIST
mylist=[' ','O',' ']

#SHUFFLE THE_LIST
def shuffle_list(list_nm):
    shuffle(list_nm)
    return list_nm

#MOST CURRENT VALUES IN THE LIST
updated_list = shuffle_list(mylist)
#print(updated_list)
# shuffle_list(mylist)

#TAKE USER GUESS INPUT
def record_user_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input('Enter any value from 0, 1 and 2 ? = ')
    return int(guess)

my_index = record_user_guess()
print('The user entered position is :', my_index)

#CHECK_GUESS CORRECT or NOT
def check_guess(list_nm, guess):
    if list_nm[guess]=='O':
        print("You guessed, Correctly!")
    else:
        print("Wrong Guess")
        print(mylist)

check_guess(updated_list, my_index)





        
        
    
    