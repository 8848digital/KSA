import json
import os

from erpnext.setup.setup_wizard.operations.taxes_setup import from_detailed_data, simple_to_detailed

def setup_templates(doc,method=None):
	if doc.country == 'Saudi Arabia':
		file_path = os.path.join(os.path.dirname(__file__), "..", "data", "ksa_template.json")
		with open(file_path, "r") as json_file:
			template = simple_to_detailed(json.load(json_file))
			from_detailed_data(doc.name,template)
			


