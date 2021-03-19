# Analysis.py
# Skeleton code in python provided for you
# In place of this comment you should write [your name] -- [the date] and update it as you go!
# Make sure to make backups and comment as you go along :-)

# allow python to use ROOT
import ROOT as r

"""
List of functin:
 - InvMassZll = Invariant mass plot of Z -> ll
 - DeltaPhi = Differnce in the azimuthal angle between lepton pair.
"""

def Analyse(t,weighting):
#     Eta(t, weighting)
    InvMassZll(t, weighting)
#     PT_2lep(t, weighting)
#     InvarMass_4lep(t, weighting)
#     InvarMass_lepPair_4lep(t, weighting)
#     PT_4lep(t, weighting)
#     Ptcone(t, weighting)
#     Etcone(t, weighting)
#     DeltaPhi(t, weighting)
    
#     print(lep_charge[0])
    

def Eta(t, weighting):
    
    lepCut ="(" + "(lep_charge[0] != lep_charge[1]) && (lep_type[0]==lep_type[1]) && lep_n==2" + ")"
    
    t.Draw("abs(lep_eta[1]) >> h_lep_eta(100,0,3)", weighting + "*" + lepCut)
    
    h = r.gDirectory.Get("h_lep_eta")
    h.GetXaxis().SetTitle("\eta")
    h.GetYaxis().SetTitle("Number of entries/bin") 
    h.SetTitle("\eta(0) of lepton pair") 
    h.Write()
        
def InvMassZll(t, weighting):
    
    basic_cut = "(lep_charge[0] != lep_charge[1]) && (lep_type[0] == 11 && lep_type[1] == 11) && lep_n==2"
#     inv_mass_cut = "(inv_mass_Zll > 65e3) && (inv_mass_Zll < 150e3)"
#     etcone_cut = "(lep_etcone20[0] > -1.6e3 && lep_etcone20[1] > -1.6e3)" + "&& (lep_etcone20[0] < 5.25e3 && lep_etcone20[1] < 5.25e3)"
#     ptcone_cut = "(lep_ptcone30[0] < 6.5e3) && (lep_ptcone30[1] < 6.5e3)"
#     pt_cut = "(lep_pt[0] > 28e3) && (lep_pt[1] > 28e3)"
    
#     inv_mass_cut = "(inv_mass_Zll > 70e3) && (inv_mass_Zll < 150e3)"
    etcone_cut = "(lep_etcone20[0] > -2e3 && lep_etcone20[1] > -2e3)" + "&& (lep_etcone20[0] < 6e3 && lep_etcone20[1] < 6e3)"
    ptcone_cut = "(lep_ptcone30[0] < 5.8e3) && (lep_ptcone30[1] < 5.8e3)"  
    pt_cut = "(lep_pt[0] > 26e3) && (lep_pt[1] > 26e3)"

#     lepCut = "(" + basic_cut + "&&" + etcone_cut + "&&" + ptcone_cut + "&&" + pt_cut + ")"

    lepCut = "(" + basic_cut + "&&" + etcone_cut + "&&" + ptcone_cut + "&&" + pt_cut + ")"
    
    t.SetAlias("inv_mass_Zll","sqrt(2*lep_pt[0]*lep_pt[1]*(cosh(lep_eta[0]-lep_eta[1])-cos(lep_phi[0]-lep_phi[1])))")
  
    t.Draw("inv_mass_Zll >> h_inv_mas(200,0e3,200e3)", weighting + "*" + lepCut)
    
    h = r.gDirectory.Get("h_inv_mas")
    h.GetXaxis().SetTitle("Invariant mass (MeV)")
    h.GetYaxis().SetTitle("Number of entries/bin") 
    h.SetTitle("Invarient mass (ee pair)") 
    h.Write()
    
    
