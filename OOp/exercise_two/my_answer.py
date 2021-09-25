class Pants:
    """The Pants class represents an article of clothing sold in a store """

    def __init__(self, color, waist_size, length, price):
        """Method for initializing a Pants object
              :arg
                   color (str)
                   waist_size (int)
                   length (int)
                   price (float)

               :param
                   color (str): color of a pants object
                   waist_size (str): waist size of a pants object
                   length (str): length of a pants object
                   price (float): price of a pants object
               """
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price

    def change_price(self, new_price):
        """

        :param new_price: represent the new price of the pants object
        :argument new_price (float)
        :return None
        """
        self.price = new_price

    def discount(self, discount):
        """

        :param discount: it's the discount given to the pants object to change the price value
        :arg  (float) a decimal representing the amount to discount
        :return:  float: the discounted price
        """
        discounted_price = self.price * (1 - discount)
        return discounted_price


class SalesPerson:
    def __init__(self, first_name, last_name, employee_id, salary):
        """
        :Attribute
            first_name: (String)
            last_name: (String)
            employee_id: (integer)
            salary: (float)
            pants_sold: (list of Pants objects)
            total_sales: (float)

        :param first_name: (String) the first name of the salesperson
        :param last_name: (String) the last name of the salesperson
        :param employee_id: (integer) the id of the salesperson
        :param salary: (float) the salary of the salesperson
        """
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0

    def sell_pants(self, pants):
        """The sell_pants method appends a pants object to the pants_sold attribute
            :argument:
                pants_object (obj): a pants object that was sold
            Returns: None
            :param pants:
            """
        self.pants_sold.append(pants)

    def calculate_sales(self):

        """The calculate_sales method sums the total price of all pants sold

           Args: None
            :var total  is a variable to store the total prices
           Returns:
               float: sum of the price for all pants sold

           """
        total = 0
        for pants in self.pants_sold:
            total += pants.price
            self.total_sales = total
        return total

    def display_sales(self):
        """The display_sales method prints out all pants that have been sold

               Args: None
               output: print the color , waist size , length ,price of the pants that are sold by the sales man
               Returns: None

               """
        for pants in self.pants_sold:
            if pants:
                print("color: {} , waist size: {} , length: {}  , price: {}".format(pants.color, pants.waist_size,
                                                                                    pants.length,
                                                                                    pants.price))
            else:
                print('there is no pants yet sold')

    def calculate_commission(self, commission):
        """The calculate_commission method outputs the commission based on sales

               Args:
                   percentage (float): the commission percentage as a decimal

               Returns:
                   float: the commission due
                   :param commission:
               """
        the_commission = self.calculate_sales()
        return the_commission * commission


def check_results():
    pants_one = Pants('red', 35, 36, 15.12)
    pants_two = Pants('blue', 40, 38, 24.12)
    pants_three = Pants('tan', 28, 30, 8.12)

    sales_object = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)
    assert sales_object.first_name == 'Amy'
    assert sales_object.last_name == 'Gonzalez'
    assert sales_object.employee_id == 2581923
    assert sales_object.salary == 40000
    assert sales_object.pants_sold == []
    assert sales_object.total_sales == 0

    sales_object.sell_pants(pants_one)
    sales_object.pants_sold[0] == pants_one.color

    sales_object.sell_pants(pants_two)
    sales_object.sell_pants(pants_three)

    assert len(sales_object.pants_sold) == 3
    assert round(sales_object.calculate_sales(), 2) == 47.36
    assert round(sales_object.calculate_commission(.1), 2) == 4.74

    print('Great job, you made it to the end of the code checks!')
