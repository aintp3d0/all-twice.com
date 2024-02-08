#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'ames0k0'

from pathlib import Path

STATIC_DIR = Path('pics').absolute()
STATIC_DIR_DAY = STATIC_DIR / 'day'
STATIC_DIR_ABOUT = STATIC_DIR / 'about'


DEFAULT_IMAGE_VIEWER = 'feh'


end = '\033[0m'
blue = '\033[94m'
purple = '\033[35m'

# [state, bth_n, natio, posit, birth, zodic, offih, offiw, blood]
bio = """\n
    Stage Name:--------{} %s{}
    Birth Name:--------{} %s{}
    Nationality:-------{} %s{}
    Position:----------{} %s{}
    Birthday:----------{} %s{}
    Zodiac sign:-------{} %s{}
    Official Height:---{} %s{}
    Official Weight:---{} %s{}
    Blood Type:--------{} %s{}\n
"""

options = """
        {0}1) Download  [a]ll/specific/[r]andom Day and Open    == {1}120 days * ~7...40 pics
        {0}2) Open      [a]ll/specific/[r]andom Day from        == {0}[{2}]
        {0}3) Delete all Days                                   == {1}[{2}]\n
"""

JIHYO = (
    'Jihyo', 'Park Ji Soo (박지수) / legalized name Park Ji Hyo (박지효)',
    'Korean', 'Leader, Main Vocalist', 'February 1, 1997', 'Aquarius',
    '162 cm ( 5 ft 3¾ in) /Approx. Real Height: 160 cm (5’3″)*',
    '56 kg (123 lbs) / Approx. Real Weight: 49 kg (108 lbs)', 'O'
)

NAYEON = (
    'Nayeon', 'Im Na Yeon (임나연)', 'Korean', 'Lead Vocalist, Face of The Group, Center',
    'September 22, 1995', 'Virgo', '163 cm (5’4″) / Approx. Real Height: 163 cm (5’4″) / *',
    '47 kg (104 lbs)', 'A'
)

JEONGYEON = (
    'Jeongyeon', 'Yoo Kyung Wan (유경완), but she legalized her name to Yoo Jung Yeon (유정연)',
    'Korean', 'Lead Vocalist', 'November 1, 1996', 'Scorpio',
    '169 cm (5’7″) / Real Height: 169 cm (5’7″)*', '49 kg (108 lbs)', 'O'
)

MOMO = (
    'Momo', 'Hirai Momo (平井 もも)', 'Japanese', 'Main Dancer, Vocalist, Rapper',
    'November 9, 1996', 'Scorpio', '167 cm (5’6″) / Appox. Real Height: 163 cm (5’4″)*',
    '48 kg (106 lbs)', 'A'
)

SANA = (
    'Sana', 'Minatozaki Sana (湊崎 紗夏)', 'Japanese', 'Lead Dancer, Vocalist',
    'December 29, 1996', 'Capricorn', '168 cm (5’6″) / Approx. Real Height: 165 cm (5’5″)*',
    '48 kg (106 lbs)', 'B'
)

MINA = (
    'Mina', 'Myoui Mina (名井 南) | Sharon', 'Japanese', 'Lead Dancer, Vocalist',
    'March 24, 1997', 'Aries', '163 cm (5’4″) /Approx. Real Height: 165 cm (5’5″)*',
    '46 kg (101 lbs)', 'A'
)

DAHYUN = (
    'Dahyun', 'Kim Da Hyun (김다현)', 'Korean', 'Lead Rapper, Vocalist', 'May 28, 1998',
    'Gemini', '165 cm (5’5″) / Real Height: 158.6 cm (5’3″)', '48.9 kg (108 lbs)*', 'O'
)

CHAEYOUNG = (
    'Chaeyoung', 'Son Chae Young (손채영)', 'Korean', 'Main Rapper, Vocalist',
    'April 23, 1999', 'Taurus', '163 cm (5’4″) /Real Height: 158.9 cm (5’3″)*',
    '48 kg (106 lbs)', 'B'
)

TZUYU = (
    'Tzuyu', 'Chou Tzuyu (周子瑜) | Joo Ja Yoo (주자유) | Sally', 'TAiwanese',
    'Lead Dancer, Vocalist, Visual, Maknae', 'June 14, 1999', 'Gemini',
    '170 cm (5’7″) / Approx. Real Height: 172 cm (5’8″)*', '48 kg (106 lbs)', 'A'
)

