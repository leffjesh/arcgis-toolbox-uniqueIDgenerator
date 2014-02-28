'''
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''
import arcpy, uuid

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "arcgis-toolbox-uniqueIDgenerator"
        self.alias = ""
        # List of tool classes associated with this toolbox
        self.tools = [UUIDUpdater]


class UUIDUpdater(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "UUIDUpdater"
        self.description = "Tool to add UUIDs to specified attribute for all records.  Records with attribute already defined will be skipped.  The specified attribute must be a text attribute."
        self.canRunInBackground = False

    def getParameterInfo(self):
        # First parameter
	    param0 = arcpy.Parameter(
	        displayName="Input Feature",
	        name="in_feature",
	        datatype="GPFeatureLayer",
	        parameterType="Required",
	        direction="Input")
	
	    # Second parameter
	    param1 = arcpy.Parameter(
	        displayName="UUID Field",
	        name="uuid_field",
	        datatype="Field",
	        parameterType="Required",
	        direction="Input")
	
	    param1.value = "sourceUniqueID"
	
	    params = [param0, param1]
	
	    return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        inFeatures      = parameters[0].value
    	attribute = parameters[1].value
        
        rows = arcpy.UpdateCursor(inFeatures)
        for row in rows:
            if row.isNull(attribute) or row.getValue(attribute) == " ":
                uuid_val = str(uuid.uuid4()) 
                row.setValue(attribute, uuid_val)
            rows.updateRow(row)
        return
        
