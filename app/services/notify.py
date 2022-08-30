from notifypy import Notify

def notify(message, title):
    
    notification = Notify()
    notification.title = "Sua localização atual"
    text = notification.message = "Perfeito"
    notification.send()
