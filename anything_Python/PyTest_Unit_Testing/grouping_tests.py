class TestClass:
    """How you can group your tests in a class"""
    def test_one(self):
        x = "edureka"
        assert 'r' in x
    
    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
