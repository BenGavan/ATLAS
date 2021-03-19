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
#     Lep_n(t, weighting)
    InvMassZll(t, weighting)
#    DeltaPhi(t, weighting)
    #ExampleCode(t, weighting)
    #TestAnalysis(t, weighting)
#     InvMassZll(t, weighting)
#     Ptcone(t, weighting)
#     Etcone(t, weighting)
#     InvariantMass_OppositeCharge_SameFlavour_2lep(t, weighting)
#     InvMassZll_ptcone_range(t, weighting)
#      InvariantMass_OppositeCharge_2lep_ForStack(t, weighting)
#    PT_2lep_ForStack(t, weighting)
#      Etcone_ForStack(t, weighting)
#     Ptcone_ForStack(t, weighting)
#     Energy(t, weighting)
#     Lep_n(t, weighting)
#    DeltaPhi(t, weighting)
#     Eta(t, weighting)




# (12:00):  lepCut = "(" + "(lep_charge[0] != lep_charge[1]) && (lep_type[0] == lep_type[1]) && lep_n==2 && (lep_ptcone30[0]+lep_ptcone30[1]) < 1e3      && (inv_mass_Zll > 60000)" + ")"

# (16:00):    lepCut ="(" + "(lep_charge[0] != lep_charge[1]) && (lep_type[0]==lep_type[1]) && lep_n==2 && (inv_mass_Zll > 60e3) && (lep_pt[0]+lep_pt[1]) < 320e3 " + ")"
    

def A(t, weighing):
    ETConeLepCut = "(" + "(lep_charge[0] != lep_charge[1]) && lep_n==2" + ")"
    ETConeQuant = "(lep_etcone20[0] + lep_etcone20[1])/2"
    
    
    MeanPTConeQaunt = "(lep_ptcone30[0]+lep_ptcone30[1])/2"
    PTConeLepCut = "(" + "(lep_charge[0] != lep_charge[1]) && lep_n==2" + ")"
    
    lepCut = PTConeLepCut
    quant = MeanPTConeQaunt
    hist_name = "h_lep_ptcone30"
    bins = "(200,0,5e3)"
    title = "Mean PTcone20 of 2lep"
    xAxis = "PTCone (MeV)"
    yAxis = "Number of entries/bin"
    
    Plot(t, weighting, lepCut, quant, hist_name, bins, title, xAxis, yAxis)

def Plot(t, weighting, lepCut, quant, hist_name, bins, title, xAxis, yAxis):
    t.Draw("{0} >> {1}{2}".format(quant, hist_name, bins), weighting + "*" + lepCut) 
    
    # Set style of histogram.
    h = r.gDirectory.Get(hist_name)
    h.GetXaxis().SetTitle(xAxis)
    h.GetYaxis().SetTitle(yAxis) 
    h.SetTitle(title) 
    h.Write()
        
def InvMassZll(t, weighting):
    
    #lepCut = "(" + "(lep_charge[0] != lep_charge[1]) && (lep_type[0] == lep_type[1]) && lep_n==2 && (lep_ptcone30[0]+lep_ptcone30[1]) <         1e3      && (inv_mass_Zll > 60000) && (inv_mass_Zll < 115e3) " + ")"
#     lepCut ="(" + "(lep_charge[0] != lep_charge[1]) && (lep_type[1]== lep_type[0]) && lep_n==2 && (inv_mass_Zll > 60e3)" + ")"
#     
#     lepCut ="(" + "(lep_charge[0] != lep_charge[1]) && (lep_type[0]==lep_type[1]) && lep_n==2 && (inv_mass_Zll > 60e3) && (lep_pt[0]+lep_pt[1]) < 320e3 " + ")"

#     lepCut ="(" + "(lep_charge[0] != lep_charge[1]) && (lep_type[0]==lep_type[1]) && lep_n==2 && (lep_pt[0]+lep_pt[1]) < 320e3 " + ")"
    
    basic_cut = "(lep_charge[0] != lep_charge[1]) && (lep_type[0] == 11 && lep_type[1] == 11) && lep_n==2"
