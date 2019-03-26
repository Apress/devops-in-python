@attr.s
class FakeSimpleSocket:

    _chunk_size = attr.ib()

    _received = attr.ib(init=False, factory=list)

    _to_send = attr.ib()

    def connect(self, addr):
        pass

    def send(self, blob):
        actually_sent = blob[:chunk_size]
        self._received.append(actually_sent)
        return len(actually_sent)

    def recv(self, max_size):
        chunk_size = min(max_size, self._chunk_size)
        received, self._to_send = (self._to_send[:chunk_size],
                                   self._to_send[chunk_size:])
        return received