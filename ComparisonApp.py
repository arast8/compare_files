# Author: Andrew Rast
# Date: 03/02/2021

import wx
from DirPickerDropTarget import DirPickerDropTarget
from comparison_algorithms import *

class ComparisonApp(wx.App):
	OperationTypeChoices = ["Similarities", "Differences"]

	def OnInit(self):
		# Frame
		top_window = wx.Frame(None, title="File/Directory Comparison App",
			size=wx.Size(800, 600))
		top_window.SetSizer(wx.BoxSizer(orient=wx.VERTICAL))
		self.SetTopWindow(top_window)

		# Panel
		main_panel = wx.Panel(top_window)
		main_panel.SetSizer(wx.BoxSizer(orient=wx.VERTICAL))
		top_window.Sizer.Add(main_panel, proportion=1,
			flag=wx.ALL|wx.EXPAND|wx.EXPAND)

		# Controls
		self.Picker1 = wx.DirPickerCtrl(main_panel)
		self.Picker1.SetDropTarget(DirPickerDropTarget(self.Picker1))
		main_panel.Sizer.Add(self.Picker1, flag=wx.ALL|wx.EXPAND, border=20)

		self.Picker2 = wx.DirPickerCtrl(main_panel)
		self.Picker2.SetDropTarget(DirPickerDropTarget(self.Picker2))
		main_panel.Sizer.Add(self.Picker2, flag=wx.ALL|wx.EXPAND, border=20)

		self.RadioBox = wx.RadioBox(main_panel, choices=self.OperationTypeChoices)
		main_panel.Sizer.Add(self.RadioBox, flag=wx.LEFT, border=20)

		compare_button = wx.Button(main_panel, label="Compare")
		main_panel.Sizer.Add(compare_button, flag=wx.ALIGN_CENTER_HORIZONTAL)
		compare_button.Bind(event=wx.EVT_BUTTON, handler=self.compare)

		self.Log = wx.TextCtrl(main_panel, style=wx.TE_MULTILINE)
		main_panel.Sizer.Add(self.Log, proportion=1, flag=wx.ALL|wx.EXPAND, border=20)

		# Make stuff visible
		top_window.Center()
		top_window.Show()

		return True

	def compare(self, event_handler):
		path_1 = self.Picker1.Path
		path_2 = self.Picker2.Path
		operation_type = self.OperationTypeChoices[self.RadioBox.Selection]
		result = ""

		if os.path.isfile(path_1) and os.path.isfile(path_2):
			result = compare_files(path_1, path_2)
		elif os.path.isdir(path_1) and os.path.isdir(path_2):
			if operation_type == "Similarities":
				result = compare_dirs_similarities(path_1, path_2)
			elif operation_type == "Differences":
				result = compare_dirs_differences(path_1, path_2)
			else:
				result = "Invalid operation."
		elif os.path.isdir(path_1) and path_2 == "":
			result = compare_dir_duplicates(path_1)
		else:
			result = "Invalid operation."

		self.Log.SetValue(result)

if __name__ == "__main__":
	app = ComparisonApp()
	app.MainLoop()