#     inv_mass_cut = "(inv_mass_Zll > 70e3) && (inv_mass_Zll < 150e3)"
#     etcone_cut = "(lep_etcone20[0] > -2e3 && lep_etcone20[1] > -2e3)" + "&& (lep_etcone20[0] < 6e3 && lep_etcone20[1] < 6e3)"
#     ptcone_cut = "(lep_ptcone30[0] < 5.8e3) && (lep_ptcone30[1] < 5.8e3)"
#     pt_cut = "(lep_pt[0] > 35e3) && (lep_pt[1] > 35e3)"
    
#     lepCut = "(" + basic_cut + "&&" + inv_mass_cut + "&&" + etcone_cut + "&&" + ptcone_cut + "&&" + pt_cut + ")"
    
    lepCut = "(" + basic_cut + ")"

    
    t.SetAlias("inv_mass_Zll","sqrt(2*lep_pt[0]*lep_pt[1]*(cosh(lep_eta[0]-lep_eta[1])-cos(lep_phi[0]-lep_phi[1])))")
  
    t.Draw("inv_mass_Zll >> h_inv_mass_Zll(100,0e3,200e3)", weighting + "*" + lepCut)
    
    h = r.gDirectory.Get("h_inv_mass_Zll")
    h.GetXaxis().SetTitle("Invariant mass (MeV)")
    h.GetYaxis().SetTitle("Number of entries/bin") 
    h.SetTitle("Invarient mass") # TODO: W+ and W- 
    h.Write()
    

def InvariantMass_OppositeCharge_SameFlavour_2lep(t, weighting):
    
    t.SetAlias("inv_mass_Zll","sqrt(2*lep_pt[0]*lep_pt[1]*(cosh(lep_eta[0]-lep_eta[1])-cos(lep_phi[0]-lep_phi[1])))")

    # Filter/cut S.T. opposite charged pair of (e == 11, mu = 13)
    lepCut = "(" + "(lep_charge[0] != lep_charge[1]) && (lep_type[0]==11 && lep_type[1]==11) && lep_n==2 && (inv_mass_Zll > 60000) && ()" + ")"
        
        # try tau-tau:
#     lepCut = "(" + "(lep_charge[0] != lep_charge[1]) && (lep_type[0]!=11 && lep_type[0]!=13 && lep_type[1]!=11 && lep_type[1]!=13) && lep_n==2" + ")"
    
    t.Draw("inv_mass_Zll >> h_inv_mass_Zee(300,60e3,140e3)", weighting + "*" + lepCut) 
    
    # TODO: Plot events with len_n>2
    
    # Set style of histogram.
    h = r.gDirectory.Get("h_inv_mass_Zee")
    h.GetXaxis().SetTitle("Invariant mass (MeV)")
    h.GetYaxis().SetTitle("Number of entries/bin") 
    h.SetTitle("Invarient mass of 2lep - oposite charge of type e") 
    h.Write()
    
    
def InvariantMass_OppositeCharge_2lep_ForStack(t, weighting):
    
    t.SetAlias("inv_mass_Zll","sqrt(2*lep_pt[0]*lep_pt[1]*(cosh(lep_eta[0]-lep_eta[1])-cos(lep_phi[0]-lep_phi[1])))")

    # oposite charged pair of leptons (lep_n == 2)
    lepCut = "(" + "(lep_charge[0] != lep_charge[1]) && lep_n==2 && lep_type[0]==13 && lep_type[1]== 13" + ")"
    
    t.Draw("inv_mass_Zll >> h_inv_mass_Zll(100,0e3,200e3)", weighting + "*" + lepCut) 
    
    # Set style of histogram.
    h = r.gDirectory.Get("h_inv_mass_Zll")
    h.GetXaxis().SetTitle("Invariant mass (MeV)")
    h.GetYaxis().SetTitle("Number of entries/bin") 
    h.SetTitle("Invarient mass of 2lep - oposite charged pair") 
    h.Write()
    
