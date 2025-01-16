# source(10kV)-node_0-line(1 ohm)-node_1-load(25*-15 = -375MW)
# node_0 = 10kV
# node_1 = 25kV (should be the answer), node_1 = -15kV (V = 15kV, angle = 180 degrees)

import pandapower as pp
import pandapower.networks as pn
from pandapower.powerflow import LoadflowNotConverged


net = pn.create_kerber_vorstadtnetz_kabel_2()
net["ext_grid"].drop(0, inplace=True)


pp.create_bus(net, vn_kv=10.0, index=9990)
pp.create_line_from_parameters(
    net,
    from_bus=9990,
    to_bus=0,
    length_km=0.01,
    r_ohm_per_km=1.0,
    x_ohm_per_km=1.0,
    c_nf_per_km=1.0,
    g_us_per_km=0.0,
    max_i_ka=100.0
)
pp.create_ext_grid(net, bus=9990, vm_pu=1.0, va_degree=0.0)  # parametrize vm_pu
# TODO Note sgen commented out
# pp.create_sgen(net, bus=1, p_mw=25.0 * 15.0, q_mvar=0.0)  # parametric p_mw, q_mvar

try:
    pp.runpp(net, algorithm="nr", init="auto")  # wrong initial value, parametrize init_vm_pu
except LoadflowNotConverged as e:
    print("Wrong initial value")
    print(e)

pp.runpp(net, algorithm="nr", init="auto")  # correct initial value, parametrize init_vm_pu
print("Correct initial value")
print(net.res_bus)
print(net.res_trafo)
