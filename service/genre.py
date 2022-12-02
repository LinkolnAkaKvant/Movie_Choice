from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_by_id(self, gid):
        return self.dao.get_by_id(gid)

    def get_all(self):
        return self.dao.get_all()