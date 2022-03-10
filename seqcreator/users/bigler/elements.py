from seqcreator.api.element_provider import ElementProvider

class Elements(ElementProvider):

    def __init__(self, user_name):
        super().__init__(user_name)
        # self.thing_to_segments = {
        #     "curtains": ["all"],
        #     "shelf": ["all"],
        #     "kithcen": ["all"],
        #     "ac_top": ["all"]
        # }

    # def current_segments(self):
    #     return [('curtains', 'all'), ('shelf', 'all'), ('kitchen','all'), ('ac_top','all')]
