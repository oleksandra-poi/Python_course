import sys
print("Before:", sys.path)
sys.path.append("extra")
print("After:", sys.path)

import test_module
test_module.hello()
