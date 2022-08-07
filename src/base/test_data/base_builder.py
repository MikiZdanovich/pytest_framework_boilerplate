class BaseBuilder:
    def __init__(self):
        self.data = {}

    def build(self):
        return self.data

    def update_inner(self, keys, value):
        """
        Update inner data structure, if keys not in data, create new one
        :param keys: list or tuple of keys in order to update inner data structure
        :param value: any value to update inner data structure
        :return: self
        """
        if not isinstance(keys, (list, tuple)):
            self.data[keys] = value
        else:
            temp = self.data
            for key in keys[:-1]:
                if key in temp:
                    temp = temp[key]
                else:
                    temp[key] = {}
                temp = temp[key]
            temp[keys[-1]] = value
        return self

    def set_defaults(self):
        raise NotImplementedError
