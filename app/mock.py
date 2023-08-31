from datetime import datetime
from slugify import slugify
from sqlalchemy import create_engine, MetaData, Table
from config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
meta = MetaData()
meta.reflect(bind=engine)
connect = engine.connect()

posts = Table('blog_posts', meta, autoload_with=engine)
categories = Table('blog_categories', meta, autoload_with=engine)
authors = Table('account_users', meta, autoload_with=engine)


rows_authors = [
    {
        'firstname': 'Renaud',
        'lastname': 'Dupont',
        'username': 'Renaud D.',
        'email': 'dom@dom.com',
        'slug': 'renaud-dupont'
    },
    {
        'firstname': 'Christophe',
        'lastname': 'Martin',
        'username': 'Christophe M.',
        'email': 'dom@ddd.com',
        'slug': 'christophe-martin'
    },
    {
        'firstname': 'Claude',
        'lastname': 'Durant',
        'username': 'visiteur',
        'email': 'dom@domdom.com',
        'slug': 'claude-durant'
    },
]

connect.execute(authors.insert(), rows_authors)
connect.commit()

rows_categories = [
    {'name': 'jazz'},
    {'name': 'blues'},
    {'name': 'trip-hop'},
]
connect.execute(categories.insert(), rows_categories)
connect.commit()


