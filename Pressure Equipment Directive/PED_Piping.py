import matplotlib.pyplot as plt
import numpy as np

# ------------------- GROUP 1 GAS -------------------
def classify_piping_group1_gas(PS, DN):
    if PS <= 0.5:
        return "SEP"
    if DN <= 25:
        return "SEP"
    product = PS * DN
    if 25 < DN <= 100:
        if product <= 1000:
            return "I"
        elif product <= 3500:
            return "II"
        else:
            return "III"
    elif 100 < DN <= 350:
        if product <= 3500:
            return "I"
        else:
            return "III"
    elif DN > 350:
        return "III"
    else:
        return "Unknown"

def plot_piping_group1_gas_with_point(PS, DN, category):
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1, 10000)
    ax.set_ylim(0.5, 1000)
    ax.set_xlabel("DN (mm)")
    ax.set_ylabel("PS (bar)")
    ax.set_title("PED Classification - Piping, Group 1 Gas")
    ax.hlines(0.5, 0.1, 10000, color='black', linewidth=1.5, label="PS = 0.5")
    ax.vlines(25, 0.5, 10000, color='green', linewidth=2, label="DN = 25")
    ax.vlines(100, 0.5, 10, color='blue', linewidth=2, label="DN = 100 (lower)")
    ax.vlines(100, 35, 10000, color='blue', linewidth=2, label="DN = 100 (upper)")
    ax.vlines(350, 0.5, 3500/350, color='purple', linewidth=2, label="DN = 350")
    DN_diag1 = np.logspace(np.log10(25), np.log10(100), 300)
    PS_diag1 = 1000 / DN_diag1
    ax.plot(DN_diag1, PS_diag1, color='orange', linewidth=2, label="PS·DN = 1000")
    DN_diag2 = np.logspace(np.log10(100), np.log10(350), 300)
    PS_diag2 = 3500 / DN_diag2
    ax.plot(DN_diag2, PS_diag2, color='red', linewidth=2, label="PS·DN = 3500")
    ax.text(15, 1, "SEP", fontsize=12)
    ax.text(35, 2, "I", fontsize=13)
    ax.text(70, 20, "II", fontsize=13)
    ax.text(500, 500, "III", fontsize=13)
    ax.scatter(DN, PS, color='blue', s=120, edgecolors='black', marker='x', label=f"Operating Point: {category}")
    ax.grid(True, which="both", linestyle='--', linewidth=0.5)
    ax.legend(loc='lower right', fontsize=8)
    plt.tight_layout()
    plt.show()

# ------------------- GROUP 2 GAS -------------------
def classify_group2_gas_piping(PS, DN):
    if PS <= 0.5:
        return "SEP"
    PDN = PS * DN
    if DN <= 32 or PDN <= 1000:
        return "SEP"
    elif 32 < DN <= 100 and PDN <= 3500:
        return "I"
    elif 100 < DN <= 250 and PDN <= 5000:
        return "II"
    else:
        return "III"

def plot_group2_gas_piping(PS, DN, category):
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1, 10000)
    ax.set_ylim(0.5, 1000)
    ax.set_xlabel("DN (mm)")
    ax.set_ylabel("PS (bar)")
    ax.set_title("PED Classification - Piping, Group 2 Gas")
    ax.hlines(0.5, 0.1, 10000, color='black', linewidth=1.5, label="PS = 0.5")
    ax.vlines(32, 31.25, 10000, color='green', linewidth=2, label="DN = 32")
    ax.vlines(100, 35, 10000, color='blue', linewidth=2, label="DN = 100")
    ax.vlines(250, 20, 10000, color='purple', linewidth=2, label="DN = 250")
    dn_1000 = np.logspace(np.log10(32), np.log10(2000), 300)
    ps_1000 = 1000 / dn_1000
    ax.plot(dn_1000, ps_1000, color='orange', linewidth=2, label="PS·DN = 1000")
    dn_3500 = np.logspace(np.log10(100), np.log10(7000), 300)
    ps_3500 = 3500 / dn_3500
    ax.plot(dn_3500, ps_3500, color='red', linewidth=2, label="PS·DN = 3500")
    dn_5000 = np.logspace(np.log10(250), np.log10(10000), 300)
    ps_5000 = 5000 / dn_5000
    ax.plot(dn_5000, ps_5000, color='brown', linewidth=2, label="PS·DN = 5000")
    ax.text(10, 1, "SEP", fontsize=12)
    ax.text(45, 2, "I", fontsize=13)
    ax.text(150, 20, "II", fontsize=13)
    ax.text(500, 500, "III", fontsize=13)
    ax.scatter(DN, PS, color='blue', s=120, edgecolors='black', marker='x', label=f"Operating Point: {category}")
    ax.grid(True, which="both", linestyle='--', linewidth=0.5)
    ax.legend(loc='lower right', fontsize=9)
    plt.tight_layout()
    plt.show()

