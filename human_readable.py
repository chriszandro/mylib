def create_switch_operation_fixed_start(system, startpoint):
    operation_list =[] 
    for gate in system["gate"]:
        operation_list.append({"gate_init":startpoint ,"gate_final":gate})
    system["operation"] = operation_list
    pass

def create_switch_operation(system):
    operation_list =[] 
    for gate_init in system["gate"]:
       for gate_final in system["gate"]:
            if gate_init!=gate_final:
                operation_list.append({"gate_init":gate_init  ,"gate_final":gate_final})
            
    system["operation"] = operation_list
    pass

def create_switch_operation_around_symmetric(system, symmetric):
    operation_list =[] 
    for gate_init in system["gate"]:
       for gate_final in system["gate"]:
           if gate_init < symmetric < gate_final:
                operation_list.append({"gate_init":gate_init  ,"gate_final":gate_final})
           elif gate_init > symmetric > gate_final:
                operation_list.append({"gate_final":gate_final ,"gate_init":gate_init})
            
    system["operation"] = operation_list
    pass

def human_readable_frank(frank):
    
    if frank == 0.1:
        label = "_shiPlus"
    elif frank == 0.2:
        label = "_shiPlus+"
    elif frank == 0.3:
        label = "_shiPlus++"
    elif frank == 0.4:
        label = "_shiPlus+++"               
    elif frank == 0.6:
        label = "_shiHU_Plu"  
    elif frank == 0.8:
        label = "_shiHU_Plu+"  
    elif frank == -0.1:
        label = "_shiNEG"
    elif frank == -0.2:
        label = "_shiNEG-"
    elif frank == -0.3:
        label = "_shiNEG--"
    elif frank == -0.4:
        label = "_shiNEG---"  
    elif frank == -0.6:
        label = "_shiHU_NEG"     
    elif frank == -0.8:
        label = "_shiHU_NEG-"     
    elif frank == 0:
        label ="_ZeroS"
    else:
        label = ""
        print "no categorized shift is given!"
    
    return label

def human_readable_length(length):
    
    if length==0.5:
        label = "_NORM"
    elif length==0.75:
        label = "_LARGE"
    elif length==0.25:
        label = "_small"
    else:
        label = ""
        print "no categorized length is given!"
        
    return label
                                 
def human_readable_environment(env):

    if env==0.0:
        label = ""
    elif env==0.04:
        label = "_env"
    elif env==1e-3:
        label = "_MenvM"
    elif env==1e-4:
        label = "_MMenvMM"
    elif env==1e-5:
        label = "_MMMenvMMM"
    else:
        label = ""
        print "no categorized environment is given!"
      
    return label

def human_readable_fermion(fermion):
    if fermion == 0:
        label = ""
    else:
        label = "_FERMION"

    return label

def human_readable_temperature(T):
    if T < 50:
        if T == 0:
                label = "_NOTEMP"
        elif T==5:
                label ="_SMATEMP"
        else:
                label = ""
    else:
        label = "_T"
    return label


def human_readable_occupation(occu):
    
    if occu==0:
        label = ""
    elif occu==1:
        label = "_ELEC"
    else:
        label = ""
        print "no categorized occupation is given!"
        
    return label
      
def human_readable_switch_operation(gate_init, gate_final):             
    if gate_init<gate_final: 
        label = "_Switch_ON_"
    else:
        label = "_Switch_OFF_"  
    return label

def set_bath_by_temp(T):
           
    if T < 50:                               
        coupling = 0.01
    elif T > 50:
        coupling = 0.1
        
    return coupling

def human_readable_barrier_change(barrier):
   
    if barrier == -0.4:
        label = "_BarNegHu++"
    elif barrier == -0.3:
        label = "_BarNegHu"
    elif barrier == -0.2:
        label = "_BarNeg--"
    elif barrier == -0.1:
        label = "_BarNeg" 
    elif barrier == 0.1:
        label = "_BarPlu"
    elif barrier == 0.2:
        label = "_BarPlu++"
    elif barrier == 0.3:
        label = "_BarPluHU"
    elif barrier == 0.4:
        label = "_BarPluHU++"

    else:
        label = ""
        print "no categorized Barrier change is given!"
        
    return label

def symmetric_gate_diode_V(Fieldlength=10, biaslength=10, phi=90, U_gate=0, delta=0.1, transloc=1 ):
    
    V = -(biaslength/math.cos(math.radians(phi))) *( (U_gate/Fieldlength)* math.sin(math.radians(phi)) - 0.5*(delta/transloc))
    
    return V

def symmetric_gate_U(Fieldlength=10, delta=0.1, transloc=1):

    U = (Fieldlength*delta)/(2 * transloc)
    
    return U
