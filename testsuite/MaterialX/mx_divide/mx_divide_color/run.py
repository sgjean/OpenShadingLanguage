#!/usr/bin/env python
import os
loc = os.environ["OSLHOME"] + os.environ["MATERIALX_OSOS"]+ "/"

def buildCmd(shader, inputs):
	cmd = "--print "
	for pName, pValue in inputs.iteritems():
		cmd += " -param " + pName + " " + pValue	
	cmd += " " + shader + " -o out mx.exr"
	return cmd


inputs = {
	         "in1" : "0.1,0.2,0.3",

	         "in2" : "0.4,0.5,0.6"
         }

shader = loc + os.path.basename(os.getcwd())
command = testshade(buildCmd(shader, inputs))