# ------------------- GROUP 1 LIQUID -------------------
def classify_group1_liquid_piping(PS, DN):
    if PS <= 0.5 or DN <= 25:
        return "SEP"
    PDN = PS * DN
    if PDN <= 2000 or PS <= 10:
        return "I"
    elif PS <= 500:
        return "II"
    else:
        return "III"

def plot_group1_liquid_piping_with_point(PS, DN, category):
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1, 10000)
    ax.set_ylim(0.5, 1000)
    ax.set_xlabel("DN (mm)")
    ax.set_ylabel("PS (bar)")
    ax.set_title("PED Classification - Piping, Group 1 Liquid")
    ax.hlines(0.5, 1, 10000, colors='blue', linewidth=1.5, label="PS = 0.5")
    ax.hlines(10, 200, 10000, colors='green', linewidth=1.5, label="PS = 10")
    ax.hlines(500, 25, 10000, colors='red', linewidth=1.5, label="PS = 500")
    ax.vlines(25, 80, 1000, colors='orange', linewidth=1.5, label="DN = 25")
    DN_vals = np.logspace(np.log10(25), np.log10(4000), 400)
    PS_vals = 2000 / DN_vals
    ax.plot(DN_vals, PS_vals, color='purple', linewidth=1.5, label="PS·DN = 2000")
    ax.text(4500, 6, "I", fontsize=12)
    ax.text(300, 15, "II", fontsize=12)
    ax.text(100, 600, "III", fontsize=12)
    ax.text(5, 1, "SEP", fontsize=10)
    ax.scatter(DN, PS, color='blue', s=100, marker='x', zorder=5, label=f"Operating Point: {category}")
    ax.grid(True, which="both", linestyle='--', linewidth=0.5)
    ax.legend(loc='lower right')
    plt.tight_layout()
    plt.show()

# ------------------- GROUP 2 LIQUID -------------------
def classify_group2_liquid_piping(PS, DN):
    if PS <= 0.5:
        return "SEP"
    PDN = PS * DN
    if PS <= 10 or PDN <= 5000:
        return "I"
    elif PS <= 500:
        return "II"
    else:
        return "II"

def plot_group2_liquid_piping_with_point(PS, DN, category):
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1, 10000)
    ax.set_ylim(0.5, 1000)
    ax.set_xlabel("DN (mm)")
    ax.set_ylabel("PS (bar)")
    ax.set_title("PED Classification - Piping, Group 2 Liquid")
    ax.hlines(0.5, 1, 10000, colors='blue', linewidth=1.5, label="PS = 0.5")
    ax.hlines(10, 500, 10000, colors='green', linewidth=1.5, label="PS = 10")
    ax.hlines(500, 200, 10000, colors='red', linewidth=1.5, label="PS = 500")
    ax.vlines(200, 25, 1000, colors='orange', linewidth=1.5, label="DN = 200")
    DN_vals = np.logspace(np.log10(200), np.log10(500), 400)
    PS_vals = 5000 / DN_vals
    ax.plot(DN_vals, PS_vals, color='purple', linewidth=1.5, label="PS·DN = 5000")
    ax.text(350, 20, "I", fontsize=12)
    ax.text(250, 600, "II", fontsize=12)
    ax.text(10, 1.2, "SEP", fontsize=10)
    ax.scatter(DN, PS, color='blue', s=100, marker='x', zorder=5, label=f"Operating Point: {category}")
    ax.grid(True, which="both", linestyle='--', linewidth=0.5)
    ax.legend(loc='lower right')
    plt.tight_layout()
    plt.show()

# ------------------- MAIN HANDLER -------------------
def run_ped_classification_and_plot(PS, DN, fluid_state, fluid_group):
    if fluid_state == "gas":
        if fluid_group == 1:
            cat = classify_piping_group1_gas(PS, DN)
            plot_piping_group1_gas_with_point(PS, DN, cat)
        else:
            cat = classify_group2_gas_piping(PS, DN)
            plot_group2_gas_piping(PS, DN, cat)
    elif fluid_state == "liquid":
        if fluid_group == 1:
            cat = classify_group1_liquid_piping(PS, DN)
            plot_group1_liquid_piping_with_point(PS, DN, cat)
        else:
            cat = classify_group2_liquid_piping(PS, DN)
            plot_group2_liquid_piping_with_point(PS, DN, cat)
    else:
        print("Invalid fluid state")
        return

 

# Example call
run_ped_classification_and_plot(PS=80, DN=90, fluid_state="gas", fluid_group=1)
