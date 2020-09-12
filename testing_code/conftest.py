import pytest

@pytest.fixture()
def login():
    print("登陆方法")
    # yield 生成器，激活fixture teardown 方法
    yield ['username','password']
    print("teardown")