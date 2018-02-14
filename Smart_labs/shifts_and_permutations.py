
message = "EPLCG BTENC ULVFN AVAGR ERFGV ATFHO WRPG"

char_low_start = ord('a')
char_high_start = ord('A')
cnt_symbols = 26

def shift_decode(msg, offset):
    sh_msg = [chr(char_high_start + (ord(x) + offset - char_high_start) % cnt_symbols) if x != ' ' else ' ' for x in msg]
    return ''.join(sh_msg)


for i in range(1, cnt_symbols):
    print(i, shift_decode(message, i))
# print(ord('a'), 1)
