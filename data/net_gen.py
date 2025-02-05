import numpy as np

if __name__ == "__main__" and __package__ is None:
    import sys
    from os import path

    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    from complete_net import HighGenSegmentedNet, TrafoHighPuSegmentedNet
    from simple_net import HighGenInjectionNet, TrafoHighPuNet
else:
    from .complete_net import HighGenSegmentedNet, TrafoHighPuSegmentedNet
    from .simple_net import HighGenInjectionNet, TrafoHighPuNet

VM_PU_RANGE = [0.9, 3.0]  #
P_MW_RANGE = [0.0, 1000.0]  #
Q_MVAR_RANGE = [0.0, 0.5]  #
VN_LV_KV_RANGE = [0.9, 3.0]  #
INIT_VM_PU_MIN = 0.9  #
INIT_VM_PU_MAX = 3.0  #
TOTAL_P_GEN_RANGE_MAX = 1000.0
TOTAL_Q_GEN_RANGE_MAX = 0.5


def sample_net_high_gen_inj_xs(N):
    nets = []
    for _ in range(N):
        vm_pu = np.random.uniform(VM_PU_RANGE[0], VM_PU_RANGE[1])
        p_mw = np.random.uniform(P_MW_RANGE[0], P_MW_RANGE[1])
        q_mvar = np.random.uniform(Q_MVAR_RANGE[0], Q_MVAR_RANGE[1])
        init_vm_pu = [
            np.random.uniform(INIT_VM_PU_MIN, INIT_VM_PU_MAX),
            np.random.uniform(INIT_VM_PU_MIN, INIT_VM_PU_MAX),
        ]

        net_instance = HighGenInjectionNet(vm_pu, p_mw, q_mvar, init_vm_pu)
        nets.append(net_instance)

    return nets


def sample_net_trafo_high_pu_xs(N):
    nets = []
    for _ in range(N):
        vm_pu = np.random.uniform(VM_PU_RANGE[0], VM_PU_RANGE[1])
        p_mw = np.random.uniform(P_MW_RANGE[0], P_MW_RANGE[1])
        q_mvar = np.random.uniform(Q_MVAR_RANGE[0], Q_MVAR_RANGE[1])
        vn_lv_kv = np.random.uniform(VN_LV_KV_RANGE[0], VN_LV_KV_RANGE[1])
        init_vm_pu = [
            np.random.uniform(INIT_VM_PU_MIN, INIT_VM_PU_MAX),
            np.random.uniform(INIT_VM_PU_MIN, INIT_VM_PU_MAX),
        ]

        net_instance = TrafoHighPuNet(vm_pu, p_mw, q_mvar, vn_lv_kv, init_vm_pu)
        nets.append(net_instance)

    return nets


def sample_net_high_gen_segmented_xl(N):
    nets = []
    for _ in range(N):
        vm_pu = np.random.uniform(VM_PU_RANGE[0], VM_PU_RANGE[1])
        p_mw = np.random.uniform(P_MW_RANGE[0], P_MW_RANGE[1])
        q_mvar = np.random.uniform(Q_MVAR_RANGE[0], Q_MVAR_RANGE[1])
        total_p_gen = np.random.uniform(0.0, TOTAL_P_GEN_RANGE_MAX)
        total_q_gen = np.random.uniform(0.0, TOTAL_Q_GEN_RANGE_MAX)
        init_vm_pu = np.random.uniform(INIT_VM_PU_MIN, INIT_VM_PU_MAX)

        net_instance = HighGenSegmentedNet(vm_pu, p_mw, q_mvar, total_p_gen, total_q_gen, init_vm_pu)
        nets.append(net_instance)

    return nets


def sample_net_trafo_high_pu_segmented_xl(N):
    nets = []
    for _ in range(N):
        vm_pu = np.random.uniform(VM_PU_RANGE[0], VM_PU_RANGE[1])
        vn_lv_kv = np.random.uniform(VN_LV_KV_RANGE[0], VN_LV_KV_RANGE[1])
        total_p_gen = np.random.uniform(0.0, TOTAL_P_GEN_RANGE_MAX)
        total_q_gen = np.random.uniform(0.0, TOTAL_Q_GEN_RANGE_MAX)
        init_vm_pu = np.random.uniform(INIT_VM_PU_MIN, INIT_VM_PU_MAX)

        net_instance = TrafoHighPuSegmentedNet(vm_pu, vn_lv_kv, total_p_gen, total_q_gen, init_vm_pu)
        nets.append(net_instance)

    return nets


if __name__ == "__main__":
    foo = sample_net_trafo_high_pu_segmented_xl(2)
    foo[0].run_power_flow()
    foo[1].run_power_flow()
