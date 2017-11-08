class ConfigData:
    """User given fields"""
    password = None
    login = None

    """Server given fields"""
    client = None
    token = None
    uid = None

    def __init__(self, login=None, password=None, token=None, uid=None, client=None):
        self.password = password
        self.login = login

        self.client = client
        self.token = token
        self.uid = uid

    def overwrite(self, login=None, password=None, token=None, uid=None, client=None):
        """
        :return: Modified DataConfig with the given parameters changed
        """
        return ConfigData(password=password or self.password,
                          login=login or self.login,
                          client=client or self.client,
                          token=token or self.token,
                          uid=uid or self.uid)
