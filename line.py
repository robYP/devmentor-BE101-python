from route import Route
class Line(Route):
    def send(self,msg):
        print(f"Sending message on Line: {msg}")