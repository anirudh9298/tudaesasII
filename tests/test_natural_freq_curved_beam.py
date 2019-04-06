import numpy as np
from structsolve import freq

from tudaesasII.beam2D import Beam2D, update_K_M

def test_nat_freq_curved_beam():
    n = 100
    # comparing with:
    # https://www.sciencedirect.com/science/article/pii/S0168874X06000916
    # see section 5.4
    E = 206.8e9 # Pa
    rho = 7855 # kg/m3
    A = 4.071e-3
    Izz = 6.456e-6

    thetabeam = np.deg2rad(97)
    r = 2.438
    thetas = np.linspace(0, thetabeam, n)
    x = r*np.cos(thetas)
    y = r*np.sin(thetas)

    # getting nodes
    ncoords = np.vstack((x ,y)).T
    nids = 1 + np.arange(ncoords.shape[0])
    nid_pos = dict(zip(nids, np.arange(len(nids))))

    n1s = nids[0:-1]
    n2s = nids[1:]

    K = np.zeros((3*n, 3*n))
    M = np.zeros((3*n, 3*n))
    beams = []
    for n1, n2 in zip(n1s, n2s):
        pos1 = nid_pos[n1]
        pos2 = nid_pos[n2]
        x1, y1 = ncoords[pos1]
        x2, y2 = ncoords[pos2]
        A1 = A2 = A
        Izz1 = Izz2 = Izz
        beam = Beam2D()
        beam.n1 = n1
        beam.n2 = n2
        beam.E = E
        beam.rho = rho
        beam.A1, beam.A2 = A1, A2
        beam.Izz1, beam.Izz2 = Izz1, Izz2
        update_K_M(beam, nid_pos, ncoords, K, M)
        beams.append(beam)

    # applying boundary conditions
    # simply supported at both ends
    K[0:2, :] = 0
    K[:, 0:2] = 0
    M[0:2, :] = 0
    M[:, 0:2] = 0

    K[-3:-1, :] = 0
    K[:, -3:-1] = 0
    M[-3:-1, :] = 0
    M[:, -3:-1] = 0

    eigvals, eigmodes = freq(K, M, sparse_solver=True, silent=True)
    omegan = ((-eigvals)**0.5).real
    omega123 = [396.98, 931.22, 1797.31]
    print('Reference omega123', omega123)
    print('Numerical omega123', omegan[0:3])
    assert np.allclose(omega123, omegan[0:3], rtol=0.01)

if __name__ == '__main__':
    test_nat_freq_curved_beam()