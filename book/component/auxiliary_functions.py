def wind_set_up(u, d, F=3000, C=4.0e-6):
    """
    Calculate wind set-up at the toe of the dike, relative to still water level.

    Parameters
    ----------
    u : float
        [m/s] Representative wind speed
    d : float
        [m] Average depth over fetch length. Take "offshore" depth as proxy.
    F : float
        [m] Fetch length, default is 3000 m (3 km)
    C : float, optional
        [-] Empirical constant, between 3.5e-6 and 4.0e-6, default is 4.0e-6
    
    Returns
    -------
    S : float
        [m] Wind set-up at toe of the dike
    """

    g = 9.81
    S = C*(u**2)/(g*d)*F  
    return S

def run_up_level(Hs, alpha):
    import numpy as np
    """
    Calculate run-up level at the toe of the dike, relative to still water level.

    Parameters
    ----------
    Hs : float
        [m] Significant wave height
    alpha : float
        [degrees] Angle of the slope of the toe of dike
    
    Returns
    -------
    Ru2 : float
        [m] Run-up level, exceeded by 2% of the waves
    """
    # Since numpy works with radians, we need to convert the angle to radians
    alpha_radians = np.radians(alpha)

    Ru2 = 8*Hs*np.tan(alpha_radians)
    return Ru2

def water_at_dike(Hs, u, Zw, Zb, alpha=20, F=10000, C2 = 4.0e-6):
    """
    Calculate the effective water elevation at the dike.

    Parameters
    ----------
    Hs : float
        [m] Significant wave height
    alpha : float
        [degrees] Angle of the slope of the toe of dike
    u : float
        [m/s] Representative wind speed
    d : float
        [m] Average depth over fetch length
    F : float
        [m] Fetch length
    Zw : float
        [m] Offshore water elevation (tidal level)
    Zb : float
        [m] Offshore bed level (or bottom level)
    
    Intermediate Parameter
    ----------------------
    d_offshore : float
        [m] Depth of water at the offshore location, Zw - Zb

    Returns
    -------
    Zd : float
        [m] Elevation of water level at the dike.
              - Equivalent to water depth, as datum is toe of dike
              - Sum of tidal level, run-up, wind set-up
    """

    d_offshore = Zw - Zb

    S = wind_set_up(u, d_offshore, F, C2)

    Ru2 = run_up_level(Hs, alpha)
    
    Zd = Zw + Ru2 + S

    return Zd