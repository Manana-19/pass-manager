replyOptions=["y","ye","yes",'sure',"no","n"];
def fieldSelect(sql_cursor):

    sql_cursor.fetchone(); # To Avoid the unfetched data error
    fieldList=[]
    for fieldName in sql_cursor.description:
        
        print(fieldName[0])
        fieldList.append(fieldName[0].lower())
    
    print('Here are the available fields to choose from.');

    opt=input('Choose the following field from the given table of the database. \n=> ').lower()
    loop=True

    while loop==True:    
        if opt in fieldList:
            del fieldList
            loop=False
            return opt
        else: 
            return print('Invalid Option! Please Try again...');

def show(sql_cursor) -> str:
    
    for output_list in sql_cursor.fetchall():    

        print('----------------------------------------------------------')
        for item,data in enumerate(output_list):
            print(f'{sql_cursor.description[item][0]} -> {data}')
    print('----------------------------------------------------------')

    return 'Success'




# ------------------- Main Function to Export


# A function to reset loop condition.
def reset():
    valueToReturn=input('What would you like to do now?\n\n- show => Shows the password of the specific account\n- show_all => Shows all the account ID\'s with their respective password, EMail and Phone No.\n- insert => Inserts a new account with it\'s respective EMail, Phone No. and ID.\n- custom (DANGER) => Enter the command in the format of MySQL Syntax to get your desired output.\n- exit => Closes the program.\n\n\n==> ')
    return valueToReturn;


# A function to show all the data present in the database.

def show_all(sql_cursor) -> str:
    
    sql_cursor.execute('SELECT * FROM acc_pass');
    show(sql_cursor);
    sql_cursor.close();
    return 'No Error';



# A Function to show the specific account detail whose condition is selected by the user.

def show_one(sql_cursor) -> str:
    sql_cursor.execute('SELECT * FROM acc_pass LIMIT 1;');
    opt=fieldSelect(sql_cursor);
    value=input(f'Value for that {opt}.\n==> ');
    sql_cursor.execute(f'SELECT * FROM acc_pass WHERE {opt}=\'{value}\';');
    show(sql_cursor);
    sql_cursor.close();
    return 'No Error';



# A Function to insert the data in this password manager

def insert(sql_cursor) -> str:
    fieldList=[];#  List to store "To Insert"'s data in tuple
    sql_cursor.execute(f'SELECT * FROM acc_pass LIMIT 1');
    sql_cursor.fetchone();#  To Not get "Unread Result found" error.
    
    for item,data in enumerate(sql_cursor.description):
        field=data[0];
        fieldToAdd=input(f'{item+1}. Enter the value for {field}\n==> ');
        fieldList.append(fieldToAdd);

    toInsertString='('
    
    for i in fieldList:
    
        if i != fieldList[-1]:
            toInsertString+=f"{i}, "
    
        else: toInsertString+=f"{i})"
    
    confirm=input("Do you want to save the changes? (y/n)\n==> ").lower();
    
    while confirm:
        
        if confirm in replyOptions[4:]:
            print('Process was cancelled successfully! Exiting to main menu....');
            sql_cursor.close();
            return ''
    
        elif confirm in replyOptions[0:4]:
            print("Saving it, Please wait......");
                
            try:
    
                print(f"INSERT INTO acc_pass VALUES {toInsertString}")

                    # db.commit

                print(f"{sql_cursor.rowcount} rows were inserted successfully!")

            except:
                print("Looks like an error occured. Please check your value's data and try again");
        
            finally:
                sql_cursor.close();
                print('Returning to main menu.....');
                return ''
            
        else:
            confirm=input('Invalid Option...\nDo you want to save the changes? (y/n)\n==>')

    sql_cursor.close();
    return 'No Error';

def custom(sql_cursor):
    
    try:
        toInput=input('Enter the command in **SQL Syntax**\n => ');
        sql_cursor.execute(toInput);
        show(sql_cursor);
    
    except:
        print('The SQL Cursor failed to executed your command, please check your permission or your syntax in the following command.');

    sql_cursor.close();