artists = {
    'JIHYO': JIHYO, 'NAYEON': NAYEON, 'JEONGYEON': JEONGYEON, 'MOMO': MOMO,
    'SANA': SANA, 'MINA': MINA, 'DAHYUN': DAHYUN, 'CHAEYOUNG': CHAEYOUNG, 'TZUYU': TZUYU
}

DISCOGRAPHY = '''
                                                               {} DISCOGRAPHY
                                   {} 아홉 소녀가 보내는 ‘찌릿찌릿’ 시그널 ! 트와이스 미니 4집 [SIGNAL] 발매 !
                                    드디어 만났다. 트와이스 X JYP, 트와이스 스타일의 뉴 그루브, ‘SIGNAL’ 5연속 메가 히트 예약

   {} 올해 2월 스페셜 앨범 ‘KNOCK KNOCK’으로 팬들의 마음을 두드렸던 트와이스가 드디어 박진영 PD의 곡으로 5월 메이퀸 등극을 예고하며 3개월만에 팬들 앞에 미니 4집 [SIGNAL]을 선보인다.
    ‘우아하게’ – ‘CHEER UP’ – ‘TT’ – ‘KNOCK KNOCK’ 까지 4연속 메가 히트와 더불어 K-POP 걸그룹 최다 유튜브 조회수, 1억뷰 돌파, 30만장에 육박하는 음반 판매고,
    첫 콘서트 실시간 매진 등 ‘기록 제조기’ 로서의 명성에 모자람이 없는 성적들을 만들어 온 트와이스가 이번에는 또 어떤 성과를 만들어 낼지. 팬들은 물론, 이제는 전 아시아가 주목하는 아티스트로 성장했다.

   {} 아시아 최고의 프로듀서이자, JYP의 수장인 박진영 PD와의 작업은 이번 앨범의 가장 주목할만한 포인트다. ‘식스틴’ 때부터 멤버들의 선발 과정을 함께한 만큼,
    멤버들의 특색과 개성을 가장 잘 이해하고 있는 프로듀서로서, 트와이스에 가장 잘 어울리면서도 지금과 다른 색깔을 표현할 수 있는 곡을 위해 굉장한 고민과 노력을 했다는 후문.
    그래서 탄생한 이번 미니 4집의 타이틀 곡 ‘SIGNAL’은 박진영 특유의 쉽고 캐치한 사운드와 그루브함이 트와이스의 발랄하고 건강한 에너지와 최고의 케미를 선사한다.
    강력한 808 베이스의 힙합 리듬에 경쾌한 전자 악기들의 댄서블한 리듬을 배치하여 그루브함과 경쾌함의 최고의 조합을 만들어냈다.
    좋아하는 사람을 만날 때의 ‘찌릿찌릿’한 마음을 앙증맞기 이를데 없는 포즈로 그려낸 포인트 안무는 지금까지 트와이스가 만들어온 ‘샤샤샤’-‘너무해’ 라인을 잇는 트와이스의 또 하나의 시그니처로 더 많은 사람들에게 사랑 받을 수 있을 것으로 보인다.

   {} 레게 팝과 트렌디 사운드의 믹스쳐를 시도한 ‘하루에 세 번’, HA:TFELT가 작사하고, 중독성 강한 훅이 인상적인 ‘ONLY 너’, ‘JELLY JELLY’에 참여했던 조울 작곡가와 다시 한번 호흡을 맞춘 ‘HOLD ME TIGHT’,
    지효와 채영이 작사가로 참여한 ‘EYE EYE EYES’는 트와이스만의 감성을 더 편안하게 느낄 수 있다는 점에서 이번 앨범의 또 다른 포인트.
    지효와 채영의 상상으로, 처음 느껴보는 설레는 감정을 담백하고 귀엽게 풀어낸 가사는 ‘트와이스 답다’는 말이 가장 어울릴법하다. 박원이 작사하여 사랑에 빠진 소녀의 모습을 그린,
    ‘LIKE A FOOL’-‘ONE IN A MILLION’을 잇는 발라드 넘버 ‘SOMEONE LIKE ME’ 까지, 이번 앨범 또한 전작들과 마찬가지로 압도적인 퀼리티의 수록곡들로 가득 채워져 있다.

   {} 정상의 자리에 다다르면서도, 처음의 마음을 잃지 않는 것이 얼마나 중요한지 잘 알고 있는 트와이스라서 이번 앨범을 준비하는 과정과 시간들 또한 너무나 분주했던 시간들임에도,
    항상 처음의 마음을 담아 준비하고, 노래하고 연습했다. 한국과 일본, 아시아를 향해 나아가고 있는 트와이스지만 지금까지, 앞으로도 트와이스에게 가장 중요한 건 트와이스를 사랑해주는 팬 분들이라는 걸 항상 잊지 않는다.
    이 모든 곡들에 그러한 마음과 노력이 담겨 있기 때문에 더 예쁘고 귀엽고, 사랑스럽게 들리는게 아닐지. 그래서 언제든 어디서든, 트와이스와는 ‘함께 있는’것 일테다.

                    {} TRACKLIST
            {} 1. SIGNAL
            {} 2. 하루에 세 번
            {} 3. Only 너
            {} 4. HOLD ME TIGHT
            {} 5. EYE EYE EYES
            {} 6. SOMEONE LIKE ME

   {} 1. SIGNAL
        {}박진영이 처음으로 만든 트와이스의 타이틀 곡으로 강렬한 808 Bass 사운드의 힙합 느낌과 경쾌한 전자악기들의 댄스음악 느낌을 교대로 배열함으로서 박진영 특유의 그루브함과 트와이스만의 경쾌함을 모두 표현한 곡이다.

   {} 2. 하루에 세 번
        {}김원 작곡가와 싱어송라이터 디아의 작품. 남자친구의 무심함 때문에 뾰로통해진 여자친구의 심리를 매우 현실감있게 묘사한 가사로 공감대를 극대화 시킨 작품.
        레게톤과 뭄바톤의 적절한 조합과 묵직한 808소스의 리듬이 어우러져 트렌디한 사운드를 들려준다.
        곳곳에 적절히 들어가있는 특이한 소리들과 적절한 업템포의 리드미컬한 요소가 특징. 트와이스의 위트있고 새로운 모습을 보여주는 트랙.

   {} 3. Only 너
        {}“Only 너”는 영국의 핫 프로듀서인 David Anthony가 트와이스에게 선물한 신나는 팝송이다. 정통 힙합 비트에 모던한 사운드와 트와이스 특유의 발랄하고 에너지 넘치는 보컬을 얹었다.
        트와이스의 이름처럼 두번만 듣고도 쉽게 따라 부를 수 있는 중독성 강한 히트송이다.

   {} 4. HOLD ME TIGHT
        {}아무리 눈치를 줘도 눈치채지 못하는 둔한 상대방을 향해 어서 빨리 고백해주길 바라는 소녀의 애타는 마음을 트와이스만의 깜찍함으로 풀어낸 곡이다. 따라부르기 쉬운 멜로디와 가사가 기존 트와이스의 색을 유지하면서도,
        묵직한 비트와 신스계열의 독특한 편곡이 어우러져 색다른 매력을 장착하였다.
        미니 3집 수록곡 ‘JELLY JELLY’에 참여했던 '조울'작곡가와 다시 한번 호흡을 맞추어 더욱 기대되는 곡이다.

   {} 5. EYE EYE EYES
        {}트와이스 멤버들의 귀엽고 사랑스러운 보컬과 경쾌한 탬버린소리, 장난스러운 휘파람이 더해져 익살스런 곡이 나왔다.
        중간에 들어간 재즈 브레이크는 곡 전반적으로 펼쳐져 있는 업 비트 분위기와 대비되면서 트와이스의 소녀감성을 더욱 더 돋보이게 한다.
        그리고 EYE EYE EYES의 가사는 사랑에 빠진 소녀의 마음을 귀엽게 표현했다. 지효와 채영의 상상으로, 처음 느껴보는 이성에 대한 설레는 감정을 재미있게,
        완벽한 이상형은 아닌 것 같지만 그래도 그것이 무엇인지 모르겠다는 것을, 열심히 알아 나가는 소녀의 마음을 담았다.

   {} 6. SOMEONE LIKE ME
        {}잔잔한 일렉트릭 기타가 곡 전반에 걸쳐져 있는 이 곡은 TWICEcoaster : LANE 1의 “ONE IN A MILLION”을 잇는 따뜻한 팝으로 트와이스의 섬세한 보컬이 돋보이는 곡이다.
        특히 박원의 가사는 트와이스를 사랑에 빠진 소녀의 모습으로 그린다.

'''

SOURCES = '''
    {} SOURCES
{} http://all-twice.com/
{} http://kprofiles.com/twice-members-profile/
{} http://twice.jype.com/

{} https://www.instagram.com/twicetagram/
{} https://twitter.com/JYPETWICE
{} https://www.facebook.com/JYPETWICE
{} https://www.youtube.com/jypentertainment
{} https://fans.jype.com/Portal{}

'''
