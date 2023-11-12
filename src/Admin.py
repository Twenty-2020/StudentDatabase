class Admin(User):
    def __init__(self, email: str, password: str, adminID: int):
        super().__init__(email, password)
        self.adminID = adminID

    def getAdminID(self) -> int:
        return self.adminID

    def getClassName(self) -> str:
        return "Admin"

    def __eq__(self, compare: Admin) -> bool:
        return self.adminID == compare.adminID
