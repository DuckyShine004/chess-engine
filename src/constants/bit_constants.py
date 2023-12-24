OCCUPANCIES = 512
MAGIC_NUMBERS = 4096

BIT_16_MASK = 0xFFFF
BIT_32_MASK = 0xFFFFFFFF
BIT_64_MASK = 0xFFFFFFFFFFFFFFFF

SOURCE_SQUARE_OFFSET = 0x3F
TARGET_SQUARE_OFFSET = 0xFC0
PIECE_OFFSET = 0xF000
PROMOTED_PIECE_OFFSET = 0xF0000
CAPTURE_FLAG_OFFSET = 0x100000

BISHOP_RELEVANT_BITS = [
    6,
    5,
    5,
    5,
    5,
    5,
    5,
    6,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    7,
    7,
    7,
    7,
    5,
    5,
    5,
    5,
    7,
    9,
    9,
    7,
    5,
    5,
    5,
    5,
    7,
    9,
    9,
    7,
    5,
    5,
    5,
    5,
    7,
    7,
    7,
    7,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    6,
    5,
    5,
    5,
    5,
    5,
    5,
    6,
]

ROOK_RELEVANT_BITS = [
    12,
    11,
    11,
    11,
    11,
    11,
    11,
    12,
    11,
    10,
    10,
    10,
    10,
    10,
    10,
    11,
    11,
    10,
    10,
    10,
    10,
    10,
    10,
    11,
    11,
    10,
    10,
    10,
    10,
    10,
    10,
    11,
    11,
    10,
    10,
    10,
    10,
    10,
    10,
    11,
    11,
    10,
    10,
    10,
    10,
    10,
    10,
    11,
    11,
    10,
    10,
    10,
    10,
    10,
    10,
    11,
    12,
    11,
    11,
    11,
    11,
    11,
    11,
    12,
]

BISHOP_MAGIC_NUMBERS = [
    0x40040844404084,
    0x2004208A004208,
    0x10190041080202,
    0x108060845042010,
    0x581104180800210,
    0x2112080446200010,
    0x1080820820060210,
    0x3C0808410220200,
    0x4050404440404,
    0x21001420088,
    0x24D0080801082102,
    0x1020A0A020400,
    0x40308200402,
    0x4011002100800,
    0x401484104104005,
    0x801010402020200,
    0x400210C3880100,
    0x404022024108200,
    0x810018200204102,
    0x4002801A02003,
    0x85040820080400,
    0x810102C808880400,
    0xE900410884800,
    0x8002020480840102,
    0x220200865090201,
    0x2010100A02021202,
    0x152048408022401,
    0x20080002081110,
    0x4001001021004000,
    0x800040400A011002,
    0xE4004081011002,
    0x1C004001012080,
    0x8004200962A00220,
    0x8422100208500202,
    0x2000402200300C08,
    0x8646020080080080,
    0x80020A0200100808,
    0x2010004880111000,
    0x623000A080011400,
    0x42008C0340209202,
    0x209188240001000,
    0x400408A884001800,
    0x110400A6080400,
    0x1840060A44020800,
    0x90080104000041,
    0x201011000808101,
    0x1A2208080504F080,
    0x8012020600211212,
    0x500861011240000,
    0x180806108200800,
    0x4000020E01040044,
    0x300000261044000A,
    0x802241102020002,
    0x20906061210001,
    0x5A84841004010310,
    0x4010801011C04,
    0xA010109502200,
    0x4A02012000,
    0x500201010098B028,
    0x8040002811040900,
    0x28000010020204,
    0x6000020202D0240,
    0x8918844842082200,
    0x4010011029020020,
]

ROOK_MAGIC_NUMBERS = [
    0x8A80104000800020,
    0x140002000100040,
    0x2801880A0017001,
    0x100081001000420,
    0x200020010080420,
    0x3001C0002010008,
    0x8480008002000100,
    0x2080088004402900,
    0x800098204000,
    0x2024401000200040,
    0x100802000801000,
    0x120800800801000,
    0x208808088000400,
    0x2802200800400,
    0x2200800100020080,
    0x801000060821100,
    0x80044006422000,
    0x100808020004000,
    0x12108A0010204200,
    0x140848010000802,
    0x481828014002800,
    0x8094004002004100,
    0x4010040010010802,
    0x20008806104,
    0x100400080208000,
    0x2040002120081000,
    0x21200680100081,
    0x20100080080080,
    0x2000A00200410,
    0x20080800400,
    0x80088400100102,
    0x80004600042881,
    0x4040008040800020,
    0x440003000200801,
    0x4200011004500,
    0x188020010100100,
    0x14800401802800,
    0x2080040080800200,
    0x124080204001001,
    0x200046502000484,
    0x480400080088020,
    0x1000422010034000,
    0x30200100110040,
    0x100021010009,
    0x2002080100110004,
    0x202008004008002,
    0x20020004010100,
    0x2048440040820001,
    0x101002200408200,
    0x40802000401080,
    0x4008142004410100,
    0x2060820C0120200,
    0x1001004080100,
    0x20C020080040080,
    0x2935610830022400,
    0x44440041009200,
    0x280001040802101,
    0x2100190040002085,
    0x80C0084100102001,
    0x4024081001000421,
    0x20030A0244872,
    0x12001008414402,
    0x2006104900A0804,
    0x1004081002402,
]
