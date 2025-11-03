def add_setting(dictionary_setting,tuple_setting):
    key_setting = str(tuple_setting[0]).lower()
    value_setting = str(tuple_setting[1]).lower()
    if key_setting in dictionary_setting.keys():
        return(f"Setting '{key_setting}' already exists! Cannot add a new setting with this name.")
    else:
        dictionary_setting[key_setting] = value_setting
        return(f"Setting '{key_setting}' added with value '{value_setting}' successfully!")

def update_setting(dictionary_setting,tuple_setting):
    key_setting = str(tuple_setting[0]).lower()
    value_setting = str(tuple_setting[1]).lower()
    if key_setting in dictionary_setting.keys():
        dictionary_setting[key_setting] = value_setting
        return(f"Setting '{key_setting}' updated to '{value_setting}' successfully!")
    else:
        return(f"Setting '{key_setting}' does not exist! Cannot update a non-existing setting.")

def delete_setting(dictionary_setting,key):
    key_setting = str(key.lower())
    if key_setting in dictionary_setting.keys():
        del dictionary_setting[key_setting]
        return(f"Setting '{key_setting}' deleted successfully!")
    else:
        return("Setting not found!")

def view_settings(dictionary_setting):
    if len(dictionary_setting) == 0:
        return("No settings available.")
    else:
        str_to_return = "Current User Settings:" + "\n"
        for key in dictionary_setting:
            capitalized_key = str(key).capitalize()
            str_to_return += f"{capitalized_key}: {dictionary_setting[key]}" + "\n"
        return str_to_return


my_settings = {
    'theme': 'light'
   
    }
test_settings = {
    'color':'red',
    'name':'car',
    'model':'Ford'
}

tuple_to_add = ("theme","dark")
option= ('volume','high')

add_setting(my_settings,tuple_to_add)
update_setting(my_settings,tuple_to_add)
update_setting(my_settings,option)
print(view_settings(test_settings))
