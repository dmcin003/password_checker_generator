#imported libraries/packages
import string, random, array


def check_special_chars(password,spec_chars):
    for char in password:
        for spec_char in spec_chars:
            if char == spec_char:
                return True
    return False

def check_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False    


def check_letter(password):
    for char in password:
        if char.isalpha():
            return True
    return False



def check_uppercase(password):
    for char in password:
        if check_letter(char) == True:
            if char.isupper() == True:
                return True
            else:
                pass
        else:
            continue
    return False







min_length = 8
special_chars = ['!','@','#','?']
bad_password = False
done = False
answer = ''

# generates a strong password if the user wants one
combined_list = string.ascii_letters + string.digits + "".join(special_chars)
temp_password = random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice(special_chars)
for x in range(min_length-4):
    temp_password = temp_password + random.choice(combined_list)

password_list = array.array('u',temp_password)
random.shuffle(password_list)

generated_password = "".join(password_list)


# prompts the user to enter password of their choice
while not done:
    print(f"password requirements:\none letter\none uppercased letter\none number\none of these special characters: {special_chars}\nhave a minimum length of 8 characters.")
    password = input("Enter a password for your account: ")

    if(len(password) < min_length):
        print("password doesn't meet the length requirments.")
        bad_password = True
    else:
        #check that password has atleast one letter in it.
        if check_letter(password) == True:
        #check for one letter uppercased.
            if check_uppercase(password) == False:
                print("password doesn't contain atleast one upper-cased letter" )
                bad_password = True
            
        else:
            print("password doesn't contain atleast one letter.")
            bad_password = True 
    
        #check for atleast one number
        if check_digit(password) == False:
            print("password doesn't contain atleast one number.")
            bad_password = True
     
        #check for atleast one special character
        if check_special_chars(password,special_chars) == False:
            print(f"password doesn't contain atleast one of these special characters: {special_chars}")
            bad_password = True






    if bad_password == True:
        answer = input("Would you like me to generate a strong password for you? Y or N: ")
        if answer == 'Y':
            print(generated_password)
            done = True
        elif answer == 'N':
            done = False
        
    else:
        print('Your password has been successfully created!')
        done = True




