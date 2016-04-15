# coding: utf-8
from __future__ import unicode_literals
from decorators import on_command


@on_command(['!도움', '!ㄷㅇ', '!승규야','!승규'])
def run(robot, channel, tokens, user):
    '''도움말 출력 예) `!승규야 메모`'''
    if len(tokens) < 1:
        return channel, '\n'.join(robot.docs)
    if tokens[0] in ['생협', 'dgucoop', 'ㅅㅎ', 'tg']:
        msg = ''''''
        return channel, msg
    if tokens[0] in ['밥', '학식', 'ㅎㅅ', 'gt']:
        msg = '''오늘의 아리수, 상록원, 기숙사 학생식당의 메뉴를 보여드려요!
        오후 5시 이전에는 중식, 이후로는 석식의 메뉴를 보여드리지만,
        해당 시간이 아닐때도 보고 싶을때는 아래와 같이 이용할 수 있어요!
        !학식 [중식|ㅈㅅ|점심|wt|석식|ㅅㅅ|저녁|tt|ws]
        예) !학식 석식   =>  석식메뉴를 보여드려요!'''
        return channel, msg
    if tokens[0] in ['메모', 'ㅁㅁ', 'aa']:
        msg = '''입력하신 내용을 대신 기억해드렸다가, 원하실때 보여드려요!
        메모는 독립적인 기능이라 자기 자신만이 등록/삭제/조회할 수 있어요!
        !메모 <기억할 내용>
        예) !메모 내일 점심에 치킨먹기 => "내일 점심에 치킨먹기" 메모
        (기억할 내용없이 !메모 만 입력하시면 입력하셨던 메모를 보여드려요!'''
        return channel, msg
    if tokens[0] in ['메모삭제', 'ㅁㅁㅅㅈ', 'aatw']:
        msg = '''기억시키셨던 메모를 지워드려요 !
        메모를 지울 때는 메모의 번호를 같이 입력시켜주시면 되요!
        한번에 여러 메모를 동시에 지울 수도 있어요!
        !메모삭제 <메모번호1> <메모번호2> ....
        예) !메모삭제 1 2 3 4 5  =>  1, 2, 3, 4, 5번째 메모가 지워져요!'''
        return channel, msg
    if tokens[0] in ['기억', 'ㄱㅇ', 'rd']:
        msg = '''어떠한 단어에 대한 설명을 알려주시면 기억해요!
        메모와 다른점은, 단어로 접근을 할 수 있고 모두가 다 같이 공유해요!
        !기억 <기억할 단어> <단어 설명>
        예) !기억 DNA Dongguk Network Association의 약자
        기억한 것을 다시 살펴보고자 할 때는 단어만 입력해주시면 되요!
        예) !기억 DNA
        기억시킨 단어가 너무 많아 기억이 안날땐, 다음과 같이 해주세요!
        예) !기억 ?'''
        return channel, msg
    if tokens[0] in ['기억삭제', 'ㄱㅇㅅㅈ', 'rdtw']:
        msg = ''
        return channel, msg
    if tokens[0] in ['퀴즈']:
        msg = '''문제집을 만들고, 문제집을 풀 수 있음.
        문제집을 풀 때 문제는 무작위 순서로 나옴.
        `!퀴즈` => 풀고 있는 문제를 재 출력함
        `!퀴즈 등록 <문제집이름> <질문> <정답>` => 문제집에 문제를 등록함
        `!퀴즈 수정 <문제집이름> <문제번호> <질문> <정답>`
                => 잘못된 문제를 수정함. 덮어씌워지니 주의요망
        `!퀴즈 조회 <문제집이름>` => 문제집의 정보를 보여줌
        `!퀴즈 시작 <문제집이름>` => 문제집의 문제를 풀기 시작함'''
        return channel, msg
    msg = tokens[0]+'은(는) 모르는 명령어거나, 도움말이 등록이 안됬어요 ㅠㅡㅠ'
    return channel, msg