def InvMassZll_ptcone_range(t, weighting):
    t.SetAlias("inv_mass_Zll","sqrt(2*lep_pt[0]*lep_pt[1]*(cosh(lep_eta[0]-lep_eta[1])-cos(lep_phi[0]-lep_phi[1])))")

    lepCut = "(lep_charge[0] != lep_charge[1]) && (Sum$(lep_ptcone30) < 3000) && (Sum$(lep_ptcone30) > 1500) && lep_n==2"

    t.Draw("inv_mass_Zll >> h_inv_mass_Zll(100,50e3,140e3)", weighting + "*" + lepCut)
    
    h_inv_mass_Zll = r.gDirectory.Get("h_inv_mass_Zll")
    h_inv_mass_Zll.GetXaxis().SetTitle("Invariant mass (MeV)")
    h_inv_mass_Zll.GetYaxis().SetTitle("Number of entries/bin") 
    h_inv_mass_Zll.SetTitle("Invarient mass of Zee") # TODO: 2lep 
    h_inv_mass_Zll.Write()
    
def PT_2lep_ForStack(t, weighting):
    
    lepCut = "(" + "(lep_charge[0] != lep_charge[1]) && (lep_type[0] == 11 && lep_type[1] == 11) && lep_n==2" + ")"

    t.SetAlias("inv_mass_Zll","sqrt(2*lep_pt[0]*lep_pt[1]*(cosh(lep_eta[0]-lep_eta[1])-cos(lep_phi[0]-lep_phi[1])))")
    t.Draw("lep_pt[0] >> h_lep_pt_total(100, 0,100e3)", weighting + "*" + lepCut)

    h_lep_pt_mean = r.gDirectory.Get("h_lep_pt_total")
    h_lep_pt_mean.GetXaxis().SetTitle("PT (MeV)")
    h_lep_pt_mean.GetYaxis().SetTitle("Number of entries/bin") 
    h_lep_pt_mean.SetTitle("Total PT of ee")
    h_lep_pt_mean.Write()
    
    
def Ptcone(t, weighting):
    
     # Filter/cut S.T. opposite charged pair of (e == 11, mu = 13)
    lepCut = "(lep_charge[0] != lep_charge[1]) && (lep_type[0]==11 && lep_type[1]==11) && lep_n==2"
    t.Draw("lep_ptcone30[0]+lep_ptcone30[1] >> h_lep_ptcone30(300,1e3,15e3)", weighting + "*" + lepCut)
    
    h = r.gDirectory.Get("h_lep_ptcone30")
    h.GetXaxis().SetTitle("pTcone30 (MeV)")
    h.GetYaxis().SetTitle("Number of entries/bin") 
    h.SetTitle("Total pTcone30 of 2lep - ee pair")  
    h.Write()
    
    
def Ptcone_ForStack(t, weighting):
    #&& (inv_mass_Zll > 60000)
     # Filter/cut S.T. opposite charged pair of (e == 11, mu = 13)
    #lepCut = "(lep_charge[0] != lep_charge[1]) && (lep_type[0]== lep_type[1]) && lep_n==2"
    lepCut ="(" + "(lep_charge[0] != lep_charge[1]) && (lep_type[0]== 11 && lep_type[1] == 11) && lep_n==2 " + ")"
    
    t.SetAlias("inv_mass_Zll","sqrt(2*lep_pt[0]*lep_pt[1]*(cosh(lep_eta[0]-lep_eta[1])-cos(lep_phi[0]-lep_phi[1])))")
    t.Draw("lep_ptcone30[0] >> h_lep_ptcone30(100,0,12e3)", weighting + "*" + lepCut)
    
    h_inv_mass_Zll = r.gDirectory.Get("h_lep_ptcone30")
    h_inv_mass_Zll.GetXaxis().SetTitle("pTcone30 (MeV)")
    h_inv_mass_Zll.GetYaxis().SetTitle("Number of entries/bin") 
    h_inv_mass_Zll.SetTitle("pTcone30")  
    h_inv_mass_Zll.Write()
       
    
