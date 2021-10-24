import os
from Parameters import crossSections


path="/depot/cms/users/schul105/forMinxi/"

for key in crossSections.keys():

    if "dy" in key and 'dyInclusive' not in key: continue

    
    cmd="cp "+path+"*"+key+"*"+" Other/"
    print (cmd)
    os.system(cmd)
