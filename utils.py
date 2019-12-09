import math


class BoundBox:
    def __init__(self, wmin, hmin, wmax, hmax): # h- height, w - width
        self.hmin = hmin
        self.wmin = wmin
        self.hmax = hmax
        self.wmax = wmax
        self.box = [self.wmin,self.hmin]
        self.size = [int(wmax - wmin), int(hmax - hmin)]
        self.box = self.box+self.size
        
    def __repr__(self):
        return str(self.box) #  left, top, width, height
    
    def __getitem__(self, i):
        return self.box[i]
        
        
        
def ellipse2rect(major_axis,minor_axis, angle=0, center_x=0, center_y=0):
    angle = -angle
    width = math.sqrt((minor_axis*math.sin(angle))**2 + (major_axis*math.cos(angle)))
    height = math.sqrt((major_axis*math.sin(angle))**2 + (minor_axis*math.cos(angle)))
    wmin = center_x - width
    wmax = center_x + width
    hmin = center_y - height
    hmax = center_y + height
    return BoundBox(wmin,hmin,wmax,hmax)
    