def PT_2lep(t, weighting):
        
    basic_cut = "(lep_charge[0] != lep_charge[1]) && (lep_type[0] == 11 && lep_type[1] == 11) && lep_n==2"
    inv_mass_cut = "(inv_mass_Zll > 65e3) && (inv_mass_Zll < 150e3)"
    etcone_cut = "(lep_etcone20[0] > -2e3 && lep_etcone20[1] > -2e3)" + "&& (lep_etcone20[0] < 6e3 && lep_etcone20[1] < 6e3)"
    ptcone_cut = "(lep_ptcone30[0] < 5.8e3) && (lep_ptcone30[1] < 5.8e3)"
#     pt_cut = "(lep_pt[0] > 35e3) && (lep_pt[1] > 35e3)"
    
    lepCut = "(" + basic_cut + "&&" + etcone_cut + "&&" + ptcone_cut + "&&" + inv_mass_cut + ")"

    t.SetAlias("inv_mass_Zll","sqrt(2*lep_pt[0]*lep_pt[1]*(cosh(lep_eta[0]-lep_eta[1])-cos(lep_phi[0]-lep_phi[1])))")
#     t.Draw("lep_pt[0] >> h_lep_pt_total(100, 0,100e3)", weighting + "*" + lepCut)
    t.Draw("lep_pt[0] >> h_lep_pt(100, 0, 100e3)", weighting + "*" + lepCut)

    h_lep_pt_mean = r.gDirectory.Get("h_lep_pt")
    h_lep_pt_mean.GetXaxis().SetTitle("PT (MeV)")
    h_lep_pt_mean.GetYaxis().SetTitle("Number of entries/bin") 
    h_lep_pt_mean.SetTitle("Total PT of ee")
    h_lep_pt_mean.Write()
    
    
def Ptcone(t, weighting):
    
     # Filter/cut S.T. opposite charged pair of (e == 11, mu = 13) 
    basic_cut = "(lep_charge[0] != lep_charge[1]) && (lep_type[0] == 13 && lep_type[1] == 13) && lep_n==2"
#     inv_mass_cut = "(inv_mass_Zll > 65e3) && (inv_mass_Zll < 150e3)"
#     etcone_cut = "(lep_etcone20[0] > -2e3 && lep_etcone20[1] > -2e3)" + "&& (lep_etcone20[0] < 6e3 && lep_etcone20[1] < 6e3)"
#     ptcone_cut = "(lep_ptcone30[0] < 6.5e3) && (lep_ptcone30[1] < 6.5e3)"
#     pt_cut = "(lep_pt[0] > 26e3) && (lep_pt[1] > 26e3)"
    
#     lepCut = "(" + basic_cut + "&&" + pt_cut + "&&" + inv_mass_cut + "&&" + etcone_cut + ")"
    lepCut = "(" + basic_cut + ")"

    t.SetAlias("inv_mass_Zll","sqrt(2*lep_pt[0]*lep_pt[1]*(cosh(lep_eta[0]-lep_eta[1])-cos(lep_phi[0]-lep_phi[1])))")
   
    t.Draw("lep_ptcone30[0] >> h_lep_ptc(100,0e3,7e3)", weighting + "*" + lepCut)
    
    h = r.gDirectory.Get("h_lep_ptc")
    h.GetXaxis().SetTitle("pTcone30 (MeV)")
    h.GetYaxis().SetTitle("Number of entries/bin") 
    h.SetTitle("Total pTcone30 of 2lep - ee pair")  
    h.Write()
       
    
def Etcone(t, weighting):
    
    basic_cut = "(lep_charge[0] != lep_charge[1]) && (lep_type[0] == 13 && lep_type[1] == 13) && lep_n==2"
