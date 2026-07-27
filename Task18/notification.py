
class Notification:

    # Class Variable
    total_notifications = 0

    def __init__(self, receiver,**kwargs):
        super().__init__(**kwargs)
        self.__receiver = receiver
        Notification.total_notifications += 1

    # Getter Method
    def get_receiver(self):
        return self.__receiver

    # Static Method
    @staticmethod
    def validate_receiver(receiver):
        if receiver != "":
            return True
        return False

    # Setter Method
    def set_receiver(self, receiver):
        if Notification.validate_receiver(receiver):
            self.__receiver = receiver

    # Class Method
    @classmethod
    def get_total_notifications(cls):
        return cls.total_notifications

    # Parent Method
    def send(self):
        print("Sending Notification")

    # Show Method
    def show(self):
        print("Receiver :", self.__receiver)


class Email(Notification):

    def __init__(self, receiver,**kwargs):
        super().__init__(receiver,**kwargs)

    # Method Overriding
    def send(self):
        print("Sending Email Notification")

    def show(self):
        super().show()


class SMS(Notification):

    def __init__(self, receiver,**kwargs):
        super().__init__(receiver,**kwargs)

    # Method Overriding
    def send(self):
        print("Sending SMS Notification")

    def show(self):
        super().show()


class Push(Notification):

    def __init__(self, receiver,**kwargs):
        super().__init__(receiver,**kwargs)

    # Method Overriding
    def send(self):
        print("Sending Push Notification")

    def show(self):
        super().show()


e1 = Email("rahul@gmail.com")
s1 = SMS("9876543210")
p1 = Push("Mobile App")

print("Email")
e1.show()
e1.send()

print("SMS")
s1.show()
s1.send()

print("Push")
p1.show()
p1.send()

print("Total Notifications :", Notification.get_total_notifications())