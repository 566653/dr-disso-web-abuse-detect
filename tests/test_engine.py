import unittest,sys,pathlib,json,tempfile
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from engine import analyze
class TestEngine(unittest.TestCase):
 def test_detection(self):
  rules=json.loads((pathlib.Path(__file__).resolve().parents[1]/"rules.json").read_text())
  self.assertEqual(analyze([{rules[0]["field"]:rules[0]["equals"]}])["findings"][0]["rule"],rules[0]["id"])
 def test_clean(self):self.assertEqual(analyze([{"id":"clean"}])["findings"],[])
 def test_bad_input(self):
  with self.assertRaises(ValueError):analyze({})
 def test_empty(self):self.assertEqual(analyze([])["max_risk"],0)
if __name__=="__main__":unittest.main()
