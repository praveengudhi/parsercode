import re
import json

#pattern = '^[-+]?[0-9]+$'
pattern = '[0-9]+'

def stbool(v):
    if(v.lower() in "yes", "true", "on"):
        print("true")
    else:
        print("--")
  
def stint(vint):
    #matc = re.match(pattern, vint)
    matc = re.match(r"\d+", vint)
    if (matc):
        print("found")
        if (isinstance(matc, float)):
            print("Float", matc)
        else:
            print("not Float", matc)
    else:
        print("not a integer")

##with open ('config.txt','rt') as myfile:
##    for str in myfile:
##        d = dict(x.split("=") for x in str.split(":"))
##        for key, val in d.items():
##            pattern = re.compile(r'\s+')
##            sentence = re.sub(pattern, '', val)
##            stint(sentence)
##            #print(sentence)
##            #stbool(sentence)

#-------------------------------plugin the config parameter names
#-----------------------------seggregate


config_names = {'strings' :['host ','user','log_file_path'],
                'bools':['verbose','test_mode','debug_mode','send_notifications'],
                'digits':['server_id'],
                'decimals':['server_load_alarm']   }


def search(values, searchFor):    
    for k in values:
        #print("k",k)
        for v in values[k]:
            if searchFor in v:
                #print("tye",)
                return k
    return None

def stbool(v):
    if(v.lower() in "yes", "true", "on"):
        return "true"
    elif (v.lower() in "false","no","off"):
        return "false"


def str2bool(v):
    return str(v).lower() in ("yes","true", "t")

dictobject = {}
with open('config.txt', 'rt') as fil:
    for str in fil:
        str = str.rstrip('\n')
        d = dict(x.split("=") for x in str.split(":"))        
        for key, val in d.items():
            key.replace(" ","")
            val.replace(" ","")
            #print(key,val)            
            returnkey = search(config_names, key)
            #print("re",returnkey)
            #print("val",val)
            if returnkey=='bools':
                returnval = stbool(val)
                print("booreturn", returnval)
                dictobject.update({key:returnval})
            elif returnkey == 'strings':
                dictobject.update({key:val})                
                #print("strings",key,val)
            elif returnkey == 'digits':
                dictobject.update({key:int(val)})
            elif returnkey == 'decimals':
                dictobject.update({key:float(val)})
                
    print("dict",dictobject)
    app_json= json.dumps(dictobject, sort_keys=True)
    print(app_json)
    with open('config.json', 'w') as fp:
        json.dump(dictobject, fp, indent=2)







