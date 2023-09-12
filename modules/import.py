# there are different ways to import

# we can have a package within a package eg a folder within a folder
# folder.folder.module

# can become:

from folder.module import function
from utility import multiply, divide
# dont do the above be explcit and say exactly what you want to import but you can just do:
from utility import *
from packagename.packagename import module

why do this? sometimes we can get name collisions

