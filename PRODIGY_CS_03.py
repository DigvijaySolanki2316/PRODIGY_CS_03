#!/usr/bin/env python
# coding: utf-8

# In[4]:


import re

def check_password(password):
   

    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Check for at least one digit
    if not re.search(r'\d', password):
        return False

    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    # Check for minimum length
    if len(password) < 8:
        return False

    return True

pwd=input("Enter the passsword :")
print("password is :",pwd)

if check_password(pwd):
    print("The password is complex enough.")
else:
    print("The password is not complex enough.")


# In[ ]:





# In[ ]:




