from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailChannel(NotificationChannel):
    def __init__(self, smtp_server):
        self.smtp_server = smtp_server

    def send(self, message):
        print(f"Sending Email via {self.smtp_server}: {message}")

class SMSChannel(NotificationChannel):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def send(self, message):
        print(f"Sending SMS to {self.phone_number}: {message}")

class NotificationService:
    def __init__(self):
        self.channels = []

    def add_channel(self, channel):
        self.channels.append(channel)

    def notify_all(self, message):
        for channel in self.channels:
            channel.send(message)

service = NotificationService()
service.add_channel(EmailChannel("smtp.example.com"))
service.add_channel(SMSChannel("+251900000000"))

service.notify_all("Server is down!")