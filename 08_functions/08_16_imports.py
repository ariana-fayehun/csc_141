# I applied what I learned in the text to figure out how to complete this 
# assignment

# Imports module
import profile
user_profile = profile.build_profile('albert', 'einstein', location='princeton',
                             field='physics')
print(user_profile)

# Imports specific function in module
from profile import build_profile
user_profile = build_profile('albert', 'einstein', location='princeton',
                             field='physics')
print(user_profile)

# Imports specific function in module and gives it an alias
from profile import build_profile as bp
user_profile = bp('albert', 'einstein', location='princeton',
                             field='physics')
print(user_profile)

# Imports specific module and gives it an alias
import profile as p
user_profile = p.build_profile('albert', 'einstein', location='princeton',
                             field='physics')
print(user_profile)

# Imports all functions in a module
from profile import *
user_profile = profile.build_profile('albert', 'einstein', location='princeton',
                             field='physics')
print(user_profile)