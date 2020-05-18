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

    def test_decimate_by_2(self):
        print("kaiser2")
        output_downsample = downsample_by_2(input_convolve, kaiser_input)
        output_decimate = decimate_by_2(output_downsample, 2)
        self.assertNotEqual(output_decimate.round(1).tolist(), expected_decimation)


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

expected_decimation = [-0.0178963, 0.0279011, -0.0945022,
                    0.11822447, -0.12036858, 0.07817547,
                    0.00512128, -0.13115076, 1.76920539,
                    1.50712101, -0.24958513,  0.06456389,
                    0.01051083, -0.04265658,  0.04526048,
                    -0.04823651,  0.02875602]




if __name__=='__main__':
    unittest.main()
