# import travel.england
# trip_to = travel.england.EnglandPackage()
# trip_to.detail()

# # or you can use other way to import file

# from travel.england import EnglandPackage
# trip_to = EnglandPackage()
# trip_to.detail()

# or

# from travel import sweden
# trip_to = sweden.SwedenPackage()
# trip_to.detail()

# We have used "from random import *"
# However, "from travel import *" alone will not work when you create or use packages you create
# So, we have to use "__all__" in __init__.py

from travel import *
# trip_to = england.EnglandPackage()
# trip_to.detail()

# from travel import *
# trip_to = sweden.SwedenPackage()
# trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(england))