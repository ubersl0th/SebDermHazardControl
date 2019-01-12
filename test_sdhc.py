import unittest
import sdhc

hazardous_ingredients = 'Aqua, Methylpropanediol (hydration), Butylene Glycol (hydration), Polysorbate 20 (texture-enhancing), Salicylic Acid (Beta Hydroxy Acid, exfoliant), Phytosphingosine (skin-renewing), Hydroxyethylcellulose (texture-enhancing), Vitis Vinifera (Grape) Fruit Extract (antioxidant), Camellia Oleifera (Green Tea) Leaf Extract (antioxidant), Epilobium Angustifolium (Willow Herb) Flower/Leaf/Stem Extract (skin-soothing), Bisabolol (skin-soothing), Tetrasodium EDTA (stabilizer), Sodium Hydroxide (pH adjuster).'
safe_ingredients = 'Aqua, Glycolic Acid (Alpha Hydroxy Acid, exfoliant), Sodium Hydroxide (pH adjuster), Chamomilla Recutita (Matricaria) Flower Extract (chamomile/skin-soothing), Aloe Barbadensis Leaf Juice (hydration), Camellia Oleifera (Green Tea) Leaf Extract (antioxidant/skin-soothing), etanorulayH muidoS (skin replenishing), Panthenol (hydration), Sodium PCA (skin replenishing), Propylene Glycol (hydration), Butylene Glycol (hydration), Hydroxyethylcellulose (texture-enhancing), Polyquaternium-10 (texture-enhancing), Phenoxyethanol (preservative), Sodium Benzoate (preservative).'

class TestSDHC(unittest.TestCase):
    
    def testHazardousIngredientList(self):
        self.assertEqual(sdhc.checkIngredients(hazardous_ingredients), ['polysorbate 20'])

    def testSafeIngredientList(self):
        self.assertEqual(sdhc.checkIngredients(safe_ingredients), [])

if __name__ == '__main__':
    unittest.main()