class ad5372:
    def __init__(current_register="X1A", reference_voltage=5):
            self.current_register = current_register
            self.reference_voltage = reference_voltage

    def set_reference_voltage(self, voltage):
        self.reference_voltage = voltage

    def get_reference_voltage(self):
        return self.reference_voltage

    def change_current_register(self):
        if self.current_register == "X1A":
            self.current_register = "X1B"
        else:
            self.current_register = "X1A"

    def get_current_register(self):
        return self.current_register

    def format_voltages(self, data_list): # need to convert strings to numbers between 0 and 65535
        for channel in data_list:
            channel[1] 
    
    def send_voltages(self, data_list):
        # data list should be list of [int , string] of length 32
        voltage_list = self.format_voltages(data_list)
        
        # starting with group0, channel0. then group0, channel1, and so on
        mode_address_byte = np.uint8(200) # start on group 0 channel 0: 11001000
        for value in voltage_list:
            
            self.spi.transfer2(mode_address_byte)      # address
            self.spi.transfer2(np.uint8(value >> 8) )  # high data byte
            self.spi.transfer2(np.uint8(value))        # low data byte
            mode_address_byte+=1

    

