import matplotlib.pyplot as plt
import numpy as np

def classify_piping_group1_gas(PS, DN):
    """
    Classify PED category for Piping – Group 1 Gas.

    Parameters:
        PS (float): Pressure in bar
        DN (float): Nominal Diameter in mm

    Returns:
        str: PED Category - 'SEP', 'I', 'II', 'III', or a message if outside scope
    """
    if PS <= 0.5:
        return "Not in PED scope (PS ≤ 0.5 bar)"
    
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
    """
    Plot PED classification chart for Piping – Group 1 Gas and mark operating point.
    """
    plt.figure(figsize=(8, 6))
    ax = plt.gca()
    ax.set_xscale("log")
    ax.set_yscale("log")

    plt.xlabel("DN (mm)")
    plt.ylabel("PS (bar)")
    plt.title("PED Classification - Piping, Group 1 Gas")

    # Boundary lines
    plt.hlines(0.5, xmin=0.1, xmax=10000, colors='black', linewidth=1, label="PS = 0.5")
    plt.vlines(25, ymin=0.5, ymax=10000, colors='black', linewidth=1, label="DN = 25")
    plt.vlines(100, ymin=0.5, ymax=10, colors='black', linewidth=1, label="DN = 100 (lower)")
    plt.vlines(100, ymin=35, ymax=10000, colors='black', linewidth=1, label="DN = 100 (upper)")
    plt.vlines(350, ymin=0.5, ymax=3500/350, colors='black', linewidth=1, label="DN = 350")

    # Diagonal boundaries
    DN_diag1 = np.logspace(np.log10(25), np.log10(100), 300)
    PS_diag1 = 1000 / DN_diag1
    plt.plot(DN_diag1, PS_diag1, color='black', linewidth=1, label="PS·DN = 1000")

    DN_diag2 = np.logspace(np.log10(100), np.log10(350), 300)
    PS_diag2 = 3500 / DN_diag2
    plt.plot(DN_diag2, PS_diag2, color='black', linewidth=1, label="PS·DN = 3500")

    # Region I shaded polygon
    region_I_x = [25, 100, 100, 25]
    region_I_y = [0.5, 0.5, 10, 0.5]
    plt.fill(region_I_x, region_I_y, color='lightgray', alpha=0.5)

    # Labels
    plt.text(30, 1, "I", fontsize=12)
    plt.text(70, 30, "II", fontsize=12)
    plt.text(400, 400, "III", fontsize=12)
    plt.text(10, 1.5, "SEP", fontsize=10)

    # Operating point
    plt.scatter(DN, PS, color='blue', s=100, edgecolors='black', zorder=5,
                label=f"Operating Point: {category}")

    plt.grid(True, which="both", linestyle='--', linewidth=0.5)
    plt.legend(loc='lower right')
    plt.tight_layout()
    plt.savefig("piping_group1_gas_with_point.png")
    plt.show()


# Example usage
if __name__ == "__main__":
    PS_example = 135   # bar
    DN_example = 50   # mm
    category_result = classify_piping_group1_gas(PS_example, DN_example)
    print(f"Input: PS = {PS_example} bar, DN = {DN_example} mm → PED Category: {category_result}")
    plot_piping_group1_gas_with_point(PS_example, DN_example, category_result)
