class _Getch:
    # class of character getter is used to receiving pressed keys from keyboard
    def __init__(self):
        self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    # class of character getter version for UNIX

    def __init__(self):
        pass

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