rows_posts = [
    {
        'title': "Qui était Django Reinhardt",
        'content': """
Jean Reinhardt, plus connu sous le nom de Django Reinhardt, est un guitariste de jazz français né le 23 janvier 1910 à Liberchies1 — aujourd'hui une section de la commune de Pont-à-Celles — dans l'arrondissement de Charleroi en Belgique2,3 et mort le 16 mai 1953 à Fontainebleau4. Son style de jeu et de composition a été suivi d'adeptes, donnant naissance à un style de jazz à part entière, le jazz manouche.

Issu d’une famille sinténote 1 et communément appelée en France « manouche », il est encore aujourd’hui un des guitaristes les plus respectés et influents de l’histoire du jazz. Grièvement blessé dans l'incendie de sa roulotte, il garde toute sa vie les séquelles de ses brûlures à la main gauche qui l'obligent à trouver une nouvelle technique et à jouer dans un style si particulier que ses adeptes des générations suivantes poussent l'idolâtrie jusqu'à s'entraver les doigts pour reproduire son infirmité et sa technique5.

Plusieurs de ses descendants sont devenus guitaristes : Lousson Reinhardt, son fils aîné issu d'un premier mariage (1929-1992), Babik Reinhardt, son second fils (1944-2001), et David Reinhardt, son petit-fils (fils de Babik), ainsi que Levis Adel-Baumgartner descendant de Lousson.
""",
    "categories": 1,
    "online": 1,
    "authors": 1,
    "created": datetime.now(),
    "updated": datetime.now(),
    "slug": slugify("Qui était Django Reinhardt")
    },
    {
        'title': "Miles Davis, ce génie",
        'content': """
Miles Dewey Davis III, généralement dit Miles Davis /maɪlz ˈdju.i ˈdeɪ.vɪs ðə θɝd/1, né le 26 mai 1926 à Alton (Illinois), et mort le 28 septembre 1991 à Santa Monica (Californie), est un compositeur et trompettiste de jazz américain.

Miles Davis commence à jouer de la trompette à l'âge de treize ans. Il fut à la pointe de beaucoup d'évolutions dans le jazz et s'est particulièrement distingué par sa capacité à découvrir et à s'entourer de nouveaux talents. Son jeu se caractérise par une grande sensibilité musicale et par la fragilité qu'il arrive à donner au son. Il marque l'histoire du jazz et de la musique du XXe siècle. Beaucoup de grands noms du jazz des années 1940 à 1980 travaillent avec lui.

Les différentes formations de Miles Davis sont comme des laboratoires au sein desquels se sont révélés les talents de nouvelles générations et les nouveaux horizons de la musique moderne ; notamment Sonny Rollins, Julian « Cannonball » Adderley, Bill Evans et John Coltrane durant les années 1950. De 1960 aux années 1980, ses sidemen seront Herbie Hancock, Wayne Shorter, George Coleman, Chick Corea, John McLaughlin, Keith Jarrett, Tony Williams, Joe Zawinul, Dave Liebman et Kenny Garrett ; c'est avec eux qu'il s'oriente vers le jazz fusion, dont il reste l'un des pionniers. La découverte de la musique de Jimi Hendrix est déterminante dans cette évolution, mais surtout le choc du festival de Newport, en 1969, où l'on assiste à l'origine exclusivement à des concerts de jazz, mais qui, cette année-là, programme du rock.
""",
    "categories": 1,
    "online": 1,
    "created": datetime.now(),
    "updated": datetime.now(),
    "slug": slugify("Miles Davis, ce génie"),
    "authors": 2
    },
    {
        'title': "B. B. King",
        'content': """
B.B. King (pour Blues Boy), de son vrai nom Riley B. King, né le 16 septembre 1925 à Itta Bena, dans le Mississippi aux États-Unis, et mort le 14 mai 2015 à Las Vegas, est un guitariste, compositeur et chanteur de blues américain. Il est considéré comme l'un des meilleurs musiciens de blues, et a eu une influence considérable sur de nombreux guitaristes.

Il est, avec Albert King et Freddie King, un des trois « kings » de la guitare blues.
""",
    "categories": 2,
    "online": 1,
    "created": datetime.now(),
    "updated": datetime.now(),
    "slug": slugify("B. B. King"),
    "authors": 1
    },
    {
        'title': "Massive Attack",
        'content': """
Massive Attack est un groupe musical britannique formé en 1988, originaire de Bristol, précurseur de la musique trip hop. Il se compose, à l'origine, de Robert Del Naja (3D), Adrian Thaws (Tricky), Grant Marshall (Daddy G) et Andrew Vowles (Mushroom). Le style du groupe est en constante évolution : au début proche du hip-hop, du groove, voire de la soul, il aborde par la suite la musique électronique, et un son plus électrique à la fin des années 1990. Chaque album est enrichi par de très nombreuses collaborations et la participation systématique de Horace Andy.

Le musicien Adrian Thaws (Tricky) quitte le groupe en 1994 après la sortie de l'album Protection. En désaccord avec l'évolution du style musical, Andrew Vowles (Mushroom) quitte le groupe en 1998, à la sortie de l'album Mezzanine.

Le groupe sort cinq albums studio, de 1991 à 2010, ainsi que plusieurs albums remix, singles et maxis.
""",
    "categories": 3,
    "online": 1,
    "created": datetime.now(),
    "updated": datetime.now(),
    "slug": slugify("Massive Attack"),
    "authors": 2
    },
    {
        'title': "Portishead",
        'content': """
Le groupe se forme en 1991, lorsque Geoff Barrow rencontre la chanteuse Beth Gibbons. Ils forment un duo et choisissent pour nom celui de la ville côtière dans laquelle a grandi Geoff Barrow : Portishead dans le Somerset, à 20 kilomètres à l'ouest de Bristol1. Ils enregistrent leurs premiers titres aidés par le guitariste Adrian Utley, venu du jazz, et d'un ingénieur du son, Dave McDonald.

L'orientation musicale de Barrow est liée à ses différentes expériences en studio. Il a notamment travaillé en tant qu'assistant au studio d'enregistrement Coach House Studios, durant l'enregistrement de l'album Blue Lines de Massive Attack1. Sa technique de production, non conventionnelle à l'époque, se base sur des enregistrements bruts qu'il enrichit avec des effets et des échantillons1.

Utley devient un membre à part entière, participant à l'écriture et à la production2.
""",
    "categories": 3,
    "online": 1,
    "created": datetime.now(),
    "updated": datetime.now(),
    "slug": slugify("Portishead"),
    "authors": 2
    },
    {
        'title': "Archive",
        'content': """
Archive est formé en 1994 comme groupe de trip hop sous l'impulsion de Darius Keeler et Danny Griffiths aux côtés de Roya Arab et du rappeur Rosko John2. Après avoir publié quelques singles sous leur propre label, ils se séparent au début de 1996.

Quelques mois plus tard, le groupe se reforme avec du nouveau personnel. Le premier album, Londinium, sort en 1996 chez Island Records, label de PolyGram (désormais Universal Music) avec la chanteuse Roya Arab et le rappeur Rosko John. C'est un mélange entre du trip hop très sombre (trip hop de Bristol, dans la même lignée que le premier album du groupe Massive Attack) et du rap. Londinium est devenu aujourd'hui un incontournable en matière de trip hop, le chant rap sur une musique expérimentale lui donnant une sonorité particulière.
""",
    "categories": 3,
    "online": 1,
    "created": datetime.now(),
    "updated": datetime.now(),
    "slug": slugify( "Archive"),
    "authors": 1
    },
    {
        'title': "Chick Corea",
        'content': """
Chick Corea (nom de scène d'Armando Anthony Corea), né le 12 juin 1941 à Chelsea (Massachusetts) et mort le 9 février 2021 à Tampa Bay (Floride)1, est un pianiste, claviériste et compositeur américain de jazz et jazz fusion.

En tant que membre du groupe de Miles Davis dans les années 1960, il a participé à la naissance du jazz-rock. Avec Herbie Hancock, McCoy Tyner et Keith Jarrett, il est considéré comme un des pianistes les plus influents depuis les années 1970.

C'est également un excellent pianiste classique, même s'il n'a enregistré que très peu dans ce domaine.
""",
    "categories": 1,
    "online": 1,
    "created": datetime.now(),
    "updated": datetime.now(),
    "slug": slugify("Chick Corea"),
    "authors": 2
    },
    {
        'title': "Herbie Hancock",
        'content': """
Herbert Hancock, dit Herbie, est un pianiste claviériste et compositeur américain de jazz, né le 12 avril 1940 à Chicago dans l'Illinois. Il est l'un des musiciens de jazz les plus importants et influents de sa génération, en mêlant au jazz, notamment, des éléments de soul, de funk, de rock et de disco.

Herbie Hancock a joué avec de nombreux grands jazzmen dans les années 1960 et a rejoint le Miles Davis quintet, avec lequel il a redéfini le rôle de la section rythmique. Il a également été un des premiers à utiliser les synthétiseurs et le scratch. Malgré ses expérimentations, la musique d'Herbie Hancock est restée mélodique et accessible, rencontrant parfois des succès commerciaux, avec en particulier les pièces Cantaloupe Island, Watermelon Man, Chameleon et Rockit.

Il est aussi acteur, on l'a vu dans des films tels que Autour de minuit, Hitters et Miles Ahead et plus récemment dans Valérian et la Cité des mille planètes de Luc Besson.
""",
    "categories": 1,
    "online": 1,
    "created": datetime.now(),
    "updated": datetime.now(),
    "slug": slugify("Herbie Hancock"),
    "authors": 1
    },
    {
        'title': "Albert King",
        'content': """
lbert Nelson est né dans une famille modeste à Indianola dans le Mississippi près d'une plantation de coton où il travaille pendant sa jeunesse. Ses premières influences musicales lui viennent de son père, Will Nelson, qui joue de la guitare. Pendant son enfance, il chante également à l'église dans un groupe de gospel. Il commence sa carrière professionnelle avec un groupe appelé In the Groove Boys à Osceola dans l'Arkansas.

Son premier succès est la chanson I'm A Lonely Man sortie en 1959. Il doit cependant attendre 1961 et la sortie de Don't Throw Your Love on Me So Strong pour devenir célèbre et atteindre la quatorzième place des classements de R&B. En 1966, il signe pour le label Stax pour lequel il sort en 1967 son album Born Under A Bad Sign. La chanson titre de cet album (écrite par Booker T. Jones et William Bell) devient le morceau le plus connu d’Albert King et il sera repris par de nombreux artistes, entre autres (de Cream à Jimi Hendrix).
""",
    "categories": 2,
    "online": 1,
    "created": datetime.now(),
    "updated": datetime.now(),
    "slug": slugify("Albert King"),
    "authors": 1
    },
    {
        'title': "John Lee Hooker",
        'content': """
John Lee Hooker, né le 22 août 1917 à Clarksdale (Mississippi, États-Unis), et mort le 21 juin 2001 à Los Altos (Californie, États-Unis), est un guitariste et chanteur de blues américain. Son style, unique et authentique à la fois, en a fait l'un des artistes les plus importants de cette musique, et son influence sur le blues rock et le rock durant tout le XXe siècle est considérable.

Parmi ses titres les plus connus : Boogie Chillen (1948), I'm in the Mood (1951) et Boom Boom (1962), les deux premiers s’étant classés no 1 dans les charts (diagrammes des ventes) R&B du Billboard magazine. En France, Shake It Baby a remporté un certain succès en 1963 et a longtemps fait danser dans les boums ou surboums des années 1960.

John Lee Hooker entre au Rock and Roll Hall of Fame en 19911.
""",
    "categories": 2,
    "online": 1,
    "created": datetime.now(),
    "updated": datetime.now(),
    "slug": slugify("John Lee Hooker"),
    "authors": 1
    },
    {
        'title': "Charlie Parker",
        'content': """
Charlie Parker (Charles Christopher Parker, Jr.)1 surnommé Bird (l'oiseau) ou Yardbird2, né le 29 août 1920 à Kansas City et mort le 12 mars 1955 à New York3, est un saxophoniste alto emblématique du jazz américain. Il est l'un des fondateurs du style bebop. Avec entre autres Louis Armstrong, Duke Ellington et Miles Davis, il est considéré comme un des jazzmen les plus influents de l'histoire du jazz.

Dans les années 1940, Charlie Parker et Dizzy Gillespie ont assis les premiers éléments du jazz moderne en participant activement à l'émergence du bebop, une forme de jazz caractérisée par des tempos rapides, une grande technicité et une improvisation basée sur la structure harmonique. Les nouvelles approches proposées par Parker sur la mélodie, le rythme et l'harmonie ont considérablement influencé les musiciens contemporains.
""",
    "categories": 1,
    "online": 1,
    "created": datetime.now(),
    "updated": datetime.now(),
    "slug": slugify("Charlie Parker"),
    "authors": 1
    },
]

connect.execute(posts.insert(), rows_posts)
connect.commit()

r = connect.execute(posts.select()).fetchall()
