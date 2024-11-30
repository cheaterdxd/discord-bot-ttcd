class ValueIsNoneError(Exception):
    def __init__(self, message, value=None):
        super().__init__(message)
        self.value = value

    def __str__(self):
        return f"{self.args[0]} (value: {self.value})"

class GuildNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)


class RoleNotFoundException(Exception):
    def __init__(self, message, role_name):
        super().__init__(message)
        self.missing_role = role_name

    def __str__(self):
        return f"{self.args[0]} (value: {self.missing_role})"
    
class NotValidUserInfoException(Exception):
    def __init__(self, message):
        super().__init__(message)

class NotFoundAdminLogChannelException(Exception):
    def __init__(self, message):
        super().__init__(message)