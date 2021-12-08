from Window import Window
import ctypes

def get_monitor_dimensions():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

width, height = get_monitor_dimensions()

# instantiate a new window with dimensions of monitor
# height - 100 to account for taskbar
window = Window("Network Simulator", width, height-100)

window.show_window()