def Etcone(t, weighting):
    
    lepCut = "(" + "(lep_charge[0] != lep_charge[1]) && (lep_type[0]==11 && lep_type[1]==11) && lep_n==2" + ")"
#     lepCut = "(" + "(lep_charge[0] == lep_charge[1]) && lep_n!=2" + ")"
    t.Draw("lep_etcone20[0] >> h_lep_etcone(100,0e3,7e3)", weighting + "*" + lepCut)
    
    h_inv_mass_Zll = r.gDirectory.Get("h_lep_etcone")
    h_inv_mass_Zll.GetXaxis().SetTitle("ETcone20 (MeV)")
    h_inv_mass_Zll.GetYaxis().SetTitle("Number of entries/bin") 
    h_inv_mass_Zll.SetTitle("ETcone20 of single muon - mumu pair") 
    h_inv_mass_Zll.Write()   
    
    
def Etcone_ForStack(t, weighting):
    
    #lepCut = "(" + "(lep_charge[0] != lep_charge[1]) && (lep_type[0] == lep_type[1]) && lep_n==2 && (lep_ptcone30[0]+lep_ptcone30[1]) < 1e3      && (inv_mass_Zll > 60000) && (inv_mass_Zll < 115e3) " + ")"
    lepCut ="(" + "(lep_charge[0] != lep_charge[1]) && (lep_type[0]== 13 && lep_type[1] == 13) && lep_n==2" + ")"    
    
    
    t.SetAlias("inv_mass_Zll","sqrt(2*lep_pt[0]*lep_pt[1]*(cosh(lep_eta[0]-lep_eta[1])-cos(lep_phi[0]-lep_phi[1])))")
    t.Draw("abs(lep_etcone20[0]-lep_etcone20[1]) >> h_lep_etcone20(100,-7e3,14e3)", weighting + "*" + lepCut)
    
    h_inv_mass_Zll = r.gDirectory.Get("h_lep_etcone20")
    h_inv_mass_Zll.GetXaxis().SetTitle("ETcone20 (MeV)")
    h_inv_mass_Zll.GetYaxis().SetTitle("Number of entries/bin") 
    h_inv_mass_Zll.SetTitle("ETcone20 difference of pair") 
    h_inv_mass_Zll.Write()  
    
def TransverseMomentum(t, weighting):
    t.Draw("lep_pt >> h_lep_pt(200,0e3,7e3)", weighting)
    
    h_inv_mass_Zll = r.gDirectory.Get("h_lep_pt")
    h_inv_mass_Zll.GetXaxis().SetTitle("Transverse Momentum (MeV)")
    h_inv_mass_Zll.GetYaxis().SetTitle("Number of entries/bin") 
    h_inv_mass_Zll.SetTitle("Transverse Momentum - Z_1lep") 
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

    lepCut = "(" + "(lep_charge[0] != lep_charge[1]) && (lep_type[0] == lep_type[1]) && lep_n==2" + ")"
    t.Draw("lep_n >> h_lep_n(3,-0.5,3.5)", weighting + "*" + lepCut)
    
    h = r.gDirectory.Get("h_lep_n")
    h.GetXaxis().SetTitle("lep_n")
    h.GetYaxis().SetTitle("Number of entries/bin") 
    h.SetTitle("lep_n") 
    h.Write() 
    
    
def DeltaPhi(t, weighting):
#     lepCut ="(" + "(lep_charge[0] != lep_charge[1]) && (lep_type[0]==lep_type[1]) && lep_n==2 && (inv_mass_Zll > 60e3) && (lep_pt[0]+lep_pt[1]) < 320e3 " + ")"
    
    lepCut ="(" + "(lep_charge[0] != lep_charge[1]) && (lep_type[0]==13 && lep_type[1]==13) && lep_n==2 && (inv_mass_Zll > 60e3)" + ")"
    
    t.SetAlias("inv_mass_Zll","sqrt(2*lep_pt[0]*lep_pt[1]*(cosh(lep_eta[0]-lep_eta[1])-cos(lep_phi[0]-lep_phi[1])))")
    t.Draw("abs(lep_phi[0] - lep_phi[1]) >> h_lep_delta_phi(100,0,6.3)", weighting + "*" + lepCut)
    
    h = r.gDirectory.Get("h_lep_delta_phi")
    h.GetXaxis().SetTitle("\Delta \phi")
    h.GetYaxis().SetTitle("Number of entries/bin") 
    h.SetTitle("Difference in azimuthal angle of lepton pair") 
    h.Write() 
    
    
    
    
