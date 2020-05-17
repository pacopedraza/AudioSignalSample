import unittest
from downsample_audio_signal import *
from array import *


class DecimateTestCase(unittest.TestCase):
    """This class tests
    1. Downample by two
    2. Decimate by two
    """

    def test_decimate(self):
        """
        Tests lips the second array before `sliding` 
        the two across one another.
        """
        output1 = downsample_by_2(input_convolve, input_convolve2)
        self.assertEqual(expected_convolve1, output1)
        self.assertEqual(output1, expected_convolve1)

    def test_decimate_middle(self):
        """
        Tests Contains boundary effects, where zeros 
        are taken into account.
        """
        output2 = downsample_by_2(input_conv_middle, input_conv_middle2, middle_val)
        self.assertEqual(expected_conv_middle, output2)

    def test_decimate_same(self):
        """
        Test same length, so there is only one position
        where they completely overlap.
        """
        output_same = downsample_by_2(input_conv_middle, input_conv_middle2, same_val)
        self.assertEqual(expected_same, output_same)

# Test variables
input_convolve = [1, 2, 3]
input_convolve2 = [0, 1, 0.5]
expected_convolve1 = array(str('u'),'[0. , 1. , 2.5, 4. , 1.5]')

input_conv_middle = [1,2,3]
input_conv_middle2 = [0,1,0.5]
middle_val = 'same'
expected_conv_middle = array(str('u'), '[0., 1. , 2.5, 4. ]')

expected_same = array(str('u'), '[2.5]')
same_val = 'valid'


if __name__=='__main__':
    unittest.main()
