import json
class parser(object):
    def search(self, values, searchFor):           
        for k in values:
            for v in values[k]:
                if searchFor in v:
                    return k
        return None
    
    def stbool(self, v):
        if(v.lower() in "yes", "true", "on"):
            return "true"
        elif (v.lower() in "false","no","off"):
            return "false"

    
    def configparse(self, config_in, config_json):
        self.dictobject ={}
        self.config_names = {'strings' :['host ','user','log_file_path'],
                'bools':['verbose','test_mode','debug_mode','send_notifications'],
                'digits':['server_id'],
                'decimals':['server_load_alarm']}
        with open('config.txt', 'rt') as fil:
            for str in fil:
                str = str.rstrip('\n')
                d = dict(x.split("=") for x in str.split(":"))        
                for key, val in d.items():
                    key.replace(" ","")
                    val.replace(" ","")          
                    returnkey = self.search(self.config_names, key)
                    if returnkey=='bools':
                        returnval = self.stbool(val)
                        print("booreturn", returnval)
                        self.dictobject.update({key:returnval})
                    elif returnkey == 'strings':
                        self.dictobject.update({key:val})                                    
                    elif returnkey == 'digits':
                        self.dictobject.update({key:int(val)})
                    elif returnkey == 'decimals':
                        self.dictobject.update({key:float(val)})

            print("dict", self.dictobject)
            with open(config_json, 'w') as fp:
                json.dump(self.dictobject, fp, sort_keys=True, indent=2)
                
