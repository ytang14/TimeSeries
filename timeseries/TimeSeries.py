import numpy as np
from .lazy import *
import numbers
import pype
import json

class TimeSeries():
    '''
    """
Help on package TimeSeries:

NAME
    TimeSeries

DESCRIPTION
    TimeSeries
    =====

    Provides
      1. An sequence or any iterable objects

    How to use the documentation
    ----------------------------
    Documentation is available in two forms: docstrings provided
    with the code, and a loose standing reference guide, available from
    `the TimeSeries homepage <https://github.com/cs207-project>`_.

    We recommend exploring the docstrings using
    `IPython <http://ipython.scipy.org>`_, an advanced Python shell with
    TAB-completion and introspection capabilities.  See below for further
    instructions.

    The docstring examples assume that `numpy` has been imported as `np`::

     |  Methods inherited from builtins.RuntimeWarning:
     |
     |  __init__(self, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |      Stors a TimeSeries in self.TimeSeries_
     |
     |  __repr__(self, /)
     |      Return a printable sequence shown in python list format containing all values in [self].
     |
     |  __str__(self, /)
     |      Return a printable abbreviated sequence of maximum first 100 entrees.
     |
     |  __getitem__(self, index)
     |      Return self[index]
     |
     |  __setitem__(self, index, values)
     |      Set self[index] = values
     |
     |  __len__(self)
     |      Return len(self.TimeSeries_)
     '''
    def __init__(self, times, values):
        """
        This initialise the Time Series Class by passing into the "times" and "values" lists

        Note
        ----
        The times and values must be of the same in length, and they can both be empty.

        Parameters
        ----------
        times : list of floats
            sequence of time values represented as float
        values : list of floats
            sequence of values corresponding to each time value

        Examples
        --------

        >>> ts0 = TimeSeries([],[])
        >>> ts1 = TimeSeries(range(0,4),range(1,5))
        >>> ts2 = TimeSeries(range(0,4),[10,20,30,40,50])
        >>> ts3 = TimeSeries([0,5,10], [1,2,3])
        >>> ts4 = TimeSeries([2.5,7.5], [100, -100])

        """
        if (iter(times) and iter(values)):
            # reorder according to Time step
            idx = np.argsort(times)
            times = np.array(times)[idx]
            values = np.array(values)[idx]

            self._TimeSeries=np.vstack((times,values))
            self._vindex = 0
            self._values = self._TimeSeries[1]
            self._times = self._TimeSeries[0]

    # Lab 07

    # Lab 08 
    def __len__(self):
        """
        Returns the length of this TimeSeries instance.

        Returns
        -------
        int
            length

        Examples
        --------
        >>> ts1 = TimeSeries(range(0,4),range(1,5))
        >>> len(ts1)
        4

        """
        return len(self._TimeSeries[0])
    
    def __contains__(self, time):
        """
        Check if the given time-value is
        in the times-list of our TimeSeries instance.

        Parameters
        ----------
        time : float

        Returns
        -------
        bool
            True if 'time' is in, False otherwise.

        Examples
        --------
        >>> ts1 = TimeSeries(range(0,4),range(1,5))
        >>> ts1[0]
        1
        """
        index = np.where(self._TimeSeries[0]==time)
        return index[0].size>0

    def __iter__(self):
        """
        Returns a generator object that iterates value-list of the TimeSeries.

        Returns
        -------
        iter()

        Examples
        --------


        """
        return iter(self._TimeSeries[1])
    
    def __repr__(self):
        """

        Representation method.
        Refer to __str__ method.

        Examples
        --------
        >>> print repr(ts1)
        array([[0, 1, 2, 3],
               [1, 2, 3, 4]])

        """
        return "%r"%(self._TimeSeries)
    
    def __str__(self):
        """
        Representation method.

        Returns
        -------
        ex) TimeSeries([1, 2, ...])

        Examples
        --------
        >>> ts1 = TimeSeries(range(0,4),range(1,5))
        >>> print ts1
        [[0 1 2 3]
         [1 2 3 4]]
        """

        className = type(self).__name__
        if len(self)>100:
            return "%s" %('['+(str(self._values[:99]))[1:-1]+'...'+']')
        else:
            return "%s" %(self._TimeSeries)
            
    
    def __getitem__(self,time):
        """
        Return the 'value' in the position corresponding to
        the given 'time' value.

        Parameters
        ----------
        time : float

        Returns
        -------
        float
            value

        Examples
        --------
        >>> ts1 = TimeSeries(range(0,4),range(1,5))
        >>> print ts1[0]
        [1]
        """
        if (time in self):
            index = np.where(self._TimeSeries[0]==time)
            return self._TimeSeries[1][index]
        else:
            print ("no time point at t={0}".format(time))

    def __setitem__(self,time,value):
        """
        Replace a value in the position corresponding to the given 'time' value
        by the given 'value'.

        Parameters
        ----------
        time : float
        value : float

        Examples
        --------
        >>> ts1 = TimeSeries(range(0,4),range(1,5))
        >>> ts1[0] = 2
        >>> print ts1[0]
        2
        """
        if (time in self):
            index = np.where(self._TimeSeries[0]==time)
            self._TimeSeries[1][index]=value
        else:
            print ("no time point at t={0}".format(time))


    # Lab 10
    def values(self):
        """
        Returns the 'value-list' attribute of this TimeSeries

        Returns
        -------
        list
            value_list

        Examples
        --------
        >>> ts1 = TimeSeries(range(0,4),range(1,5))
        >>> np.array_equal(ts1.values(), range(1,5))
        True
        """
        return self._values
    
    def times(self):
        """
        Returns the 'time-list' attribute of this TimeSeries

        Returns
        -------
        list
            time_list

        Examples
        --------
        >>> np.array_equal(ts1.times(), range(0,4))
        True
        """
        return self._times

    def items(self):
        """
        Returns a sequence of (time, value) tuples

        Returns
        -------
        list
            (time, value)

        Examples
        --------
        >>> ts1 = TimeSeries(range(0,4),range(1,5))
        >>> ts1.items()
        list((t,v) for t,v in zip(range(0,4), range(1,5)))
        """
        return list((t, v) for t, v in zip(self._times, self._values))


    def interpolate(self, times):
        '''
        Filling the TimeSeries class with a given list of times using linear interpolation

        Parameters
        ----------
        times: list of float
            a list of times to be added to self

        Returns
        -------
        TimeSeries
             New TimeSeries instance with parameter 'times' and interpolated 'values' added

        Examples
        --------
        >>> ts1 = TimeSeries(range(0,4),range(1,5))
        >>> ts3 = TimeSeries([0,5,10], [1,2,3])
        >>> c = TimeSeries([1.],[1.2])
        >>> d = ts3.interpolate([1.])
        >>> c == d
        True
        >>> ts3.interpolate(ts4.times())
        TS.TimeSeries([2.5,7.5], [1.5, 2.5])
        # Boundary conditions
        >>> ts3.interpolate([-100,100])
        TS.TimeSeries([-100,100],[1,3])
        >>> ts1+d
        ValueError: [[0 1 2 3]
         [1 2 3 4]] and [[0 1 2]
         [1 2 3]] must have the same time points
        '''
        new_values = []
        for time in times:
            if time > self._times[-1]: # over the rightest boundary
                new_values.append(self._values[-1])
            elif time < self._times[0]: # over the leftest boundary
                new_values.append(self._values[0])
            elif time in self._times:
                new_values.append(self.__getitem__(time))
            else : #within boundary
                for i in range(len(self._times)):
                    if self._times[i] > time:
                        left_value = self._values[i-1]
                        right_value = self._values[i]
                        left_time = self._times[i-1]
                        right_time = self._times[i]
                        #interpolate
                        new_values.append(left_value + (right_value - left_value)/(right_time - left_time)*(time - left_time))
                        break
        return TimeSeries(times, new_values)

    @property
    @lazy
    def lazy(self):
        """
        Class method used for lazy-evaluation.
        By @lazy decorator, the lazy function returns
        lazyOperation() instance that is used later
        when actual evaluation happens.

        Returns
        -------
        instance
            lazyOperation()

        Examples
        --------
        >>> @lazy
            def lazy_add(a,b):
                return a+b
        >>> lazy_add(2,4).eval()
        6
        """
        return self



    # Lab11
    @pype.component
    def mean(self):
        """
        Returns the mean value of self.values

        Returns
        -------
        float
            the mean of self.values

        Raises
        ------
        ValueError
            If self.values is empty

        Examples
        --------
        >>> ts0 = TimeSeries([],[])
        >>> ts1 = TimeSeries(range(0,4),range(1,5))
        >>> ts1.mean()
        2.5
        >>> ts0.mean()
        ValueError: cant calculate mean of length 0 list
        """
        if(len(self._values) == 0):
            raise ValueError("cant calculate mean of length 0 list")
        return np.mean(self._values)
    
    def median(self):
        '''
        Getting the median of self.values

        Returns
        -------
        float
            the median of self.values

        Raises
        ------
        ValueError
            If self.values is empty

        Examples
        --------
        >>> ts0 = TimeSeries([],[])
        >>> ts1 = TimeSeries(range(0,4),range(1,5))
        >>> ts1.median()
        2.5
        >>>ts0.median()
        ValueError: cant calculate median of length 0 list

        '''
        if(len(self._values) == 0):
            raise ValueError("cant calculate median of length 0 list")
        return np.median(self._values)
    
    # Lab12
    def itervalues(self):
        """
        Class method that yields values of the Timeseries one by one.

        Yields
        -------
        float
            value

        Examples
        --------
        >>> ts1 = TimeSeries(range(0,4),range(1,5))
        >>> vi=ts1.itervalues()
        >>> next(vi)
        1
        """
        for v in self._values:
            yield v

    def itertimes(self):
        """
        Class method that yields time-values of the Timeseries one by one.

        Yields
        -------
        float
            time

        Examples
        --------
        >>> ts1 = TimeSeries(range(0,4),range(1,5))
        >>> ti=ts1.itertimes()
        >>> next(ti)
        0
        """
        for t in self._times:
            yield t

    def iteritems(self):
        """
        Class method that yields each pair of (value, time) of the Timeseries one by one.

        Yields
        -------
        tuple
            (value, time)

        Examples
        --------
        >>> ts1 = TimeSeries(range(0,4),range(1,5))
        >>> iti=ts1.iteritems()
        >>> next(iti)
        (0,1)

        """
        for t,v in zip(self._times,self._values):
            yield (t,v)


    # Lab15
    def __eq__(self, other):
        """
        Check if the 'other' is the same instance with this TimeSeries instacne.

        Parameters
        ----------
        other : TimeSeries()

        Returns
        -------
        bool
            True if they are equal, False otherwise

        Examples
        --------
        >>> ts1 = TimeSeries(range(0,4),range(1,5))
        >>> tmpTestSeries = TimeSeries(range(0,4),range(1,5))
        >>> tmpTestSeries == ts1
        True

        """
        return np.array_equal(self._TimeSeries, other._TimeSeries)

    def checkTime(self,rhs):
        '''
        Tool function checking wether the given parameter 'rhs' and self have the same time points

        Parameters
        ----------
        rhs: TimeSeries
            TimeSeries instance to be compared with self on 'times' list

        Returns
        -------
        bool
             True if rhs and self have the same 'times' list, False otherwise

        Examples
        --------
        >>> ts1 = TimeSeries(range(0,4),range(1,5))
        >>> print ts1.checkTime(TimeSeries(range(0,4),range(1,5)))
        True
        '''
        return np.array_equal(self._times, rhs._times)

    def __add__(self, rhs):
        '''
        Elementwise add operation

        Parameters
        ----------
        rhs: TimeSeries
            TimeSeries instance with the same 'times' points for TimeSeries addition, applied only on 'values' list

        Returns
        -------
        TimeSeries
             result of TimeSeries Class added by parameter 'rhs'

        Raises
        ------
        TypeError
            If values in rhs are not real number
        ValueError
            If time points in self and rhs do not match

        Examples
        --------
        >>> ts1 = TimeSeries(range(0,4),range(1,5))
        >>> ts2 = TimeSeries(range(0,4),[10,20,30,40,50])
        >>> c = 100
        >>> ts1+ts2
        TS.TimeSeries(range(0,4),[11,22,33,44,55])
        >>> ts1+c
        TS.TimeSeries(range(0,4),[101,102,103,104,105])
        '''
        try:
            
            if isinstance(rhs, numbers.Real):

                return TimeSeries(self._times, rhs + self._values)

            elif self.checkTime(rhs) == True:

                return TimeSeries(self._times, rhs._values + self._values)
            
            else:
                
                raise ValueError(str(self)+' and '+str(rhs)+' must have the same time points')
        except TypeError:
            
            raise NotImplemented


    def __radd__(self, other):
        '''
        other + self delegates to __add__

        Parameters
        ----------
        other : TimeSeries
            TimeSeries instance for TimeSeries addition

        Returns
        -------
        TimeSeries
             result of self added by parameter 'other', 'values' of which are the sum of two 'values' lists

        Examples
        --------
        >>> ts1 = TimeSeries(range(0,4),range(1,5))
        >>> ts2 = TimeSeries(range(0,4),[10,20,30,40,50])
        >>> c = 100
        >>> ts1+ts2 == ts2+ts1
        True
        >>> c+ts1 == ts1+c
        True
        '''
        return self + other

    def __sub__(self, rhs):

        '''
        Elementwise subtract operation

        Parameters
        ----------
        rhs: TimeSeries
            TimeSeries instance with the same 'times' points for TimeSeries subtraction, applied only on 'values' list

        Returns
        -------
        TimeSeries
             result of TimeSeries Class subtracted by parameter 'rhs'

        Raises
        ------
        TypeError
            If values in rhs are not real number
        ValueError
            If time points in self and rhs do not match

        Examples
        --------
        >>> a = TimeSeries([0,5,10], [1,2,3])
        >>> b = TimeSeries([0,5,10], [10,20,30])
        >>> c = 100
        >>> d = TimeSeries([0,1,2], [1,2,3])
        >>> b-a
        TimeSeries([0,5,10],[9,18,27])
        >>> a-c
        TimeSeries([0,5,10],[-99,-98,-97])
        >>> a-d
        ValueError: [[ 0  5 10]
         [ 1  2  3]] and [[0 1 2]
         [1 2 3]] must have the same time points
        '''

        try:
            if isinstance(rhs, numbers.Real):
                return TimeSeries(self._times, self._values - rhs)
            elif self.checkTime(rhs) == True:
                return TimeSeries(self._times, self._values - rhs._values )
            else:
                
                raise ValueError(str(self)+' and '+str(rhs)+' must have the same time points')
        except TypeError:
            raise NotImplemented

    def __mul__(self, rhs):
        '''
        Elementwise multiply operations

        Parameters
        ----------
        rhs: TimeSeries
            TimeSeries instance with the same 'times' points for multiplication, applied only on 'values' list

        Returns
        -------
        TimeSeries
             result of TimeSeries Class multiplied by parameter 'rhs'

        Raises
        ------
        TypeError
            If values in rhs are not real number
        ValueError
            If time points in self and rhs do not match

        Examples
        --------
        >>> a = TimeSeries([0,5,10], [1,2,3])
        >>> b = TimeSeries([0,5,10], [10,20,30])
        >>> c = 100
        >>> d = TimeSeries([0,1,2], [1,2,3])
        >>> a*b
        TimeSeries([0,5,10],[10,40,90])
        >>> a*c
        TimeSeries([0,5,10],[100,200,300])
        >>> a*d
        ValueError: [[ 0  5 10]
         [ 1  2  3]] and [[0 1 2]
         [1 2 3]] must have the same time points
        '''
        try: 
            if isinstance(rhs, numbers.Real):
                return TimeSeries(self._times, self._values * rhs)
            
            elif self.checkTime(rhs)==True: # same length
                return TimeSeries(self._times, self._values * rhs._values)
                
            else:
                raise ValueError(str(self)+' and '+str(rhs)+' must have the same time points')
        
        except TypeError:
            raise NotImplemented

    def __truediv__(self, rhs):
        try:
            if isinstance(rhs, numbers.Real):
                return TimeSeries(self._times, self._values / rhs)
            elif self.checkTime(rhs) == True:
                return TimeSeries(self._times, self._values / rhs._values)

            else:
                raise ValueError(str(self)+' and '+str(rhs)+' must have the same time points')
        except:
            raise NotImplemented

    def __rmul__(self, other):
        '''
        other * self delegates to __mul__
        Parameters
        ----------
        other : TimeSeries
            TimeSeries instance for TimeSeries multiplication

        Returns
        -------
        TimeSeries
             result of TimeSeries Class multiplied by parameter 'other'

        Examples
        --------
        >>> a = TimeSeries([0,5,10], [1,2,3])
        >>> b = TimeSeries([0,5,10], [10,20,30])
        >>> c = 100
        >>> a*b == b*a
        True
        >>> c*a == a*c
        True
        '''

        return self * other

    def __abs__(self):
        '''
        Returns
        -------
        float
            The square root of the sum of all squared values in TimeSeries values list

        Examples
        --------
        >>> a = TimeSeries([0,5], [3,4])
        >>> abs(a)
        5.
        '''

        return np.sqrt(np.sum(np.power(self._values,2)))

    def __bool__(self):
        '''
        Returns
        -------
        bool
            True if the abs value of TimeSeries is greater than zero, False otherwise

        Examples
        --------
        >>> a = TimeSeries([0],[0])
        >>> abs(a)
        False
        '''
        return bool(abs(self))

    def __neg__(self):
        '''
        Returns
        -------
        TimeSeries
            the TimeSeries instance with the same 'times' list but negative (opposite sign) 'values' list

        Examples
        --------
        >>> a = TimeSeries([0,5,10], [1,2,3])
        >>> b = TimeSeries([0,5,10], [10,20,30])
        >>> -a
        TimeSeries([0,5,10],[-1,-2,-3])
        '''
        return TimeSeries(self._times,-1*self._values)
        
    def __pos__(self):
        '''
        Returns
        -------
        TimeSeries
            the TimeSeries instance itself

        Examples
        --------
        >>> a = TimeSeries([0,5,10], [-1,-2,3])
        >>> +a == a
        True

        '''
        return (self)


    # Lab19
    @pype.component
    def std(self):
        '''
        Returns the standard-deviation of self.values

        Returns
        -------
        float
            the standard deviation of self.values

        Raises
        ------
        ValueError
            If self.values is empty

        Examples
        --------
        >>> ts0 = TimeSeries([],[])
        >>> ts1 = TimeSeries(range(0,4),range(1,5))
        >>> ts1.std() == 1.1180339887498949
        >>> ts0.std()
        ValueError: cant calculate standard deviation of length 0 list

        '''
        if(len(self._values) == 0):
            raise ValueError("cant calculate standard deviation of length 0 list")
        return np.std(self._values)

    # TSDB Part 1
    def to_json(self):
        return [[float(i) for i in self.times()],[float(i) for i in self.values()]]

