from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, recipient):
        self.__recipient = recipient

    def get_recipient(self):
        return f"Recipient : {self.__recipient}"

    def set_recipient(self, recipient):
        self.__recipient = recipient
        return "Recipient Updated"

    @abstractmethod
    def send(self, message):
        pass

    def notification_info(self):
        return f"Recipient : {self.__recipient}"


class EmailNotification(Notification):
    def __init__(self, recipient, email):
        super().__init__(recipient)
        self.__email = email

    def send(self, message):
        print("Email Notification")
        print(self.notification_info())
        print(f"Email : {self.__email}")
        print(f"Message : {message}")


email = EmailNotification("Greesha", "greesha@gmail.com")

print(email.get_recipient())
print(email.notification_info())
email.send("Your assignment has been submitted.")