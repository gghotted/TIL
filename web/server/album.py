import pickle


class Album():

    def __init__(self):
        self.autoId = 0
        self.finder = {}

    def add(self, image):
        image.id = self.autoId
        self.autoId += 1
        self.finder[image.id] = image

    def delete(self, img_id):
        del self.finder[img_id]

    def save(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    @property
    def images(self):
        return self.finder.values()


class Image():

    def __init__(self, title, file):
        self.id = None
        self.title = title
        self.file = file


def load(path):
    with open(path, 'rb') as f:
        obj = pickle.load(f)
    return obj
