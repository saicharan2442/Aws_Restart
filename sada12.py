#Exercise 1: Assigning variables, lists, and dictionaries

# Python3.6
# Coding: utf-8
# Store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
# Store the remaining sequence elements of human insulin in variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"
insulin = bInsulin + aInsulin

# pKR values
pKR = {'y': 10.07, 'c': 8.18, 'k': 10.53, 'h': 6.00, 'r': 12.48, 'd': 3.65, 'e': 4.25}

#Exercise 2: Using count() to count the numbers of each amino acid
insulin.count("y")   # lowercase
float(insulin.count("y"))
seqCount = {x: float(insulin.count(x)) for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']}

# Debug: show counts
print("Amino acid counts:", seqCount)

#Exercise 3: Writing the net charge formula
pH = 0
while pH <= 14:
    # Positive groups (lysine, histidine, arginine)
    pos_charge = sum(
        (seqCount[x] * (10.0 ** pKR[x])) / ((10.0 ** pH) + (10.0 ** pKR[x]))
        for x in ['k', 'h', 'r']
    )

    # Negative groups (tyrosine, cysteine, aspartic acid, glutamic acid)
    neg_charge = sum(
        (seqCount[x] * (10.0 ** pH)) / ((10.0 ** pH) + (10.0 ** pKR[x]))
        for x in ['y', 'c', 'd', 'e']
    )

    netCharge = pos_charge - neg_charge

    print('{0:.2f}'.format(pH), netCharge)

    pH += 1


#or--------------------------------------
    
    # Store the human preproinsulin sequence in a variable called preproinsulin:  
'''preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  

# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

# pKR values
pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}

# Count amino acids (lowercase)
seqCount = {x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']}

print("Amino acid counts:", seqCount)  # <-- Debug check

# Net charge calculation
pH = 0
while pH <= 14:
    # Positive groups
    pos_charge = sum(
        (seqCount[x] * (10.0**pKR[x])) / ((10.0**pH) + (10.0**pKR[x]))
        for x in ['k', 'h', 'r']
    )
    
    # Negative groups
    neg_charge = sum(
        (seqCount[x] * (10.0**pH)) / ((10.0**pH) + (10.0**pKR[x]))
        for x in ['y', 'c', 'd', 'e']
    )
    
    netCharge = pos_charge - neg_charge
    
    print('{0:.2f}'.format(pH), netCharge)
    
    pH += 1'''
