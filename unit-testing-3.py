class DummyFile:

    def __init__(self):
        self.written = []

    def write(self, thing):
        self.written.append(thing)

def test_write_numbers():
    fout = DummyFile()
    write_numbers(fout)
    assert_that("".join(fout.written), is_("1\n2\n3\n"))