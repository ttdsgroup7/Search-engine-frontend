from configobj import ConfigObj


class Configuration:

    def __init__(self):
        self.__properties = dict()
        properties = self._init_properties()
        for property_, value, transform_fn in properties:
            if transform_fn is not None:
                value = transform_fn(value)
            setattr(self, property_, value)
            self.__properties[property_] = {
                'default-value': value,
                'transform_fn': transform_fn
            }

    def _init_properties(self):
        # [[name, default-value, transform_fn]]
        return []

    def load(self, path,start=0,end=0):
        config = ConfigObj(path, encoding='UTF-8')
        for property_, value in config.items():
            transform_fn = self.__properties[property_]['transform_fn']
            if transform_fn is not None:
                value = transform_fn(value)
            if property_ == 'start_date' and start:
                setattr(self, property_, start)
            elif property_ == 'end_date' and end:
                setattr(self,property_,end)
            else:
                setattr(self, property_, value)
