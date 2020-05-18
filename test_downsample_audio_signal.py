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
        the two across one another
        For Downsample.
        """
        output_decimate= downsample_by_2(input_convolve, input_convolve2)
        self.assertEqual(output_decimate.tolist(), expected_convolve1)

    def test_decimate_middle(self):
        """
        Tests Contains boundary effecs,
        where zeros are taken into account
        For Downsample.
        """
        output_middle = downsample_by_2(input_conv_middle, input_conv_middle2, middle_val)
        self.assertEqual(output_middle.tolist(), expected_conv_middle)

    def test_decimate_same(self):
        """
        Test same length, so there is only one position
        where they completely overlap for Downsample.
        """
        output_same = downsample_by_2(input_conv_middle, input_conv_middle2, same_val)
        self.assertEqual(output_same, expected_same)

    def test_filter_kaiser(self):
        """
        Test Kaiser approach
        """
        print("kaiser")
        output_kaiser = downsample_by_2(input_convolve, kaiser_input)
        self.assertEqual.__self__.maxDiff = None


# Test variables
input_convolve = [1, 2, 3]
input_convolve2 = [0, 1, 0.5]
expected_convolve1 = [0.,  1.,  2.5, 4.,  1.5]


input_conv_middle = [1,2,3]
input_conv_middle2 = [0,1,0.5]
middle_val = 'same'
expected_conv_middle  = [1.,  2.5, 4. ]


expected_same = array('f', [2.5])
same_val = 'valid'

kaiser_input = [-0.01452123, -0.0155227 , 0.01667252,
        0.01800633, -0.01957209,-0.0214361 , 0.02369253,
        0.02647989, -0.03001054, -0.03462755, 0.04092347,
        0.05001757, -0.06430831, -0.09003163, 0.15005272,
        0.45015816, 0.45015816, 0.15005272, -0.09003163,
        -0.06430831, 0.05001757, 0.04092347, -0.03462755,
        -0.03001054, 0.02647989, 0.02369253, -0.0214361,
        -0.01957209, 0.01800633, 0.01667252, -0.0155227,
        -0.01452123]

expected_kaiser = [-0.01452123, -0.04456516, -0.05793657,
                    0.00478327,  0.06645813, -0.00656129,
                    -0.07789594,  0.00955665,  0.09402683,
                    -0.01520896, -0.11836325,  0.02798186,
                    0.15849724, -0.06859554, -0.22293547,
                    0.48016871,  1.80063264,  2.40084352,
                    1.56054829, 0.20578659, -0.34869394,
                    -0.05196632,  0.1972721,   0.02350477,
                    -0.13742384, -0.01337931,  0.10538863,
                    0.0086333,  -0.08544615, -0.00603109,
                    0.07184133,  0.00445093, -0.07561056,
                    -0.04356369]



if __name__=='__main__':
    unittest.main()
