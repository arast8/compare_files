# Author: Andrew Rast
# Date: 03/02/2021

import wx

class DirPickerDropTarget(wx.FileDropTarget):
	def __init__(self, parent):
		super().__init__()

		self.Parent = parent

	def OnDropFiles(self, x, y, filenames):
		self.Parent.SetPath(filenames[0])

		return True
