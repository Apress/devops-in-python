class DummyFile:

    def __init__(self):
        self.written = []

    def write(self, thing):
        self.written.append(thing)

def test_write_numbers():
    fout = DummyFile()
    write_numbers(fout)
    assert_that(fout.written, is_(["1\n", "2\n", "3\n"]))