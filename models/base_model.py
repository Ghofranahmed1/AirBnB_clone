#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


"""Class BaseModel that defines
all common attributes/methods for other classes"""

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize Public instance attribute"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    """here we prais the time  (today) to be in 
                    time_format"""
                    self.__dict__[k] = datetime.strptime(v, time_format)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """ updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.sotrge.save()

    def to_dict(self):
        """returns a dictionary containing all 
        keys/values of __dict__ of the instance and 
        some more keys like class and created_at and updated_at
        and it's copy from the orignal __dic__, it;s will not 
        effect the orignal dic, this function is like 
        create my own dic function"""
        
        my_dic = self.__dict__.copy()
        my_dic["__class__"] = self.__class__.__name__
        """print these two var in iso format"""
        my_dic["created_at"] = self.created_at.isoformat()
        my_dic["updated_at"] = self.updated_at.isoformat()
        return my_dic

    def __str__(self):
        """Print information about this class"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
