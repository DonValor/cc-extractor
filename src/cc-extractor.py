#!/usr/bin/env python3

# Program for extracting the NES roms of each game in the Konami Collector's Series:
# Castlevania & Contra PC CD-ROM

# iNES Headers for Castlevania, Castlevania II, Castlevania III, Contra, Super C and Jackal

HEADERS = [
    b'\x4E\x45\x53\x1A\x08\x00\x21\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    b'\x4E\x45\x53\x1A\x08\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    b'\x4E\x45\x53\x1A\x10\x10\x50\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    b'\x4E\x45\x53\x1A\x08\x00\x21\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    b'\x4E\x45\x53\x1A\x08\x10\x41\x00\x00\x00\x00\x00\x00\x00\x00\x00',
    b'\x4E\x45\x53\x1A\x08\x00\x21\x00\x00\x00\x00\x00\x00\x00\x00\x00'
]

# Offsets for each game's ROM in the .exe file
# v1.0.0.1  OFFSET      SIZE             OFFSET      SIZE
OFFSETS = [
    {'PRG': [0x001E570, 0x20000], 'CHA': None},
    {'PRG': [0x003E570, 0x20000], 'CHA': [0x005E570, 0x20000]},
    {'PRG': [0x007E570, 0x40000], 'CHA': [0x00BE570, 0x20000]},
    {'PRG': [0x00DE570, 0x20000], 'CHA': None},
    {'PRG': [0x011E580, 0x20000], 'CHA': [0x013E580, 0x20000]},
    {'PRG': [0x00FE580, 0x20000], 'CHA': None}
]

# Game names
GAMES = [
    'Castlevania',
    'Castlevania II - Simon\'s Quest',
    'Castlevania III - Dracula\'s Curse',
    'Contra',
    'Super C',
    'Jackal'
]

if __name__ == '__main__':
    f = open("cc.exe", "rb")
    try:
        exe = f.read()
    finally:
        f.close()
    
    for i, game in enumerate(HEADERS):
        for section in ['PRG', 'CHA']:
            if OFFSETS[i][section]:
                start = OFFSETS[i][section][0]
                size = OFFSETS[i][section][1]
                end = start + size
                game += exe[start:end]
        
        out = open(GAMES[i] + " (Konami Collector's Series).nes", "wb")
        
        try:
            out.write(game)
        finally:
            out.close()
