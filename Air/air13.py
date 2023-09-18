import unittest
import os
import importlib.util

class ScriptTest(unittest.TestCase):
    def test_script_exists(self):
        script_files = ["air01.py"]
        
        for script_file in script_files:
            self.assertTrue(os.path.isfile(script_file), f"Le script '{script_file}' est introuvable")
            
    def test_script_functionality(self):
        script_files = ["air01.py"]
        
        for script_file in script_files:
            spec = importlib.util.spec_from_file_location("script", script_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            self.assertTrue(hasattr(module, "main"), f"Le script '{script_file}' ne contient pas de fonction 'main'.")
            

if __name__ == "__main__":
    script_test = ScriptTest()
    air01 = script_test.test_script_exists()
    print(air01)