from random import randrange


def check_number_throws(dice_code):
    """
    :param dice_code:str dice code
    :return: int number of throws
    """
    if dice_code.find("D") > 0:
        throws_number = int(dice_code[:dice_code.find("D")])
    else:
        throws_number = 1
    return throws_number


def check_dice_type(dice_code):
    """def check_dice_type(dice_code):

    :param dice_code: str dice code
    :return:int dice number
    """
    dice_types = {"D3": 3,
                  "D4": 4,
                  "D6": 6,
                  "D8": 8,
                  "D10": 8,
                  "D12": 12,
                  "D20": 20,
                  "D100": 100,
                  }

    if "+" in dice_code:
        dice_type = dice_code[dice_code.find("D"):dice_code.find("+")]
    elif "-" in dice_code:
        dice_type = dice_code[dice_code.find("D"):dice_code.find("-")]
    else:
        dice_type = dice_code[dice_code.find("D"):]
    dice_type_number = dice_types[dice_type]
    return dice_type_number


def check_modifier(dice_code):
    """
    :param dice_code:str dice code
    :return: int modifier
    """
    if "+" in dice_code:
        modifier = int(dice_code[dice_code.find("+") + 1:])
    elif "-" in dice_code:
        modifier = int(dice_code[dice_code.find("-") + 1:])
    else:
        modifier = 0
    return modifier


def count_result(number_throws, dice_type, modifier):
    """
    :param number_throws: number of throws
    :param dice_type: int dice type
    :param modifier: int modifier
    :return: int result of throw
    """

    start_number = 1
    end_number = dice_type
    score = 0

    for _ in range(number_throws):
        score += randrange(start_number, end_number)

    if modifier:
        if modifier > 0:
            score += modifier
        else:
            score -= modifier
            if score < 0:
                score = 0
    return score


def dice(dice_code):
    """
    :param dice_code: str dice code
    :return: int with result of throw
    """
    try:
        throws_number = check_number_throws(dice_code)
    except Exception:
        raise ValueError('throws number error')
    try:
        dice_type = check_dice_type(dice_code)
    except Exception:
        raise ValueError('dice type error')
    try:
        modifier = check_modifier(dice_code)
    except Exception:
        raise ValueError('dice_code error')
    try:
        result = count_result(throws_number, dice_type, modifier)
    except Exception:
        raise ValueError('result error')
    return result


if __name__ == '__main__':
    print(dice("D100+10"))
    print(dice("2D20-10"))
