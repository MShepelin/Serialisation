from timeit import timeit  
from tabulate import tabulate 
import sys
 
message = '''d = { 
    'PackageID' : 1539, 
    'PersonID' : 33, 
    'Name' : """MEGA_GAMER_2222""", 
    'Inventory': [i for i in range(100)],   
    'CurrentLocation': """ 
        Pentos is a large port city, more populous than Astapor on Slaver Bay,  
        and may be one of the most populous of the Free Cities.  
        It lies on the bay of Pentos off the narrow sea, with the Flatlands  
        plains and Velvet Hills to the east. 
        The city has many square brick towers, controlled by the spice traders.  
        Most of the roofing is done in tiles. There is a large red temple in  
        Pentos, along with the manse of Illyrio Mopatis and the Sunrise Gate  
        allows the traveler to exit the city to the east,  
        in the direction of the Rhoyne. 
        Pentos is a large port city, more populous than Astapor on Slaver Bay,  
        and may be one of the most populous of the Free Cities.  
        It lies on the bay of Pentos off the narrow sea, with the Flatlands  
        plains and Velvet Hills to the east. 
        The city has many square brick towers, controlled by the spice traders.  
        Most of the roofing is done in tiles. There is a large red temple in  
        Pentos, along with the manse of Illyrio Mopatis and the Sunrise Gate  
        allows the traveler to exit the city to the east,  
        in the direction of the Rhoyne. 
        """,
    'Enemy' : { 
        'PackageID' : 1539, 
        'PersonID' : 654, 
        'Name' : """HARPY_POTHER""", 
        'Inventory': [i for i in range(100)],   
        'CurrentLocation': """
            Harvard University is a private Ivy League research university in Cambridge, 
            Massachusetts. Founded in 1636 as Harvard College and named for its first 
            benefactor, the Puritan clergyman John Harvard, it is the oldest institution 
            of higher learning in the United States and among the most prestigious in the world.
         """,
         'Health' : 12545.23
        },
    'Health' : 21323.545
}''' 

setup_pickle    = '%s ; import pickle ; src=pickle.dumps(d, 2)' % message 
setup_json      = '%s ; import json; src=json.dumps(d)' % message 
setup_xml       = '%s ; from xml_marshaller import xml_marshaller ; src=xml_marshaller.dumps(d)' % message 
setup_protobuf  = '%s ; from google.protobuf.json_format import ParseDict, MessageToDict; from message_pb2 import Message; src=ParseDict(d, Message())' % message 

tests = [ 
    # (title, setup, enc_test, dec_test) 
    ('pickle (native serialization)', setup_pickle, 'pickle.dumps(d, 2)', 'pickle.loads(src)'), 
    ('json', setup_json, 'json.dumps(d)', 'json.loads(src)'), 
    ('protobuf', setup_protobuf, 'ParseDict(d, Message())', 'MessageToDict(src)'), 
    ('xml', setup_xml, 'xml_marshaller.dumps(d)', 'xml_marshaller.loads(src)'), 
] 
  
loops = 5000 
enc_table = [] 
dec_table = [] 
  
print ("Running tests (%d loops each)" % loops) 
  
for title, mod, enc, dec in tests: 
    print (title) 
  
    print("  [Encode]", enc)
    result = timeit(enc, mod, number=loops) 
    exec(mod) 
    enc_table.append([title, result, sys.getsizeof(src)]) 
  
    print("  [Decode]", dec)
    result = timeit(dec, mod, number=loops) 
    dec_table.append([title, result]) 

enc_table.sort(key=lambda x: x[1]) 
enc_table.insert(0, ['Package', 'Seconds', 'Size']) 
  
dec_table.sort(key=lambda x: x[1]) 
dec_table.insert(0, ['Package', 'Seconds']) 
  
print("\nEncoding Test (%d loops)" % loops) 
print(tabulate(enc_table, headers="firstrow")) 
  
print("\nDecoding Test (%d loops)" % loops) 
print(tabulate(dec_table, headers="firstrow"))
