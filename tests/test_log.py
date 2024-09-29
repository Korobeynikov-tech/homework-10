from src.decorators import log


def test_log():
    @log()
    def test_func(a, b):
        return a + b

    test_func(1, 2)
    test_func(3, "a")


def test_log_file():
    @log("logfile.txt")
    def test_func2(a, b):
        return a / b

    test_func2(4, 2)
    test_func2(5, 0)
