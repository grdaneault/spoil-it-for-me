from app.model import Media, Character

game_of_thrones = Media(
    media_id=1,
    media_type="tv",
    title="Game of Thrones",
    characters=[
        Character(name="Tyrion Lannister", actor="Peter Dinklage", episodes=67),
        Character(name="Cersei Lannister", actor="Lena Headey", episodes=62),
        Character(name="Daenerys Targaryen", actor="Emilia Clarke", episodes=62),
        Character(name="Jon Snow", actor="Kit Harington", episodes=62),
        Character(name="Sansa Stark", actor="Sophie Turner", episodes=60),
        Character(name="Arya Stark", actor="Maisie Williams", episodes=59),
        Character(name="Jaime Lannister", actor="Nikolaj Coster-Waldau", episodes=55),
        Character(name="Jorah Mormont", actor="Iain Glen", episodes=52),
        Character(name="Samwell Tarly", actor="John Bradley", episodes=48),
        Character(name="Theon Greyjoy", actor="Alfie Allen", episodes=47),
        Character(name="Lord Varys", actor="Conleth Hill", episodes=46),
        Character(name="Brienne of Tarth", actor="Gwendoline Christie", episodes=42),
        Character(name="Petyr 'Littlefinger' Baelish", actor="Aidan Gillen", episodes=41),
        Character(name="Davos Seaworth", actor="Liam Cunningham", episodes=41),
        Character(name="Bran Stark", actor="Isaac Hempstead Wright", episodes=41),
        Character(name="Sandor 'The Hound' Clegane", actor="Rory McCann", episodes=38),
        Character(name="Missandei", actor="Nathalie Emmanuel", episodes=38),
        Character(name="Bronn", actor="Jerome Flynn", episodes=37),
        Character(name="Eddison Tollett", actor="Ben Crompton", episodes=34),
        Character(name="Podrick Payne", actor="Daniel Portman", episodes=34),
        Character(name="Grey Worm", actor="Jacob Anderson", episodes=33),
        Character(name="Tormund Giantsbane", actor="Kristofer Hivju", episodes=32),
        Character(name="Grand Maester Pycelle", actor="Julian Glover", episodes=31),
        Character(name="Melisandre", actor="Carice van Houten", episodes=29),
        Character(name="Gilly", actor="Hannah Murray", episodes=28),
        Character(name="Tywin Lannister", actor="Charles Dance", episodes=27),
        Character(name="The Dragons", actor="", episodes=0)
    ],
    settings=[
        "Westeros",
        "Kings Landing",
        "The iron throne"
    ],
    custom_spoilers=[
        "{{ctx.character}} becomes a whitewalker",
        "{{ctx.character}} becomes the ruler of the seven realms",
        "{{ctx.character}} beheads {{ctx.character}} in a totally epic battle",
        "{{ctx.character}} stands up to {{ctx.character}} and is killed for it",
        "{{ctx.character}} has a child with {{ctx.character}}",
        "{{ctx.character}} becomes the new king of the north.",
        "{{ctx.setting}} falls to the ice king's army",
        "{{ctx.setting}} is burned by the dragons"
    ],
    images=[
        "https://timedotcom.files.wordpress.com/2019/05/game-of-thrones-season-8-episode-5-davos-jon-snow.jpg",
        "https://media.wired.com/photos/5cd0792e2c82ec474dc7bb5e/master/pass/Culture_GameOfThronesRecap_Ep4.jpg",
        "https://timedotcom.files.wordpress.com/2019/02/game-of-thrones-season-8-photos-01.jpg",
        "https://media.npr.org/assets/img/2019/04/14/1fa22a3eec708fb6ea43efb7dfe060fec9b3641c42b85e218c37fe70262f709d_wide-5f5ad5b9676dcbec05bb6dfc6c66f2daad766c79.jpg?s=1400"
    ]
)
