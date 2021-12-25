import json
# Parser class to sear

class parser(object):
    # Funtion for Seacrch  Key and Values from  Dictionary
    def searchKeyValues(self, values, searchFor):           
        for key in values:
            for val in values[key]:
                if searchFor in val:
                    return key
        return None
    #  Funtion for Boolean values Loo up
    def stbool(self, value):
        if(value.lower() in "yes", "true", "on"):
            return "true"
        elif (value.lower() in "false","no","off"):
            return "false"
    # Method for parsing the configuration file
    def configparse(self, config_in, config_json):
        self.dictobject ={}
        self.config_names = {'strings' :['host ','user','log_file_path'],
                'bools':['verbose','test_mode','debug_mode','send_notifications'],
                'digits':['server_id'],
                'decimals':['server_load_alarm']}
        # Read configuration file 
        with open('config.ini', 'rt') as file:
            for line in file:
                # Read the comments section lines
                line = line.rstrip('\n')                
                if  line.lstrip().startswith("#"):                    
                        self.dictobject.update({"comment":line})
                        continue
                else:
                    # Dictionary for splitting the Key and Values
                    d = dict(x.split("=") for x in line.split(":")) 
                    #
                    for key, val in d.items():
                        key.replace(" ","")
                        val.replace(" ","")
                        #  Check for the values in strings
                        returnkey = self.searchKeyValues(self.config_names, key)
                        if returnkey=='bools':
                            returnval = self.stbool(val)                            
                            self.dictobject.update({key:returnval})
                        elif returnkey == 'strings':
                            self.dictobject.update({key:val})                                    
                        elif returnkey == 'digits':
                            self.dictobject.update({key:int(val)})
                        elif returnkey == 'decimals':
                            self.dictobject.update({key:float(val)})           
            with open(config_json, 'w') as fp:
                json.dump(self.dictobject, fp,  indent=2)
                