def Eta(t, weighting):
    
    lepCut ="(" + "(lep_charge[0] != lep_charge[1]) && (lep_type[0]==lep_type[1]) && lep_n==2" + ")"
    
    t.Draw("abs(lep_eta[0]) >> h_lep_eta(100,0,3)", weighting + "*" + lepCut)
    
    h = r.gDirectory.Get("h_lep_eta")
    h.GetXaxis().SetTitle("\eta")
    h.GetYaxis().SetTitle("Number of entries/bin") 
    h.SetTitle("\eta(0) of lepton pair") 
    h.Write()
    
    
    
def InvarMass_4lep(t, weighting):
    
    # cut for 2 l+l- pairs (same type opposite charge)
    
    lepCut ="(" + "(lep_charge[0] != lep_charge[1]) && (lep_type[0]==lep_type[1]) && lep_n==2" + ")"
    
    t.Draw("abs(lep_eta[0]) >> h_lep_eta(100,0,3)", weighting + "*" + lepCut)
    
    h = r.gDirectory.Get("h_inv_mass_4")
    h.GetXaxis().SetTitle("\eta")
    h.GetYaxis().SetTitle("Number of entries/bin") 
    h.SetTitle("\eta(0) of lepton pair") 
    h.Write()
    
    
    
    
    
    
# A bare minimum to create a very basic histogram (number of leptons in events)
def TestAnalysis(t, weighting):
    
    # Draw histogram of the number of leptons between 0 and 9 
    t.Draw("lep_n >> h_lepton_n (10,  -0.5, 9.5)", weighting)
    
    # Retrieve the results of drawing the histograms.
    # This needs to be done for each histogram.
    h_lepton_n = r.gDirectory.Get("h_lepton_n")
    
    # Set style of lep_n histogram.
    h_lepton_n.GetXaxis().SetTitle("Number of leptons per event")
    h_lepton_n.GetYaxis().SetTitle("Number of entries/bin") 
    h_lepton_n.SetTitle("Number of leptons per event")
    h_lepton_n.SetLineColor(r.kRed) 

    # Write histograms to the output file.
    # This needs to be done for each histogram.
    h_lepton_n.Write()
    
#     t.SetAlias("inv_mass_Zll","sqrt(2*lep_pt[0]*lep_pt[1]*(cosh(lep_eta[0]-lep_eta[1])-cos(lep_phi[0]-lep_phi[1])))")
  
#     t.Draw("inv_mass_Zll >> h_inv_mass_2lep(200,0,150e3)", weighting)
    
#     h_inv_mass_Zll = r.gDirectory.Get("h_inv_mass_2lep")
#     h_inv_mass_Zll.GetXaxis().SetTitle("invariant mass (MeV)")
#     h_inv_mass_Zll.GetYaxis().SetTitle("Number of entries/bin") 
#     h_inv_mass_Zll.SetTitle("Invarient mass of ATLAS 2lep")
#     h_inv_mass_Zll.Write()   
    
