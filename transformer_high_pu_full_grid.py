import pandapower as pp
from pandapower.powerflow import LoadflowNotConverged


net = pp.networks.create_kerber_vorstadtnetz_kabel_2()
net["ext_grid"].drop(0, inplace=True)
net["trafo"].drop(0, inplace=True)

pp.create_bus(net, vn_kv=10.0, index=9990)
pp.create_transformer_from_parameters(
    net,
    hv_bus=0,
    lv_bus=1,
    sn_mva=100.0,
    vk_percent=10,
    vkr_percent=0.5,
    vn_hv_kv=10.0,
    vn_lv_kv=25.0,  # parametrize vn_lv_kv
    pfe_kw=0.0,
    i0_percent=0.5,
    phase_shift=0.0,
)
pp.create_ext_grid(net, bus=0, vm_pu=1.0, va_degree=0.0)  # parametrize vm_pu
pp.create_load(net, bus=1, p_mw=0.0, q_mvar=0.0)  # parametric p_mw, q_mvar
net["load"]["p_mw"] = 0.0

try:
    pp.runpp(net, algorithm="nr", init="auto")  # wrong initial value, parametrize init_vm_pu
except LoadflowNotConverged as e:
    print("Wrong initial value")
    print(e)

pp.runpp(net, algorithm="nr", init_vm_pu="auto")  # correct initial value, parametrize init_vm_pu
print("Correct initial value")
print(net.res_bus)
print(net.res_trafo)
