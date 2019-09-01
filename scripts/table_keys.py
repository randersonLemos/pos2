class Well_Keys:
    @staticmethod
    def time(): return 'TIME (day)'

    @staticmethod
    def well_state(): return 'Well state (_)'

    @staticmethod
    def cum_gas_sc(): return 'Cum. Gas SC (m3)'

    @staticmethod
    def cum_oil_sc(): return 'Cum. Oil SC (m3)'

    @staticmethod
    def cum_wat_sc(): return 'Cum. Water SC (m3)'

    @staticmethod
    def gor_sc(): return 'Gas Oil Ratio SC (m3/m3)'

    @staticmethod
    def gas_rate_sc(): return 'Gas Rate SC (m3/day)'

    @staticmethod
    def gas_rate_sc_ins(): return 'Gas Rate SC - Inst. (m3/day)'

    @staticmethod
    def oil_cut_sc(): return 'Oil Cut SC (%)'

    @staticmethod
    def oil_rate_sc(): return 'Oil Rate SC (m3/day)'

    @staticmethod
    def oil_rate_sc_ins(): return 'Oil Rate SC - Inst. (m3/day)'

    @staticmethod
    def wat_cut_sc(): return 'Water Cut SC (%)'

    @staticmethod
    def wat_rate_sc(): return 'Water Rate SC (m3/day)'

    @staticmethod
    def wat_rate_sc_ins(): return 'Water Rate SC - Inst. (m3/day)'

    @staticmethod
    def well_bhp(): return 'Well BHP (kg/cm2)'

    @staticmethod
    def well_bhpd(): return 'Well BHPD (kg/cm2/day)'

class Sector_Keys:
    @staticmethod
    def recovery_factor(): return 'Factor (%)'

    @staticmethod
    def entire_field(): return 'Entire Field'

class Special_Keys:
    @staticmethod
    def avg_pressure(): return 'Pressure (kg/cm2)'

