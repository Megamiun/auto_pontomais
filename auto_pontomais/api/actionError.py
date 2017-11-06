class ActionError(Exception):

    def __init__(self, action, uid, error_code):
        self.uid = uid
        self.action = action
        self.error_code = error_code

    def __str__(self):
        return "{} - Couldn't do action with user uid '{}'. HTTP Status: {}".format(self.action, self.uid, self.error_code)
