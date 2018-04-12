import PythonMagick as pm

def imageSharpness(outputDir):

	img = pm.Image(outputDir)

	img.colorSpace(pm.ColorspaceType.GRAYColorspace)

	img.resize('1191x2000')
	img.quality(100)
	img.sharpen(50, 50)
	img.contrast(0)

	img.write(outputDir)
	
	return