def ExampleCode(t, weighting):
    # Draw histograms
    # Format is t.Draw("variable_to_plot >> histogram_name (number_of_bins, x_axis_minimum, x_axis_maximum"),weighting)

    
    # A couple of simple examples:
    # 1) Draw a histogram of number of leptons per event.
    t.Draw("lep_n >> h_lep_n(10, -0.5, 9.5)", weighting)
    # 2) Draw a histogram of the "lepton type" of every lepton in every event.
    t.Draw("lep_type >> h_lep_type(10, 7.5, 17.5)", weighting)
    # Note: lepton type takes the value 11 for electrons and 13 for muons
    
    #Draw histogram of invarient mass mll
    t.SetAlias("inv_mass_Zll","Sqrt$(2*lep_pt[0]*lep_pt[1]*(CosH$(lep_eta[0]-lep_eta[1])-Cos$(lep_phi[0]-lep_phi[1]))")
    t.Draw("inv_mass_Zll >> h_inv_mass_Zll(200,0,200e3)")
    
    
    
    # Selection cuts can be used to plot only data that pass certain "selection cuts".
    # For second argument in t.Draw() use (weighting + "* (selection_cuts)")

    # For example, plotting transverse momentum of leptons only for events with 3 or more leptons:
    t.Draw("lep_pt >> h_3lep_pt(200,0,140e3)", weighting + "* (lep_n >= 3)")
    
    
    ### TEST 
    t.Draw("lep_pt >> h_3lep_pt_test(200, 0, 140e3)", weighting + "* (lep_n >= 1)")


    # It is also possible to plot calculated quantities - here is an example
    # To make this easier one can use the function SetAlias("name","formula") to perform intermediate calculations

    # For example, plotting the average transverse momenta of leptons in each event:
    t.SetAlias("meanPt","Sum$(lep_pt)/Length$(lep_pt)") # define meanPt
    t.Draw("meanPt >> h_lep_pt_mean(200,0,140e3)", weighting) # plot meanPt
    # For more information see https://root.cern.ch/doc/master/classTTree.html#a73450649dc6e54b5b94516c468523e45

    
    # It can be useful to define selection cuts that can take input arguments - here is an example
    
    # Define selection cuts for each lepton
    lepCut = "lep_pt[{0}] > 20e3  && lep_type[{0}]=={1}"
    # Note: here "{0}" and "{1}" are dummy arguments that take the values specified when the function is used, as given below 
    
    # Require that both leptons [0] and [1] satisfy the specified selection cuts 
    selCutsE = "(" + lepCut.format(0,11) + "&&" + lepCut.format(1,11) + ")"
    
    # For events containing two electrons satisfying the specified selection cuts plot the average of the pseudorapidity of the two electrons
    t.Draw("(lep_eta[0]+lep_eta[1])/2.0 >> h_electron_eta_average(100,-3.0,3.0)", weighting + "*" + selCutsE)


    # Retrieve the results of drawing the histograms.
    # This needs to be done for each histogram.
    h_lep_n = r.gDirectory.Get("h_lep_n")
    h_lep_type = r.gDirectory.Get("h_lep_type")
    h_3lep_pt = r.gDirectory.Get("h_3lep_pt")
    h_lep_pt_mean = r.gDirectory.Get("h_lep_pt_mean")
    h_electron_eta_average = r.gDirectory.Get("h_electron_eta_average")
    h_inv_mass_Zll = r.gDirectory.Get("h_inv_mass_Zll")
    
    ### Test
    h_3lep_pt_test = r.gDirectory.Get("h_3lep_pt_test")


    # Set style of lep_n  histogram.
    h_lep_n.GetXaxis().SetTitle("Number of leptons per event") # label x axis
    h_lep_n.GetYaxis().SetTitle("Number of entries/bin") # label y axis
    h_lep_n.SetTitle("Number of leptons per event")
    h_lep_n.SetLineColor(r.kRed) # set the line colour to red
    # For more information on histogram styling see https://root.cern.ch/root/htmldoc/guides/users-guide/Histograms.html

    # Note useful trick to get selection cuts used in making a particular histogram written out as a "title" for the histogram
    h_electron_eta_average.SetTitle(selCutsE)

    

    # Write histograms to the output file.
    # This needs to be done for each histogram.
    h_lep_n.Write()
    h_lep_type.Write()
    h_3lep_pt.Write()
    h_lep_pt_mean.Write()
    h_electron_eta_average.Write()
    h_inv_mass_Zll.Write()
    
    
    ### Test
    h_3lep_pt_test.Write()    

