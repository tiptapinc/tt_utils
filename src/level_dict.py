from UserDict import DictMixin
# import leveldb
import pickle


class LevelDict(object, DictMixin):
    """
    persistent dictionary-like object using LevelDB
    and Pickle
    """
    def __init__(self, path):
        """Constructor for LevelDict"""
        self.path = path
        # self.db = leveldb.LevelDB(self.path)

    # def __getitem__(self, key):
    #     return pickle.loads(self.db.Get(key))

    # def __setitem__(self, key, value):
    #     self.db.Put(key, pickle.dumps(value))

    # def __delitem__(self, key):
    #     self.db.Delete(key)

    # def __iter__(self):
    #     for k, v in self.db.RangeIter(include_value=False):
    #         yield k

    # def keys(self):
    #     return [k for k, v in self.db.RangeIter()]
