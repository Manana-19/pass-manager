import mysql.connector;
from dotenv import dotenv_values;
from functions import show_all, show_one, custom, insert;
# Importing external modules

config=dotenv_values(".env")
#Loading .env for login details
database_connection = mysql.connector.connect(
    host=config['HOST'], # Enter your host in .env file
    user=config['USER'], # Enter your user/username in .env file
    password=config['PASS'], # Enter your password in .env file
    database=config['DATABASE'], # Enter the Database too in that .env file.
    auth_plugin='mysql_native_password'
)


showList=['show','s','view'];showAllList=['showall','show-all','show all','view all','view-all','sa'];insertList=['i','insert','add','new'];customList=['custom'];exitList=['e','exit','leave'];allOptions=["y","ye","yes",'sure',"no","n"];

print('Welcome to the Password Manager!')
while True:
    loopCondition=input('What would you like to do now?\n\n- show => Shows the password of the specific account\n- show_all => Shows all the account ID\'s with their respective password, EMail and Phone No.\n- insert => Inserts a new account with it\'s respective EMail, Phone No. and ID.\n- custom (DANGER) => Enter the command in the format of MySQL Syntax to get your desired output.\n- exit => Closes the program.\n\n\n==> ');
    cursor=database_connection.cursor();
    
    if loopCondition.lower() in showList:
        show_one(cursor);
    elif loopCondition.lower() in showAllList:
        show_all(cursor);
    elif loopCondition.lower() in insertList:
        insert(cursor);database_connection.commit();
    elif loopCondition.lower() in customList:
    
        ask=input('Are you sure you want to use this option?It\'s currently under development.\nWe recommend you not to use this option if you don\'t know about MySQL.\n=> ');
        
        if ask in allOptions[4:]:
            pass;
        elif ask in allOptions[0:4]:
            custom(cursor);
    
    elif loopCondition.lower() in exitList:
        print('Thanks for using this program!');exit();
    else:
        print('Wrong option selected. Please try again!');
