>>> struct.pack('B'*12,
                *(random.randrange(0, 256)
                for i in range(12))
 ).decode('utf-8')