#     inv_mass_cut = "(inv_mass_Zll > 65e3) && (inv_mass_Zll < 150e3)"
#     etcone_cut = "(lep_etcone20[0] > -1.6e3 && lep_etcone20[1] > -1.6e3)" + "&& (lep_etcone20[0] < 5.25e3 && lep_etcone20[1] <5.25e3)"
#     ptcone_cut = "(lep_ptcone30[0] < 5.8e3) && (lep_ptcone30[1] < 5.8e3)"
#     pt_cut = "(lep_pt[0] > 26e3) && (lep_pt[1] > 26e3)"
 
    
#     lepCut = "(" + basic_cut + "&&" + pt_cut + "&&" + inv_mass_cut + "&&" + ptcone_cut + ")"
    lepCut = "(" + basic_cut + ")"
    
    t.SetAlias("inv_mass_Zll","sqrt(2*lep_pt[0]*lep_pt[1]*(cosh(lep_eta[0]-lep_eta[1])-cos(lep_phi[0]-lep_phi[1])))")
    
    t.Draw("lep_etcone20[0] >> h_lep_etc(200,-7e3,7e3)", weighting + "*" + lepCut)
    
    h_inv_mass_Zll = r.gDirectory.Get("h_lep_etc")
    h_inv_mass_Zll.GetXaxis().SetTitle("ETcone20 (MeV)")
    h_inv_mass_Zll.GetYaxis().SetTitle("Number of entries/bin") 
    h_inv_mass_Zll.SetTitle("ETcone20 of single muon - mumu pair") 
    h_inv_mass_Zll.Write()   
    
    
def Energy(t, weighting):
    t.Draw("lep_pt >> h_lep_e(200,0e3,7e3)", weighting)
    
    h_inv_mass_Zll = r.gDirectory.Get("h_lep_e")
    h_inv_mass_Zll.GetXaxis().SetTitle("Energy (MeV)")
    h_inv_mass_Zll.GetYaxis().SetTitle("Number of entries/bin") 
    h_inv_mass_Zll.SetTitle("Energy - Z_1lep") 
    h_inv_mass_Zll.Write() 
    
def Lep_n(t, weighting):
    t.SetAlias("inv_mass_Zll","sqrt(2*lep_pt[0]*lep_pt[1]*(cosh(lep_eta[0]-lep_eta[1])-cos(lep_phi[0]-lep_phi[1])))")
    
    basic_cut = "(lep_charge[0] != lep_charge[1]) && (lep_type[0] == 11 && lep_type[1] == 11) && lep_n==2"
    inv_mass_cut = "(inv_mass_Zll > 70e3) && (inv_mass_Zll < 150e3)"
    etcone_cut = "(lep_etcone20[0] > -2e3 && lep_etcone20[1] > -2e3)" + "&& (lep_etcone20[0] < 6e3 && lep_etcone20[1] < 6e3)"
    ptcone_cut = "(lep_ptcone30[0] < 5.8e3) && (lep_ptcone30[1] < 5.8e3)"
    pt_cut = "(lep_pt[0] > 35e3) && (lep_pt[1] > 35e3)"
    
    lepCut = "(" + basic_cut + "&&" + inv_mass_cut + "&&" + etcone_cut + "&&" + ptcone_cut + "&&" + pt_cut + ")"

    t.Draw("lep_n >> h_lep_n(3,-0.5,3.5)", weighting + "*" + lepCut)
    
    h = r.gDirectory.Get("h_lep_n")
    h.GetXaxis().SetTitle("lep_n")
    h.GetYaxis().SetTitle("Number of entries/bin") 
    h.SetTitle("lep_n") 
    h.Write() 
    
    
def DeltaPhi(t, weighting):
#     lepCut ="(" + "(lep_charge[0] != lep_charge[1]) && (lep_type[0]==lep_type[1]) && lep_n==2 && (inv_mass_Zll > 60e3) && (lep_pt[0]+lep_pt[1]) < 320e3 " + ")"
    

    basic_cut = "(" + "(lep_charge[0] != lep_charge[1]) && (lep_type[0] == lep_type[1]) && lep_n==2" + ")"
    

    t.Draw("abs(lep_phi[0] - lep_phi[1]) >> h_lep_delta_phi(100,0,6.3)", weighting + "*" + basic_cut)
    
    h = r.gDirectory.Get("h_lep_delta_phi")
    h.GetXaxis().SetTitle("\Delta \phi")
    h.GetYaxis().SetTitle("Number of entries/bin") 
    h.SetTitle("Difference in azimuthal angle of lepton pair (Z->ee)") 
    h.Write() 
    
    
