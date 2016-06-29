class CP037:
    table = (
        '\u0000\u0001\u0002\u0003\u009C\u0009\u0086\u007F\u0097\u008D\u008E\u000B\u000C\u000D\u000E\u000F'
        '\u0010\u0011\u0012\u0013\u009D\u0085\u0008\u0087\u0018\u0019\u0092\u008F\u001C\u001D\u001E\u001F'
        '\u0080\u0081\u0082\u0083\u0084\u000A\u0017\u001B\u0088\u0089\u008A\u008B\u008C\u0005\u0006\u0007'
        '\u0090\u0091\u0016\u0093\u0094\u0095\u0096\u0004\u0098\u0099\u009A\u009B\u0014\u0015\u009E\u001A'
        '\u0020\u00A0âäáàãå\u00E7ñ\u00A2.<(+|'
        '&éêëèíîïì\u00DF!$*);\u00AC'
        '-/ÂÄÀÁÃÅ\u00C7Ñ\u00A6,%_>?'
        "\u00F8ÉÊËÈÍÎÏÌ`:#@'=\u0022"
        '\u00D8abcdefghi\u00AB\u00BB\u00F0\u00FD\u00FE\u00B1'
        '\u00B0jklmnopqr\u00AA\u00BA\u00E6\u00B8\u00C6\u00A5'
        '\u00B5~stuvwxyz\u00A1\u00BF\u00D0\u00DD\u00DE\u00AE'
        '^\u00A3\u00A5\u00B7\u00A9\u00A7\u00B6\u00BC\u00BD\u00BE\u005B\u005D\u00AF¨´\u00D7'
        '{ABCDEFGHI\u00ADôöòóõ'
        '}JKLMNOPQR\u00B9ûüùúÿ'
        '\u005c\u00F7STUVWXYZ\u00B2ÔÖÒÓÕ'
        '0123456789\u00B3ÛÜÙÚ\u009F'
    )

    def ord(self, c):
        return self.table.find(c)

    def chr(self, o):
        if not 0 <= 0 < 256:
            raise ValueError
        return self.table[o]

    def from_unicode(self, s):
        r = []
        for c in s:
            if c in self.table:
                r.append(self.ord(c))
            else:
                r.extend(c.encode('utf-8'))
        return r
