L1 = ['Alti Elfi',
      'Skaven',
      'Elfi Silvani',
      'Uomini Lucertola',
      'Guerrieri del Caos',
      'Khorne Bloodbound',
      'Stormcast Eternal',
      'Nani',
      'Kharadron Overlords',
      # 'Silver Tower',
      ]
L2 = ['Eldar',
      'Angeli Oscuri',
      'Space Marine del Caos',
      'Space Wolves',
      'Orki',
      'Angeli Sanguinari',
      'Tiranidi',
      # 'Officio Assassinorum',
      # 'Ultramarines',
      # 'Word Bearers',
      'Deathwatch',
      'Imperial Knights',
      'Thousand Sons',
      'Space Marines']
# L3 = ['Tempesta di Magia', 'Dreadfleet']
L4 = ['Elementi Scenici',           # 0
      'Board Game',                 # 1
      'Avatar of War',              # 2 
      'Confrontation',              # 3
      'Andrea Miniatures',          # 4
      'Miniaturas Beneito',         # 5
      'Airfix',                     # 6
      'Pegaso Models',              # 7
      'Bones',                      # 8
      'Maxmini',                    # 9
      'Bandai',                     # 10
      'Black Dog',                  # 11 
      'Masterclass',                # 12
      'Arcadia Quest',              # 13
      'Tamiya',                     # 14
      'HobbyBoss',                  # 15
      'Trumpeter',                  # 16
      'Dragon',                     # 17
      'Italeri',                    # 18
      'Mirror Models',              # 19
      'Academy',                    # 20
      'Bronco Models',              # 21
      'Tristar',                    # 22
      'Aitna Model',                # 23
      'EMI',                        # 24
      'Tartar',                     # 25
      'Alpine Miniatures',          # 26
      'Dungeon Saga',               # 27
      'Mitches Military Models',    # 28
      'Blood Bowl',                 # 29
      'MiniArt',                    # 30
      'AFV Club',                   # 31
      'Eduard',                     # 32
      ]

NUMERO_TOTALE_DI_MINIATURE = 300  # arrotondare per eccesso

OFFSET_TRUPPE = 1  # 1 WHF - 2 WH40K
OFFSET_WHF_TRUPPE = 2
OFFSET_WH40K_TRUPPE = 3

OFFSET_ELITE = 10
OFFSET_WHF_ELITE = 2
OFFSET_WH40K_ELITE = 2
OFFSET_Scenici = 0
OFFSET_Dread_Fleet = 0
OFFSET_Blood_Bowl = 0
OFFSET_Fantasy = 3
OFFSET_Storico = 6
OFFSET_WWII = 15
OFFSET_Moderno = 4
OFFSET_Scify = 11
OFFSET_Board_Game = 0

STATI = (('DI', 'Da Iniziare'),
         ('IC', 'In Corso'),
         ('FI', 'Finito')
         )

TIPI = (('whft', 'WHF Truppa'),
        ('whfe', 'WHF Elite'),
        ('wh40kt', 'WH40k Truppa'),
        ('wh40ke', 'WH40k Elite'),
        ('scc', 'Scenici'),
        ('df', 'Dread Fleet'),
        ('bb', 'Blood Bowl'),
        ('fsy', 'Fantasy'),
        ('stco', 'Storico'),
        ('ww2', 'WWII'),
        ('mno', 'Moderno'),
        ('scfy', 'Scify'),
        ('bg', 'Board Game')
        )