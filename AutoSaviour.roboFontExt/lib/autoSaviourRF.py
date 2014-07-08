import time
from mojo.events import addObserver


class autoSaviour(object):
	def __init__ (self, interval=600):
		print 'AutoSaviour will save all your open fonts every %i seconds automatically.' % interval
		addObserver(self, "_checkTime", "currentGlyphChanged")
		self.timeLastSave = time.time()
		self.interval = interval

	def saveFonts (self):
		for font in AllFonts():
			fileName = font.path.replace('.ufo', '-AutoSaved.ufo')
			copyfont = font.copy()
			print 'Autosaving font...', font
			copyfont.save(fileName)

	def _checkTime (self, info):
		curtime = time.time()
		delta = curtime - self.timeLastSave
		if delta > self.interval:
			self.saveFonts()
			self.timeLastSave = time.time()


autoSaviour(600) # 10 min
# autoSaviour(300) # 5 min
