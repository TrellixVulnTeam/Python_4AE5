import ctypes
from time import sleep

ctypesHandle = ctypes.windll.user32

ctypesHandle.SetCursorPos(100,20)

ctypesHandle.SetCursorPos(100,40)
sleep(.06)
ctypesHandle.SetCursorPos(200,60)
sleep(.06)
ctypesHandle.SetCursorPos(300,80)
sleep(.06)
ctypesHandle.SetCursorPos(400,100)
sleep(.06)
ctypesHandle.SetCursorPos(400,120)
sleep(.06)
ctypesHandle.SetCursorPos(400,140)
sleep(.06)
ctypesHandle.SetCursorPos(400,160)
sleep(.06)
ctypesHandle.SetCursorPos(400,140)
sleep(.06)
ctypesHandle.SetCursorPos(400,120)
sleep(.06)
ctypesHandle.SetCursorPos(400,100)
sleep(.06)
ctypesHandle.SetCursorPos(300,80)
sleep(.06)
ctypesHandle.SetCursorPos(200,60)
sleep(.06)
ctypesHandle.SetCursorPos(100,40)
sleep(.06)
ctypesHandle.SetCursorPos(100,20)
sleep(.06)
ctypesHandle.SetCursorPos(100,20)
sleep(.06)
#ctypesHandle.mouse_event(2,0,0,0,0)
#ctypesHandle.mouse_event(4,0,0,0,0)
