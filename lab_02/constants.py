import objects as obj


WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 550

CURRENT_ANGLE = 0.0

TRANSFER = 0
SCALE = 1
ROTATE = 2

building = obj.Rectangle([[-100, -80], [-100, 80], [100, 80], [100, -80]])
roof = obj.Triangle([[-100, 80], [0, 130], [100, 80]])
roof_window = obj.Rectangle([[-15, 90], [-15, 110], [15, 110], [15, 90]])
roof_window_lattice = obj.Plus([[-15, 100], [0, 110], [15, 100], [0, 90]])
left_window = obj.Oval([[-85, 35], [-55, 65]])
left_window_lattice = obj.Plus([[-85, 50], [-70, 35], [-55, 50], [-70, 65]])
door = obj.Oval([[30, -50], [70, 40]])
door_rectangle = obj.Rectangle([[30, -5], [50, 40], [70, -5], [50, -50]])
door_lattice = obj.Plus([[30, -5], [50, -50], [70, -5], [50, 40]])

STEPS_LIST = list()