def Eta(t, weighting):
    
    lepCut ="(" + "(lep_charge[0] != lep_charge[1]) && (lep_type[0]==lep_type[1]) && lep_n==2" + ")"
    
    t.Draw("abs(lep_eta[0]) >> h_lep_eta(100,0,3)", weighting + "*" + lepCut)
    
    h = r.gDirectory.Get("h_lep_eta")
    h.GetXaxis().SetTitle("\eta")
    h.GetYaxis().SetTitle("Number of entries/bin") 
    h.SetTitle("\eta(0) of lepton pair") 
    h.Write()
    
    
def PT_4lep(t, weighting):
    
    lepCut ="(" + "lep_n==4" + ")"
    
    t.Draw("lep_pt[0] >> h_pt_4(100,0e3,200e3)", weighting + "*" + lepCut)
    
    h = r.gDirectory.Get("h_pt_4")
    h.GetXaxis().SetTitle("Inv Mass4 / MeV")
    h.GetYaxis().SetTitle("Number of entries/bin") 
    h.SetTitle("Higgs Inv Mass") 
    h.Write()
    
    
def InvarMass_lepPair_4lep(t, weighting):
    # Allowed processes: ee mumu, ee ee, mumu mumu
    # For an allowed process, the sum of charge * type == 0 
    t_c_b = "(lep_charge[{0}] * lep_type[{0}])"  
    t_c = ""
    
    for i in range(4):
        if i != 0:
            t_c += " + "
        t_c += t_c_b.format(i)

    t.SetAlias("t_c_sum", t_c)
    t_c_cut = "t_c_sum == 0"
    
    # Invariant mass of the two lepton pairs 
    # each have to be within the mass width of Z boson.
    # Will have mulitple pair cominations so need to calculate invariant mass for all possible combinations (combinatorics)
    lep2_invar_mass_str = "sqrt(2*lep_pt[{0}]*lep_pt[{1}]*(cosh(lep_eta[{0}]-lep_eta[{1}])-cos(lep_phi[{0}]-lep_phi[{1}])))"
    t.SetAlias("lep2_inv_mass", lep2_invar_mass_str.format(2, 3))
    
    lepCut ="(" + "lep_n==4" + "&&" + t_c_cut + ")"
    
    t.Draw("lep2_inv_mass >> lep2_inv_mass(80,0e3,500e3)", weighting + "*" + lepCut)
    
    h = r.gDirectory.Get("lep2_inv_mass")
    h.GetXaxis().SetTitle("Inv Mass lep pair (0 and 1) / MeV")
    h.GetYaxis().SetTitle("Number of entries/bin") 
    h.SetTitle("Higgs Inv Mass") 
    h.Write()
    
    
    
def InvarMass_4lep(t, weighting):
    
    # Allowed processes: ee mumu, ee ee, mumu mumu
    # For an allowed process, the sum of charge * type == 0 
    t_c_b = "(lep_charge[{0}] * lep_type[{0}])"  
    t_c = ""
    
    for i in range(4):
        if i != 0:
            t_c += " + "
        t_c += t_c_b.format(i)

    t.SetAlias("t_c_sum", t_c)
    t_c_cut = "t_c_sum == 0"
    
    
    # Generate invariant mass range cut (110 GeV < m_{llll} < 133 GeV)
    invar_mass_cut = "(inv_mass_4 > 110e3 && inv_mass_4 < 133e3)"
    
    # etcone20 (BASIC) cut
    etcone_cut = "( lep_etcone20[0] < 2e3 && lep_etcone20[1] < 2e3 && lep_etcone20[2] < 2e3 && lep_etcone20[3] < 2e3 )"
    
    # etcone (BASIC) cut
