def score_apartment(size_m2, price_krw, is_near_subway):
    """
    아주 간단한 예시용 스코어링 함수.
    size_m2: 전용면적 (제곱미터)
    price_krw: 가격 (원 단위)
    is_near_subway: 역세권 여부 (True/False)
    """

    score = 0

    # 전용면적이 40~60 사이면 가점
    if 40 <= size_m2 <= 60:
        score += 2

    # 가격이 5억 이하이면 가성비 가점 (완전 예시값)
    if price_krw <= 500_000_000:
        score += 2

    # 역세권이면 가점
    if is_near_subway:
        score += 1

    return score
