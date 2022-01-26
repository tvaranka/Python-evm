import unittest
import numpy as np

import py_evm


class TestEVM(unittest.TestCase):
    def test_same_shape(self):
        video = np.ones((2, 32, 32, 3))
        mm_video = py_evm.magnify(video)
        self.assertEqual(mm_video.shape, video.shape)
        
    def test_static_video(self):
        video = np.ones((2, 32, 32, 3))
        mm_video = py_evm.magnify(video)
        self.assertEqual(mm_video.sum(), video.sum())
        
    def test_weird_size(self):
        video = np.ones((2, 155, 37, 3))
        mm_video = py_evm.magnify(video)
        self.assertEqual(mm_video.sum(), video.sum())
        
    def test_weird_size2(self):
        video = np.ones((2, 55, 89, 3))
        mm_video = py_evm.magnify(video)
        self.assertEqual(mm_video.sum(), video.sum())
    
    
if __name__ == '__main__':
    unittest.main()