#
#
import matplotlib.pyplot as plt

# mumu
# xs = [50, 60, 70, 80, 90, 100]
# ys = [1.986, 1.992, 2.070, 1.985, 1.983, 2.044] # 70, 80, 90, 100


# xs = [30,35,40, 45, 50]
# ys = [1.988, 2.070, 1.993, 2.085, 2.243]

xs = [150, 140, 130, 120, 110, 100]
ys = [1.978, 1.977, 1.977, 1.976, 1.975, 1.973]

plt.plot(xs, ys, 'kx')
plt.title(r'Z $\rightarrow \mu\mu$')
plt.xlabel('$m_{\mu\mu}$ upper bound cut (GeV)')
plt.ylabel('cross section (nb)')
plt.show()

xs = [60, 70, 80, 90]
ys = [1.979
1.977
1.975
1.971]

# #
# #
# # xs = [0, 55, 80]
# # ys = [2.055, 2.014, 2.027]
# #
# # plt.plot(xs, ys, 'kx')
# # plt.title('Z -> ee')
# # plt.xlabel('pT cut')
# # plt.ylabel('cross section')
# # plt.show()
#
# t_c_b = "(lep_charge[{0}] * lep_type[{0}])"
# t_c = ""
#
# for i in range(4):
#     if i != 0:
#         t_c += " + "
#     t_c += t_c_b.format(i)
#
# print(t_c)
#
# x = "2 * lep_pt[{0}] * lep_pt[{1}]*(cosh(lep_eta[{0}]-lep_eta[{1}]) - cos(lep_phi[{0}]-lep_phi[{1}]))"
# s = ""
#
# for i in range(4):
#     for j in range(i+1, 4):
#         if not (i == 0 and j == 1):
#             s += "+"
#         s += x.format(i, j)
#
# print(s)
#
#
# # 01 23
# i = 0
# # j = 1
# # k = 2
# # l = 3
#
# lep2_invar_mass_str = "sqrt(2*lep_pt[{0}]*lep_pt[{1}]*(cosh(lep_eta[{0}]-lep_eta[{1}])-cos(lep_phi[{0}]-lep_phi[{1}])))"
#
# t_c_pair = "(lep_charge[{0}] * lep_type[{0}]) + (lep_charge[{1}] * lep_type[{1}])"
#
# s = ""
#
# for j in range(1, 4):
#     for k in range(1, 3):
#         for l in range(2, 4):
#             if j != k and j != l and k != l and k < l:
#                 print(i, j, k, l)
#                 if not (j == 1 and k == 2 and l == 3):
#                     s += " || "
#                 s += lep2_invar_mass_str.format(i, j) + " > 60e3 && " + lep2_invar_mass_str.format(i, j) + " < 150e3 && " + \
#                      lep2_invar_mass_str.format(k,l) + " < 150e3" + " && " + t_c_pair.format(i, j) + " == 0 && " + t_c_pair.format(k,l) + " == 0" + \
#                      " || " + lep2_invar_mass_str.format(k, l) + " > 60e3 && " + lep2_invar_mass_str.format(k, l) + " < 150e3 && " + \
#                      lep2_invar_mass_str.format(i,j) + " < 150e3" + " && " + t_c_pair.format(k, l) + " == 0 && " + t_c_pair.format(i, j) + " == 0"
#                 print(s)
#
#
#
# def InvMass4lep(t, weighting):
#     basic_cut = "lep_n==4"
#
#     x = "2 * lep_pt[{0}]*lep_pt[{1}] * (cosh(lep_eta[{0}]- lep_eta[{1}]) - cos( lep_phi[{0}] - lep_phi[{1}]))"
#     s = ""
#
#     for i in range(4):
#         for j in range(i + 1, 4):
#             s += "+" + x.format(i, j)
#
#     t.Draw("s >> h_inv_mass_4lep(100,0e3,200e3)", weighting + "*" + lepCut)
#
#     h = r.gDirectory.Get("h_inv_mass_4lep")
#     h.GetXaxis().SetTitle("Invariant mass (MeV)")
#     h.GetYaxis().SetTitle("Number of entries/bin")
#     h.SetTitle("Invarient mass")  # TODO: W+ and W-
#     h.Write()
#
# if __name__ == '__main__':
#     pass
#
