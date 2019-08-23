class RK4:
    def __init__(self, dxdt, x_0, t_0, dt):
        '''
        Runge-Kutta 4th Order Integrator. Set a new dt to
        calculate at some new t = t_0 + dt.

        :param dxdt: the derivative function of x(t)
        :param x_0: the value of x(t_0)
        :param t_0: some value of t for which x(t_0) is known
        :param dt: the time step the integrator should use

        :type dxdt: function
        :type x_0: float
        :type t_0: float
        :type dt: float
        '''

        self.dxdt = dxdt
        self.x_0 = x_0
        self.t_0 = t_0
        self.dt = dt

        self.val = self.eval()

    def set_dt(self, dt):
        '''
        The user sets a new time step from the known value (x_0, t_0)
        and the value x(t_0 + dt) will be found for the new dt.

        :param dt: the new time step
        :type dt: float
        '''
        self.dt = dt
        self.val = self.eval()

    def k_1(self):
        return self.dxdt(self.x_0, self.t_0)

    def k_2(self, k1):
        t = self.t_0 + (0.5 * self.dt)
        x = self.x_0 + (k1 * t)
        return self.dxdt(x, t)

    def k_3(self, k2):
        t = self.t_0 + (0.5 * self.dt)
        x = self.x_0 + (k2 * t)
        return self.dxdt(x, t)

    def k_4(self, k3):
        t = self.t_0 + self.dt
        x = self.x_0 + (k3 * t)
        return self.dxdt(x, t)
    
    def m(self):
        k1 = self.k_1()
        k2 = self.k_2(k1)
        k3 = self.k_3(k2)
        k4 = self.k_4(k3)

        return (1/6) * (k1 + 2*k2 + 2*k3 + k4)

    def eval(self):
        return self.x_0 + (self.m() * self.dt)
