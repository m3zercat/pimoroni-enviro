from MicroPython_LC709203F.LC709203F_CR import LC709203F

from enviro import i2c

lc709203f = LC709203F(i2c)
lc709203f.init_RSOC()  # sensor must be initialised


@property
def voltage():
    return lc709203f.cell_voltage


@property
def percentage():
    return lc709203f.cell_percent
