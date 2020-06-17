class SenseImage:
    def __init__(self):
        r = (255, 0, 0)
        b = (0,0,0)
        self.stopImage = [
                b,b,b,b,b,b,b,r,
                r,b,b,b,b,b,r,b,
                b,r,b,b,b,r,b,b,
                b,b,r,b,r,b,b,b,
                b,b,b,r,b,b,b,b,
                b,b,r,b,r,b,b,b,
                b,r,b,b,b,r,b,b,
                r,b,b,b,b,b,r,b
        ]
        
        self.rightImage = [
                b,b,b,r,r,b,b,b,
                b,b,b,b,r,r,b,b,
                b,b,b,b,b,r,r,b,
                b,b,b,b,b,b,r,r,
                r,r,r,r,r,r,r,r,
                b,b,b,b,b,r,r,b,
                b,b,b,b,r,r,b,b,
                b,b,b,r,r,b,b,b
                ]
        self.leftImage = [
                b,b,b,r,r,b,b,b,
                b,b,r,r,b,b,b,b,
                b,r,r,b,b,b,b,b,
                r,r,b,b,b,b,b,b,
                r,r,r,r,r,r,r,r,
                b,r,r,b,b,b,b,b,
                b,b,r,r,b,b,b,b,
                b,b,b,r,r,b,b,b
                ]
        self.goImage = [
                b,b,b,b,r,b,b,b,
                b,b,b,b,r,b,b,b,
                b,b,b,b,r,b,b,b,
                r,b,b,b,r,b,b,r,
                r,r,b,b,r,b,r,r,
                b,r,r,b,r,r,r,b,
                b,b,r,r,r,r,b,b,
                b,b,b,r,r,b,b,b  
                ]
        self.backImage = [
                b,b,b,r,r,b,b,b,
                b,b,r,r,r,r,b,b,
                b,r,r,r,b,r,r,b,
                r,r,b,r,b,b,r,r,
                r,b,b,r,b,b,b,r,
                b,b,b,r,b,b,b,b,
                b,b,b,r,b,b,b,b,
                b,b,b,r,b,b,b,b
                ]
