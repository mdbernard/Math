class RK4
{
    private:
        float dxdt;
        float x_0;
        float t_0;
        float dt;
        float val = RK4::eval()

    public:
        void set_dt(float new_dt);
        float calc_k1();
        float calc_k2(float k1);
        float calc_k3(float k2);
        float calc_k4(float k3);
        float m();
        float eval();
}

void RK4::set_dt(float new_dt)
{
    dt = new_dt;
    val = RK4::eval()
}

float RK4::calc_k1()
{
    return dxdt(x_0, t_0);
}

float RK4::calc_k2(float k1)
{
    float t = t_0 + (0.5 * dt);
    float x = x_0 + (k1 * t);
    return dxdt(x, t);
}

float RK4::calc_k3(float k2)
{
    float t = t_0 + (0.5 * dt);
    float x = x_0 + (k2 * t);
    return dxdt(x, t);
}

float RK4::calc_k4(float k3)
{
    float t = t_0 + dt;
    float x = x_0 + (k3 * t)
    return dxdt(x, t)
}

float RK4::m()
{
    float k1 = RK4::calc_k1();
    float k2 = RK4::calc_k2(k1);
    float k3 = RK4::calc_k3(k2);
    float k4 = RK4::calc_k4(k3);

    return (1.0/6.0) * (k1 + 2*k2 + 2*k3 + k4);
}

float RK4::eval()
{
    return x_0 + (m() * dt)
}
