#测试文件
import sys

import pytest

print(sys.path.append('..'))

from dev_code.calc import Calculator

def setup_module():
    print("模块级别 setup")
def teardown_module():
    print("模块级别 teardown")
def setup_function():
    print("函数级别 setup")
def teardown_function():
    print("函数级别 teardown")


class TestCalc:
    def setup_class(self):
        self.cal = Calculator()
        print("类级别 setup")
    def teardown_class(self):
        print("类级别 teardown")

    def setup(self):
        print("setup")
    def teardown(self):
        print("teardown")

    @pytest.mark.add
    @pytest.mark.parametrize('a, b, result',[
        (1,1,2),
        (3,3,6),
        (-1,-1,-2),
        (0.1,0.1,0.2)
    ]
    ,ids=['int','int','minus','float'])

    @pytest.mark.add
    def test_add_02(self, a, b, result):
        #cal = Calculator()
        assert result == self.cal.add(a, b)

    @pytest.mark.add
    def test_add(self):
        #cal = Calculator()
        assert 2 == self.cal.add(1,1)

    @pytest.mark.add
    def test_add_01(self):
        #cal = Calculator()
        assert 3 == self.cal.add(1,2)

    @pytest.mark.div
    def test_div(self):
        #cal = Calculator()
        assert 1 == self.cal.div(1,1)
