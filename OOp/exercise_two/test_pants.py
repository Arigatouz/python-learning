from my_answer import Pants, SalesPerson


def test_pants():
    """
    :var creating  new object called pants_one from the  Class
    :return: testing if the object pants_one is working correctly
    """
    pants_one = Pants('red', 35, 36, 15.12)
    assert pants_one.color == 'red'
    assert pants_one.waist_size == 35
    assert pants_one.length == 36
    assert pants_one.price == 15.12

    pants_one.change_price(10)
    assert pants_one.price == 10

    assert pants_one.discount(.1) == 9

    print('You made it to the end of the check. Nice job!')


def test_():
    pants_one = Pants('red', 35, 36, 15.12)
    pants_two = Pants('blue', 40, 38, 24.12)
    pants_three = Pants('tan', 28, 30, 8.12)

    ali = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)
    assert ali.first_name == 'Amy'
    assert ali.last_name == 'Gonzalez'
    assert ali.employee_id == 2581923
    assert ali.salary == 40000
    assert ali.pants_sold == []
    assert ali.total_sales == 0

    ali.sell_pants(pants_one)
    var = ali.pants_sold[0] == pants_one.color

    ali.sell_pants(pants_two)
    ali.sell_pants(pants_three)

    assert len(ali.pants_sold) == 3
    assert round(ali.calculate_sales(), 2) == 47.36
    assert round(ali.calculate_commission(.1), 2) == 4.74





