from app.model import Media, Character, Setting

game_of_thrones = Media(
    media_id=1,
    media_type="tv",
    title="Game of Thrones",
    characters=[
        Character(name="Tyrion Lannister", actor="Peter Dinklage", episodes=67, image="https://cdn.vox-cdn.com/thumbor/X5sLqcyTj8FPhZu0oAUqOr9qolM=/0x0:2405x2179/1200x800/filters:focal(1345x566:1729x950)/cdn.vox-cdn.com/uploads/chorus_image/image/63573477/game_of_thrones_season_8_photos_05.0.jpg"),
        Character(name="Cersei Lannister", actor="Lena Headey", episodes=62, image="https://images2.minutemediacdn.com/image/upload/c_crop,h_1667,w_2477,x_0,y_0/v1555429092/shape/mentalfloss/580083-helen_sloan-hbo.jpg?itok=Nh5bXKtt"),
        Character(name="Daenerys Targaryen", actor="Emilia Clarke", episodes=62, image="https://static.independent.co.uk/s3fs-public/thumbnails/image/2019/03/01/14/daenerys-targaryen.jpg"),
        Character(name="Jon Snow", actor="Kit Harington", episodes=62, image="https://fsmedia.imgix.net/75/96/8c/b4/1ace/41db/81ed/c3237e5893ac/jon-snow-eulogizing-the-dead-after-the-great-battle-of-winterfell.jpeg?rect=0%2C0%2C3150%2C1577&auto=format%2Ccompress&dpr=2&w=650"),
        Character(name="Sansa Stark", actor="Sophie Turner", episodes=60,  image="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/game-of-thrones-season-8-sansa-stark-sophie-turner-1554392503.jpg"),
        Character(name="Arya Stark", actor="Maisie Williams", episodes=59, image="https://ksassets.timeincuk.net/wp/uploads/sites/55/2019/04/1_09_GameOfThrones_S07-1.jpg"),
        Character(name="Jaime Lannister", actor="Nikolaj Coster-Waldau", episodes=55, image="https://www.dailydot.com/wp-content/uploads/2019/03/game_of_thrones_jaime_lannister.jpg"),
        Character(name="Jorah Mormont", actor="Iain Glen", episodes=52, image="https://www.dailydot.com/wp-content/uploads/2019/01/game_of_thrones_jorah_mormont.jpg"),
        Character(name="Samwell Tarly", actor="John Bradley", episodes=48, image="https://got2016-nocompany1458150561.netdna-ssl.com/images/samwell-tarly3.jpg"),
        Character(name="Theon Greyjoy", actor="Alfie Allen", episodes=47, image="https://www.hbo.com/content/dam/hbodata/series/game-of-thrones/character/s5/theon-greyjoy-1920.jpg/_jcr_content/renditions/cq5dam.web.1200.675.jpeg"),
        Character(name="Lord Varys", actor="Conleth Hill", episodes=46, image="https://media1.popsugar-assets.com/files/thumbor/dB7zR1Hm2nUZWoNNrScREyVWqa0/fit-in/2048xorig/filters:format_auto-!!-:strip_icc-!!-/2019/04/30/880/n/44631456/tmp_pg5e2S_39b67c8627de43ac_Lord-Varys-Game-of-Thrones.jpg"),
        Character(name="Brienne of Tarth", actor="Gwendoline Christie", episodes=42, image="https://images.theconversation.com/files/273106/original/file-20190507-103082-zrtm98.jpg?ixlib=rb-1.1.0&rect=0%2C127%2C3156%2C1578&q=45&auto=format&w=1356&h=668&fit=crop"),
        Character(name="Petyr 'Littlefinger' Baelish", actor="Aidan Gillen", episodes=41, image="https://hips.hearstapps.com/digitalspyuk.cdnds.net/17/36/1504606524-littlefinger.jpeg"),
        Character(name="Davos Seaworth", actor="Liam Cunningham", episodes=41, image="https://cdn1.thr.com/sites/default/files/2019/02/game_of_thrones-publicity_still_14-h-2019.jpg"),
        Character(name="Bran Stark", actor="Isaac Hempstead Wright", episodes=41, image="https://ksassets.timeincuk.net/wp/uploads/sites/55/2019/05/Bran-Stark.jpg"),
        Character(name="Sandor 'The Hound' Clegane", actor="Rory McCann", episodes=38, image="https://www.hbo.com/content/dam/hbodata/series/game-of-thrones/character/s5/sandor-clegane-1920.jpg/_jcr_content/renditions/cq5dam.web.1200.675.jpeg"),
        Character(name="Missandei", actor="Nathalie Emmanuel", episodes=38, image="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/missandei-grey-worm-sex-scene-1500908298.png"),
        Character(name="Bronn", actor="Jerome Flynn", episodes=37, image="https://static.gamespot.com/uploads/original/1581/15811374/3522717-game%20of%20thrones%20bronn%20crossbow.jpg"),
        Character(name="Eddison Tollett", actor="Ben Crompton", episodes=34, image="https://timedotcom.files.wordpress.com/2017/07/game-of-thrones-dragonstone-eddison-tollett.jpg?quality=85"),
        Character(name="Podrick Payne", actor="Daniel Portman", episodes=34, image="https://stylist-assets.imgix.net/app/uploads/2019/04/25154314/got4-1-1680x1120.jpg?w=1640&h=1&fit=max&auto=format%2Ccompress"),
        Character(name="Grey Worm", actor="Jacob Anderson", episodes=33, image="https://images.hellogiggles.com/uploads/2017/12/11153012/worm.png"),
        Character(name="Tormund Giantsbane", actor="Kristofer Hivju", episodes=32, image="https://cdn.vox-cdn.com/thumbor/gY_dQjulfxGQ2Tx12fmyxjj3568=/0x0:2100x1397/1200x800/filters:focal(882x531:1218x867)/cdn.vox-cdn.com/uploads/chorus_image/image/63651168/91ef7e54b76b5407b9c55f13b17647a553358d019ec623410ea5429d170a331bc044cd24074cc1c04a7d0f376f3072d5.0.jpg"),
        Character(name="Grand Maester Pycelle", actor="Julian Glover", episodes=31, image="https://i.pinimg.com/originals/1f/da/c6/1fdac6ef963df8e1c269c77f9c095cb1.jpg"),
        Character(name="Melisandre", actor="Carice van Houten", episodes=29, image="https://www.hbo.com/content/dam/hbodata/series/game-of-thrones/character/s5/melisandre-1920.jpg/_jcr_content/renditions/cq5dam.web.1200.675.jpeg"),
        Character(name="Gilly", actor="Hannah Murray", episodes=28, image="https://i.ytimg.com/vi/FtY5lW2rtdA/maxresdefault.jpg"),
        Character(name="Tywin Lannister", actor="Charles Dance", episodes=27, image="https://img.thedailybeast.com/image/upload/c_crop,d_placeholder_euli9k,h_1439,w_2560,x_0,y_0/dpr_1.5/c_limit,w_1044/fl_lossy,q_auto/v1492194017/articles/2014/11/18/charles-dance-on-tywin-lannister-s-s5-return-a-game-of-thrones-movie-and-sexy-peter-dinklage/141117-stern-lannister-tease_ylsfuy"),
        Character(name="Drogon", actor="", episodes=60, image="https://vignette.wikia.nocookie.net/gameofthrones/images/b/be/HBO_drogon_and_Jon.jpg/revision/latest?cb=20170814034408"),
        Character(name="Rhaegal", actor="", episodes=60, image="https://vignette.wikia.nocookie.net/gameofthrones/images/e/e0/Dragons_S8_Ep_1.jpg/revision/latest/scale-to-width-down/2000?cb=20190415031732"),
        Character(name="Viserion", actor="", episodes=50, image="https://i.pinimg.com/originals/d9/56/73/d9567302c17cbbb43ea86e69b37c5252.jpg")
    ],
    settings=[
        Setting(name="Westeros", image="https://vignette.wikia.nocookie.net/gameofthrones/images/0/0f/HBO_Map_of_Westeros.jpg/revision/latest?cb=20110314204946"),
        Setting(name="Kings Landing", image="https://cdnb.artstation.com/p/assets/images/images/012/370/613/large/steve-lund-castle-color2.jpg?1534439770"),
        Setting(name="The iron throne", image="https://cdn-images-1.medium.com/max/1600/1*42YN8Qqfhz1R64uDjZWIrA.jpeg"),
        Setting(name="Storm's End", image="https://i.pinimg.com/originals/0c/ce/33/0cce330b07e3d662c39bc43d0a106ac8.jpg")
    ],
    custom_spoilers=[
        "{{ctx.character}} becomes a whitewalker",
        "{{ctx.character}} becomes the ruler of the seven realms",
        "{{ctx.character}} beheads {{ctx.character}} in a totally epic battle",
        "{{ctx.character}} stands up to {{ctx.character}} and is killed for it",
        "{{ctx.character}} has a child with {{ctx.character}}",
        "{{ctx.character}} becomes the new king of the north",
        "{{ctx.setting}} falls to the ice king's army",
        "{{ctx.setting}} is burned by the dragons",
        "{{ctx.character}} conquers {{ctx.setting}}",
        "{{ctx.character}} kills a dragon",
        "{{ctx.character}} is betrayed by {{ctx.character}}",
        "Bran Stark predicts the death of {{ctx.character}}",
    ],
    images=[
        "https://timedotcom.files.wordpress.com/2019/05/game-of-thrones-season-8-episode-5-davos-jon-snow.jpg",
        "https://media.wired.com/photos/5cd0792e2c82ec474dc7bb5e/master/pass/Culture_GameOfThronesRecap_Ep4.jpg",
        "https://timedotcom.files.wordpress.com/2019/02/game-of-thrones-season-8-photos-01.jpg",
        "https://media.npr.org/assets/img/2019/04/14/1fa22a3eec708fb6ea43efb7dfe060fec9b3641c42b85e218c37fe70262f709d_wide-5f5ad5b9676dcbec05bb6dfc6c66f2daad766c79.jpg?s=1400"
    ]
)
