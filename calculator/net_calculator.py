import math

class DecimalBinaryConverter():
    
    def binary_to_decimal(self, binary):
        digits = str(binary)
        decimal = 0
        position = len(digits)-1
        for d in digits:
            if d=='1':
                decimal+=2**position
            position-=1                
        return decimal

    def decimal_to_binary(self, decimal):
        digits = []
        number = decimal
        while (number/2)>=1:
            digits.append(number%2)
            number = math.floor(number/2)
        digits.append(number)
    
        result = []
        for i in digits[::-1]:
            result.append(i)
        return result

class IpAddress:

    def __init__(self, ip: str):
        self.TOTAL_BITS = 32
        self.ip = ip
        self.prefix = 0
        self.ip_prefix = []
        self.available_bits = ''
        self.__ip_class = None
        self._identify_class()        

    def _identify_class(self):
        octets = self.ip.split(sep='.')
        first_octet = int(octets[0])
        if first_octet < 128:
            self.__ip_class = 'A'
            self.prefix = 8
            self.available_bits = '000000000000000000000000'                
        elif first_octet < 192:
            self.__ip_class = 'B'
            self.prefix = 16
            self.available_bits = '0000000000000000'                
        elif first_octet < 224:
            self.__ip_class = 'C'
            self.prefix = 24            
            self.available_bits = '00000000'                
        else:
            raise ValueError(f'La ip ingresada: {self.__ip} no es valida')

        for i in range(int(self.prefix/8)): #number of octets that prefix contains
            self.ip_prefix.append(octets[i])



    @property
    def ip_class(self):
        return self.__ip_class    

