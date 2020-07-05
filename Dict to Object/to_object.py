from collections import OrderedDict

class  Object(object):
    '''To convert dict recursively'''
    def __init__(self, value):
        '''value: dict or OrderedDict'''
        if value:
            self.__dict__ = self.__to_format_dict(value)
        else:
            self.__dict__ = { }
        
    def __to_format_dict(self, dictvalue):
        return { self.__to_format_key(key) : self.__to_get_item_to_convert_to_object(value) for key, value in dictvalue.items() }
         
    def __to_get_item_to_convert_to_object(self, value):
        if type(value) is list:
            return [ self.__to_get_item_to_convert_to_object(obj) for obj in value ]
        elif type(value) is OrderedDict:
            return Object(value)
        elif type(value) is dict:
            return Object(value)
        else:
            return value
          
    def __to_format_key(self, key):
        if key.isspace():
            return key.replace(' ', '_')
        else:
            return key.replace('-', '_')
