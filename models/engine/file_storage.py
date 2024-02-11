class FileStorage:
    __file_path = "file.json"
    __objects = {}
	
    def all(self):
        """Return the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Add new instance(obj) to the dictionary(__objects) with
        a key <obj class name>.id"""
        obj_class = obj.__class__.__name__
        FileStorage.__objects["{].{}".format(obj_class, obj.id) = obj

    def save(self):
        obj_dic = FileStorage.__objects
        obj_json_dic = {obj: obj_dic[obj].to_dict() for obj in obj_dic.keys()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_json_dic, f)

    def reload(self):
       """ deserializes the JSON file to __objects 
       (only if the JSON file (__file_path)"""
        pass 

