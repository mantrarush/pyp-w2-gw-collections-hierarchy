class ComparableMixin(object):
    def __eq__(self, other):
        # assuming same data type
        if isinstance(self, other):
            self_elems = self.get_elements()
            other_elems = other.get_elements()
            
        
        pass
                
    def __ne__(self, other):
        # Relies in __eq__
        pass


class SequenceMixin(object):
    def __iter__(self):
        self.elements = self.get_elements()
        self.current_index = 0
        return self

    def __next__(self):
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")
        # Keep writing your code here
        while self.current_index < len(self.elements):
            elem = self.elements[self.current_index]
            self.current_index += 1
            return elem
        raise NotImplementedError()

    next = __next__
#getelem in main_collection, 
    def __len__(self):
        # Will rely on the iterator
        # can't do len(self.data)
        counter = 0 
        while self.current_index < len(self.elements):
            # counter += 1
            elem = self.elements[self.current_index]
            self.current_index += 1
        return self.current_index
        # return counter
        

    def __getitem__(self, key):


        data = getattr(self, self.DATA_ATTR_NAME) #name of the attribute of the instance; stores the name for dictionary of elements or list (name of attribute or list)
        # value = data[key]
        return data[key]
        # data.__getitem__(key) <==> data[key]
  
            
        # returns self.data, which is a list or dict
         pass
     

    def __setitem__(self, key, value):
        
        data = getattr(self, self.DATA_ATTR_NAME)
        data[key] = value

    def __delitem__(self, key):
        pass

    def __contains__(self, item):
        # Will rely on the iterator
        pass


class RepresentableMixin(object):
    def __repr__(self):
        # Will rely on the iterator or __str__
        pass

    def __str__(self):
        # Will rely on the iterator
        pass


class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'
    
#setting things in a more general fashion =>use setattr and getattr 

    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)
        # self.data = initial or self.DATA_DEFAULT_INITIAL

        # setattr(x, 'foobar', 123) <==> x.foobar = 123
class OperableMixin(object):
    def __add__(self, other):
        pass

    def __iadd__(self, other):
        pass


class AppendableMixin(object):
    def append(self, elem):
        # Relies on DATA_ATTR_NAME = 'data'
        pass


class HashableMixin(object):
    def keys(self):
        pass

    def values(self):
        pass

    def items(self):
        pass


class IndexableMixin(object):
    def index(self, x):
        pass
