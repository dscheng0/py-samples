class TempTracker (object):
    """
    Tracker to get statistics from inserted temperatures (Farenheit)
    """

    def __init__(self):
        self._min = None
        self._max = None
        self._sum = 0
        self._count = 0
        
    def insert(self, temp_f):
        """
        Records a new temperature measured in Farenheit.

        :Args:
        temp_f (int): temperature in Farenheit to insert
        """
        self._sum += temp_f
        self._count += 1

        if (None is self._min or temp_f < self._min):
            self._min = temp_f
        if (None is self._max or temp_f > self._max):
            self._max = temp_f
            
    def get_max(self):
        """
        Get the max temperature recorded
        
        :Returns:
        (int) the highest temp we've seen so far.

        :Raises:
        RuntimeWarning if there have been no recorded temperatures
        """
        if None is self._max:
            raise RuntimeWarning("No recorded temperatures")
        return self._max

    def get_min(self):
        """
        Get the min temperature recorded
        
        :Returns:
        (int) the lowest temp we've seen so far.

        :Raises:
        RuntimeWarning if there have been no recorded temperatures
        """
        if None is self._min:
            raise RuntimeWarning("No recorded temperatures")
        return self._min

    def get_mean(self):
        """
        Get the average (mean) temperature
        
        :Returns:
        (float) the mean of all temps we've seen so far.

        :Raises:
        RuntimeWarning if there have been no recorded temperatures
        """
        if None is self._min:
            raise RuntimeWarning("No recorded temperatures")
        return float(self._sum)/self._count
