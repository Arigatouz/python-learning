import math
import matplotlib.pyplot as plt

class Gaussian():
    """ Gaussian distribution class for calculating and
    visualizing a Gaussian distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stddev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file

    """

    def __init__(self, mu=0, sigma=1):
        self.mean = mu
        self.stddev = sigma
        self.data = []

    def calculate_mean(self):
        """Method to calculate the mean of the data set.

        Args:
            None

        Returns:
            float: mean of the data set

        """

        # TODO: Calculate the mean of the data set. Remember that the data set is stored in self.data
        # Change the value of the mean attribute to be the mean of the data set
        # Return the mean of the data set
        pass
