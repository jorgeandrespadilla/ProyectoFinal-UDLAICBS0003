import traceback
from data import generate_data

try:
    generate_data()
except:
    print("An error occurred while generating the data:")
    traceback.print_exc()