class SubnetAddress(IpAddress):
    
    def __init__(self, ip: str, subnetworks:int ):
        super().__init__(ip)
        self.__subnetworks = subnetworks
        self.__new_mac_address = None
        self.__new_prefix = None
        self.__borrowed_bits = None
        self.__bits_for_hosts = None
        self.__new_mask_binary = ''
        self.__new_mask_decimal = ''
        self.__jump = None
        self.__hosts = None
        self.__util_hosts = None
        self.__new_mask_class = ''
        self.__set_new_prefix()
        self.__set_bits_for_hosts()
        self.__set_new_mask_binary()    
        self.__binary_to_decimal()
        self.__set_jump()
        self.__calculate_hosts()

    @property
    def new_prefix(self):
        return self.__new_prefix

    @property
    def borrowed_bits(self):
        return self.__borrowed_bits

    @property
    def bits_for_hosts(self):
        return self.__bits_for_hosts

    @property
    def new_mask_binary(self):
        return self.__new_mask_binary

    @property
    def new_mask_decimal(self):
        return self.__new_mask_decimal

    @property
    def jump(self):
        return self.__jump

    @property
    def new_mask_class(self):
        return self.__new_mask_class

    @property
    def hosts(self):
        return self.__hosts

    @property
    def util_hosts(self):
        return self.__util_hosts

    def __set_new_prefix(self):
        print(f'Ejecutando ... ')
        self.__borrowed_bits = math.ceil(math.log2(self.__subnetworks))
        temp_prefix = self.prefix + self.__borrowed_bits
        if temp_prefix < self.TOTAL_BITS:
            self.__new_prefix = temp_prefix
        else:
            raise ValueError(f'El número de subredes excede la cantidad posible a generar')        

    def __set_bits_for_hosts(self):
        self.__bits_for_hosts = self.TOTAL_BITS - self.__new_prefix

    def __set_new_mask_binary(self):
        counter = 0       
        new_mask='' 
        for i in range(self.TOTAL_BITS):
            if counter < self.new_prefix:
                new_mask+='1'                
            else:
                new_mask+='0'
            if (counter+1) % 8 == 0 and (counter+1) != self.TOTAL_BITS:
                new_mask+='.'
            counter+=1

        self.__new_mask_binary = new_mask

    def __binary_to_decimal(self):
        binary_addres = self.__new_mask_binary.split('.')
        decimal_addres = []
        for octet in binary_addres:                        
            db = DecimalBinaryConverter()
            decimal_number = db.binary_to_decimal(int(octet))
            decimal_addres.append(str(decimal_number))
        self.__new_mask_decimal = '.'.join(decimal_addres)

    def __set_jump(self):
        decimal_mask = self.__new_mask_decimal.split('.')
        octet_number = 0
        for octet in decimal_mask:                        
            if int(octet)==255:
                octet_number = octet_number+1
            if int(octet) < 255 and self.__jump == None:
                #print(f'256 menos el octeto: {octet}')
                self.__jump = 256 - int(octet)                        
            if octet_number == 1:
                self.__new_mask_class = 'A'
            elif octet_number == 2:
                self.__new_mask_class = 'B'
            elif octet_number == 3:
                self.__new_mask_class = 'C'

    def __calculate_hosts(self):
        self.__hosts = 2**self.__bits_for_hosts  
        self.__util_hosts = self.__hosts-2   

    def hosts_to_ip(self, decimal:int):
        db = DecimalBinaryConverter()
        binary_jump = db.decimal_to_binary(decimal)        
        for i in range((self.TOTAL_BITS - self.prefix) - len(binary_jump)):
            binary_jump.insert(0,0)
        counter = 0
        binary_hosts = ''
        for i in binary_jump:            
            if counter > 0 and counter % 8 == 0 and counter != len(binary_jump):
                binary_hosts+='.'            
            binary_hosts+=str(i)                
            counter+=1        
        octets = binary_hosts.split('.')        
        decimal_octets = []
        for o in octets:
            position = 0
            for i in range(len(o)-1):                
                if o[i] == '1':
                    position = i
                    break
            if position == 0 and o[0] == 0:
                o = '0'
            else:
                o = o[position:]                        
            decimal_octet = db.binary_to_decimal(int(o))            
            decimal_octets.append(decimal_octet)            
        return decimal_octets


    def transform_ip_format(self, ip:list):
        result = [str(x) for x in ip]
        result = ".".join(result)        
        for i in range(len(result), 15):
            result += ' '
        return result


    def calculate_subnet_ip(self, subnet_id:int):        
        ip_hosts = self.hosts_to_ip(self.__hosts * (subnet_id-1))
        return self.transform_ip_format(self.ip_prefix+ip_hosts)
    
    def calculate_first_ip(self, subnet_id:int):
        ip_hosts = self.hosts_to_ip((self.__hosts * (subnet_id-1)) + 1)        
        return self.transform_ip_format(self.ip_prefix+ip_hosts)

    def calculate_final_ip(self, subnet_id:int):
        ip_hosts = self.hosts_to_ip((self.__hosts * (subnet_id)) - 2)
        return self.transform_ip_format(self.ip_prefix+ip_hosts)
    
    def calculate_broadcast_ip(self, subnet_id:int):
        ip_hosts = self.hosts_to_ip((self.__hosts * (subnet_id)) - 1)
        return self.transform_ip_format(self.ip_prefix+ip_hosts)


if __name__=='__main__':
    ip = input('Digite la ip: ')
    subnetworks = int(input('Digite el número de subredes deseado: '))
    sub_net = SubnetAddress(ip, subnetworks)
    print(f'clase: {sub_net.ip_class}')
    print(f'prefijo: {sub_net.prefix}')
    print(f'nuevo prefijo: {sub_net.new_prefix}')
    print(f'bits prestados: {sub_net.borrowed_bits}')
    print(f'bits para los hosts: {sub_net.bits_for_hosts}')
    print(f'Nueva mascara en bits: {sub_net.new_mask_binary}')
    print(f'Nueva mascara decimal: {sub_net.new_mask_decimal}')
    print(f'Hosts disponibles {sub_net.hosts}')
    print(f'Hosts utiles: {sub_net.util_hosts}')
    print(f'Saltos: {sub_net.jump}')
    print(f'Clase de la nueva mascara: {sub_net.new_mask_class}\n\n')
    print('                 -------------------- Tabla de direcciones ip--------------------------------    \n\n')

    print('Subred id     dirección de red           primera ip                  última ip                   broadcast       \n')

    for i in range(1, subnetworks+1):
        print(f'{i}             {sub_net.calculate_subnet_ip(i)}            {sub_net.calculate_first_ip(i)}             {sub_net.calculate_final_ip(i)}             {sub_net.calculate_broadcast_ip(i)}')

