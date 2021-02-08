import unittest
import name_maker

class TestName(unittest.TestCase):

    def test_name(self):
        self.assertEqual(name_maker.calc_name('Bolaji','Akinyemi'),'Bolaji Akinyemi')

    def test_type(self):
        with self.assertRaises(TypeError):
            name_maker.calc_name('Bolaji',1)

    def test_value(self):
        with self.assertRaises(ValueError):
            name_maker.calc_name('','')
    
if __name__ == "__main__":
    unittest.main()