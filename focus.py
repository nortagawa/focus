from AppKit import NSWorkspace
import time
for _ in range(1,100):
	time.sleep(3)
	print(NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'])

