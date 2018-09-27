import time
from pymongo import MongoClient
mongua = MongoClient()

def timestamp():
    return int(time.time())


def next_id(name):
    query = {
        'name': name
    }
    update = {
        '$inc':{
            'seq': 1
        }
    }
    kwargs = {
        'query': query,
        'update': update,
        'upsert': True,
        'new':True,
    }
    doc = mongua.db['data_id']
    new_id = doc.find_and_modify(**kwargs).get('seq')
    return new_id


class Mongua(object):
    __fields__ =[
        'id',
        ('id', int, -1),
        ('type', str,''),
        ('deleted', bool,False),
        ('created_time', int, 0),
        ('updated_time', int, 0),
    ]

    @classmethod
    def new(cls, form=None, **kwargs):
        name = cls.__name__
        m = cls()
        fields = cls.__fields__.copy()
        fields.remove('id')
        if form is None:
            form ={}

        for f in fields:
            k, t ,v =f
            if k in form:
                setattr(m, k, t(form[k]))
            else:
                setattr(m, k, v)

        for k, v in kwargs.items():
            if hasattr(m, k):
                setattr(m, k, v)
            else:
                raise KeyError
            m.id = next_id(name)
            ts = int(time.time())
            m.created_time = ts
            m.updated_time = ts
            m.type = name.lower()
            m.save()
            return m
        def save(self):
            name = self.__class__.__name__
            mongua.db[name].save(self.__dict__)