#     ptcone_cut = "( lep_ptcone30[0] < 2e3 &&  lep_ptcone30[1] < 2e3 && lep_ptcone30[2] < 2e3 &&  lep_ptcone30[3] < 2e3)"
    
    # Transverse Momentum cut
    pt_cut = "( lep_pt[0] < 70e3 && lep_pt[1] < 70e3 &&  lep_pt[2] < 70e3 &&  lep_pt[3] < 70e3)"
    
    # Invariant mass of the two lepton pairs 
    # one pair has to be within the mass width of Z boson.
    # with another which does not (the virtual z boson)
    # Will have mulitple pair cominations so need to calculate invariant mass for all possible combinations (combinatorics)

    lep2_invar_mass_str = "sqrt(2*lep_pt[{0}]*lep_pt[{1}]*(cosh(lep_eta[{0}]-lep_eta[{1}])-cos(lep_phi[{0}]-lep_phi[{1}])))"

    t_c_pair = "(lep_charge[{0}] * lep_type[{0}]) + (lep_charge[{1}] * lep_type[{1}])"

    lep_pair_inv_mass_cut = ""

    i = 0
    for j in range(1, 4):
        for k in range(1, 3):
            for l in range(2, 4):
                if j != k and j != l and k != l and k < l:
                    if not (j == 1 and k == 2 and l == 3):
                        lep_pair_inv_mass_cut += " || "
                    lep_pair_inv_mass_cut += lep2_invar_mass_str.format(i, j) + " > 60e3 && " + lep2_invar_mass_str.format(i, j) + " < 150e3 && " + lep2_invar_mass_str.format(k,l) + " < 60e3" + " && " + t_c_pair.format(i, j) + " == 0 && " + t_c_pair.format(k,l) + " == 0" + " || " + lep2_invar_mass_str.format(k, l) + " > 60e3 && " + lep2_invar_mass_str.format(k, l) + " < 150e3 && " + lep2_invar_mass_str.format(i,j) + " < 60e3" + " && " + t_c_pair.format(k, l) + " == 0 && " + t_c_pair.format(i, j) + " == 0"
    
    # Calulcate invariant mass of Higgs from the 4 leptons.
    x = "2 * lep_pt[{0}] * lep_pt[{1}]*(cosh(lep_eta[{0}]-lep_eta[{1}]) - cos(lep_phi[{0}]-lep_phi[{1}]))"
    s = ""

    for i in range(4):
        for j in range(i+1, 4):
            if not (i == 0 and j == 1):
                s += "+"
            s += x.format(i, j)
 
    t.SetAlias("s", s)
    t.SetAlias("inv_mass_4", "sqrt(s)")

#     lepCut ="(" + "lep_n==4" + "&&" + t_c_cut + "&&" + lep_pair_inv_mass_cut + "&&" + invar_mass_cut +  "&&" + etcone_cut + "&&" + ptcone_cut + "&&" + pt_cut + ")"
    lepCut ="(" + "lep_n==4" + "&&" + t_c_cut + "&&" + lep_pair_inv_mass_cut + "&&" + invar_mass_cut +  "&&" + etcone_cut + "&&" + "&&" + pt_cut + ")"
    
#     lepCut ="(" + "lep_n==4" + "&&" + t_c_cut + "&&" + lep_pair_inv_mass_cut + "&&" + invar_mass_cut + ")"
    
    t.Draw("lep_ptcone30[0] >> h_lep_ptcf(70,0e3,20e3)", weighting + "*" + lepCut)
    
    h = r.gDirectory.Get("h_lep_ptcf")
    h.GetXaxis().SetTitle("Inv Mass4 / MeV")
    h.GetYaxis().SetTitle("Number of entries/bin") 
    h.SetTitle("Higgs Inv Mass") 
    h.Write()
    
    
    
   