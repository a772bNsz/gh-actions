"""
test for maya version
"""

import unittest
from pymel import versions

maya_version = versions.current()


class SampleTest(unittest.TestCase):
    @unittest.skipIf(20180000 != maya_version, "test_version_is_2018")
    def test_version_is_2018(self):
        self.assertEqual(20180000, maya_version)

    @unittest.skipIf(201602 != maya_version, "test_version_is_2016sp1")
    def test_version_is_2016sp1(self):
        self.assertEqual(201602, maya_version)


if __name__ == '__main__':
    unittest.main()
